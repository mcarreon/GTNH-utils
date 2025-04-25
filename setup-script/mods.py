import shutil

from pathlib import Path
from utils import *

def migrate_mods(options, mod_path):
    for file in Path(mod_path).rglob('*'):
        if not file.is_file():
            continue

        rel = file.relative_to(mod_path)
        subfolder = rel.parts[0] if len(rel.parts) > 1 else None

        if subfolder == 'server':
            dest_root = Path(options.server_workdir)
        elif subfolder == 'client':
            dest_root = Path(options.client_workdir)
        else:
            print_color('Non-organized file detected, skipping', 'yellow')
            continue

        dest = dest_root.joinpath('mods').joinpath(*rel.parts[1:])
        dest.parent.mkdir(parents=True, exist_ok=True)

        if not dest.exists():
            shutil.copy(file, dest)
            print_color(f'Copied {file} → {dest}', 'cyan')
        else:
            print_color(f"Skipped {file}; {dest} already exists", 'yellow')