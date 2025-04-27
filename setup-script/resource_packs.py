import shutil

from pathlib import Path
from utils import *

def migrate_resourcepacks(config, options):
    resouurcepacks_dir = Path(config.resourcepacks_path)
    dest = Path(options.get_resourcepacks_dest())
    print_color(f'migrating resorucepacks from: {resouurcepacks_dir} to: {dest}', 'white')

    shutil.copytree(resouurcepacks_dir, dest, dirs_exist_ok=True)
    print_color(f'successfully migrated resourcepacks to: {dest}', 'cyan')