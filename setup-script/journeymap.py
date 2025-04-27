import shutil
from pathlib import Path

from utils import *

def apply_journeymap_unlimited_fix(config, options):
    server_journeymap_jar = config.get_server_journeymap_path(options.server_workdir)
    client_journeymap_jar = config.get_client_journeymap_path(options.client_workdir)
    client_mod_dir = options.get_mod_path('client')

    if not client_mod_dir.is_dir():
        print_color(f'failed to find client mod folder at path: {client_mod_dir}', 'red')
        return

    disable_jar(server_journeymap_jar)
    disable_jar(client_journeymap_jar)

    print_color(f'migrating jar to client mod folder: {config.journeymap_unlimited_path}', 'white')
    unlimited_file = Path(config.journeymap_unlimited_path)
    dest = client_mod_dir / unlimited_file.name
    shutil.copy(config.journeymap_unlimited_path, dest)
    print_color(f'successfully migrated jar to client mod folder: {dest}', 'cyan')
