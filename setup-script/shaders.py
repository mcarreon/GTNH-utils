import shutil

from pathlib import Path
from utils import *

def migrate_shaders(config, options):
    shaders_dir = Path(config.shaders_path)
    dest = Path(options.get_shaders_dest())
    print_color(f'migrating shaders from: {shaders_dir} to: {dest}', 'white')

    shutil.copytree(shaders_dir, dest, dirs_exist_ok=True)
    print_color(f'successfully migrated shaders to: {dest}', 'cyan')