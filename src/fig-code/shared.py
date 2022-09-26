from pathlib import Path
from os import mkdir

FIGDIR = Path(__file__).parents[2] / 'fig'

def get_figdir(subfolder):
    new_figdir = FIGDIR / subfolder
    new_figdir.mkdir(parents=True, exist_ok=True)
    return new_figdir
