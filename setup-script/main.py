import json

from options import *
from utils import *
from patch import *
from pathlib import Path

# config_path = './configs/test_config.json'
config_path = './configs/patch_config.json'

options = Options("./test/server", "./test/client", True, True, True, True)

# options = get_options()

with open(config_path, 'r', encoding='utf-8') as data:
    patch_config = json.load(data)

for target in patch_config:
    print_color(f'###### starting patching for {target['target']} ######', 'green')

    if len(target['patches']) == 0 or target.get('patches', {}) == {}:
        print_color(f'no patches found for {target['target']}', 'red')
        continue

    for patch in target['patches']:
        workdir = options.get_workdir(target['target'])
        patch_path = Path(f'{workdir}/{patch["filepath"]}')
        print(f'patching file at path: {patch_path}')

        if not patch_path.exists():
            print_color(f'could not find file at patch: {patch_path}', 'red')
            continue

        patch_cfg(patch_path, patch['changes'])
