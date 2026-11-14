"""Construit les énoncés recadrés et les corrigés des parties d'exercices du brevet.
Usage : python3 build.py <spec.py> [id de partie…]
Le spec peut définir SOURCE = ('dnb_<centre>_<mois>_<année>.pdf', 'Centre, date année') : il remplace alors SUBJ
(obligatoire pour les années autres que 2025, dont les codes de centre se répètent)."""
import pymupdf, sys, os, re, subprocess, json, importlib.util
D = os.path.dirname(os.path.abspath(__file__)) + '/..'
SRC, OUT, BLD = D + '/src', D + '/out', D + '/build'
SUBJ = {
 'metj':  ('dnb_metropole_juin_2025.pdf',   'Métropole – Antilles-Guyane, 26 juin 2025'),
 'mets':  ('dnb_metropole_sept_2025.pdf',   'Métropole, septembre 2025'),
 'polj':  ('dnb_polynesie_juin_2025.pdf',   'Polynésie, juin 2025'),
 'pols':  ('dnb_polynesie_sept_2025.pdf',   'Polynésie, septembre 2025'),
 'asud':  ('dnb_ameri_sud_nov_2025.pdf',    'Amérique du Sud, novembre 2025'),
 'ncal':  ('dnb_caledonie_dec_2025.pdf',    'Nouvelle-Calédonie, décembre 2025'),
 'anor':  ('dnb_ameri_nord_juin_2025.pdf',  'Amérique du Nord, 4 juin 2025'),
 'asie':  ('dnb_asie_juin_2025.pdf',        'Asie, 16 juin 2025'),
 'cetr':  ('dnb_centres_etrangers_juin_2025.pdf', 'Centres étrangers, 17 juin 2025'),
}
X0, X1 = 42, 553          # largeur utile recadrée (pt)
def enonce(p, path):
    f, src = SUBJ[p['s']]
    sdoc = pymupdf.open(SRC + '/' + f)
    out = pymupdf.open()
    W, H = 595.28, 841.89
    FR = '/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf'
    FB = '/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf'
    titre = p['titre'].replace('--', '–')
    def newpage(first):
        pg = out.new_page(width=W, height=H)
        pg.insert_font(fontname='hr', fontfile=FR); pg.insert_font(fontname='hb', fontfile=FB)
        pg.insert_text((42, 30), 'Mathématiques – Annales du brevet', fontsize=8.5, fontname='hr')
        pg.insert_text((470, 30), 'M. Pluchet', fontsize=8.5, fontname='hr')
        pg.draw_line((42, 36), (553, 36), width=0.6)
        pg.insert_text((42, 820), 'Énoncé officiel du brevet (mise en page APMEP)', fontsize=7.5, fontname='hr')
        pg.insert_text((400, 820), 'DNB ' + src, fontsize=7.5, fontname='hr')
        y = 46
        if first:
            r = pymupdf.Rect(42, y, 553, y + 44)
            pg.draw_rect(r, width=1.1, radius=0.08)
            pg.insert_text((52, y + 19), 'Énoncé  •  ' + titre, fontsize=13, fontname='hb')
            pg.insert_textbox(pymupdf.Rect(52, y + 25, 545, y + 42), 'Brevet des collèges – ' + src, fontsize=9, fontname='hr')
            y += 52
            if p.get('consigne'):
                h = 14 * (1 + len(p['consigne']) // 95)
                pg.insert_textbox(pymupdf.Rect(42, y, 553, y + h + 4), '→ ' + p['consigne'], fontsize=10, fontname='hb')
                y += h + 6
        return pg, y
    pg, y = newpage(True)
    for (pn, y0, y1) in p['regions']:
        clip = pymupdf.Rect(X0, y0, X1, y1)
        h = clip.height
        if y + h > 805:
            pg, y = newpage(False)
        pg.show_pdf_page(pymupdf.Rect(42, y, 553, y + h), sdoc, pn - 1, clip=clip)
        y += h + 4
    out.save(path, garbage=4, deflate=True)
PRE = open(os.path.dirname(os.path.abspath(__file__)) + '/preamble.tex').read()
def corrige(p, path):
    src = SUBJ[p['s']][1]
    tex = (PRE + '\n\\rfoot{\\small DNB ' + src + '}\n\\begin{document}\n\\corrigetrue\n'
           '\\bandeaudnb{' + p['titre'] + '}{Brevet des collèges -- ' + src + '}\n' + p['corr'] + '\n\\end{document}\n')
    base = BLD + '/' + p['id']
    open(base + '.tex', 'w').write(tex)
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', BLD, base + '.tex'], capture_output=True, text=True)
    if r.returncode:
        err = [l for l in r.stdout.split('\n') if l.startswith('!') or l.startswith('l.')]
        raise SystemExit(p['id'] + ' : ' + ' | '.join(err[:4]))
    os.replace(base + '.pdf', path)
if __name__ == '__main__':
    spec = importlib.util.spec_from_file_location('spec', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if hasattr(m, 'SOURCE'):
        SUBJ.update({p['s']: m.SOURCE for p in m.PARTS})
    only = set(sys.argv[2:])
    for p in m.PARTS:
        if only and p['id'] not in only: continue
        enonce(p, f"{OUT}/enonce/{p['id']}.pdf")
        corrige(p, f"{OUT}/corrige/{p['id']}.pdf")
        print('ok', p['id'])
    meta = [{k: v for k, v in p.items() if k not in ('corr', 'regions')} for p in m.PARTS]
    json.dump(meta, open(f"{OUT}/{os.path.basename(sys.argv[1])[:-3]}.json", 'w'), ensure_ascii=False, indent=0)
