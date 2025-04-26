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

    if server_journeymap_jar.is_file():
        print_color(f'found server journeymap jar at: {server_journeymap_jar}', 'cyan')
    else:
        print_color(f'server journeymap jar not found at path: {server_journeymap_jar}', 'red')
        return

    if client_journeymap_jar.is_file():
        print_color(f'found client journeymap jar at: {client_journeymap_jar}', 'cyan')
    else:
        print_color(f'client journeymap jar not found at path: {client_journeymap_jar}', 'red')
        return

    print_color(f'disabling jar at: {server_journeymap_jar}', 'white')
    bk = server_journeymap_jar.with_name(server_journeymap_jar.name + '.bak')
    server_journeymap_jar.rename(bk)
    print_color(f'{server_journeymap_jar} Renamed to {bk}', 'cyan')

    print_color(f'disabling jar at: {client_journeymap_jar}', 'white')
    bk = client_journeymap_jar.with_name(client_journeymap_jar.name + '.bak')
    client_journeymap_jar.rename(bk)
    print_color(f'{client_journeymap_jar} Renamed to {bk}', 'cyan')

    print_color(f'migrating jar to client mod folder: {config.journeymap_unlimited_path}', 'white')
    unlimited_file = Path(config.journeymap_unlimited_path)
    dest = client_mod_dir / unlimited_file.name
    shutil.copy(config.journeymap_unlimited_path, dest)
    print_color(f'successfully migrated jar to client mod folder: {dest}', 'cyan')
