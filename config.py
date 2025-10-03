# config.py

# ─── Data directories ───────────────────────────────────────────────
source_directory      = r'D:\OneDrive\Documents\Sports Interactive\Football Manager 2024'
destination_directory = r'D:\OneDrive\Yohhan\dz\FM23\upload'
new_directory         = r'D:\OneDrive\Yohhan\dz\FM23\new'

# ─── Columns to preprocess ──────────────────────────────────────────
cols_to_prep = [
    'Acc','Wor','Vis','Thr','Tec','Tea','Tck','Str','Sta','TRO','Ref','Pun','Pos','Pen',
    'Pas','Pac','1v1','OtB','Nat','Mar','L Th','Lon','Ldr','Kic','Jum','Hea','Han','Fre',
    'Fla','Fir','Fin','Ecc','Dri','Det','Dec','Cro','Cor','Cnt','Cmp','Com','Cmd','Bra',
    'Bal','Ant','Agi','Agg','Aer',
    'xG/90','Shot/90','ShT/90','NP-xG/90','Pres C/90','Poss Lost/90','Drb/90','xA/90',
    'Pr passes/90','Sprints/90','K Ps/90','Pas %','Tck/90','Poss Won/90','Int/90','Clr/90',
    'Saves/90','xSv %','xGP/90'
]

# ─── Columns for HTML output ────────────────────────────────────────
html_output_cols = [
    'Transfer Value','Position','Name','Age',
    'GK','GK_adj','FB','FB_adj','CD','CD_adj','DM','DM_adj',
    'CM','CM_adj','W','W_adj','STR','STR_adj',
    'Height','Club'
]
