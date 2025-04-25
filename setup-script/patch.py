import shutil, re, json

from pathlib import Path
from utils import *

def apply_patches(options, config_path):
    with open(config_path, 'r', encoding='utf-8') as data:
        patch_config = json.load(data)

    for target in patch_config:
        print_color(f'###### starting patching for {target['target']} ######', 'blue')

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

def patch_cfg(patch_path, changes):
    # save a backup
    shutil.copy(patch_path, f'{patch_path}.bak')

    # read the file
    with open(patch_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # sets to keep track of bases
    unmatched_bases = {change['base'] for change in changes}
    changes_made = []

    # patch content
    new_lines = []
    for i, line in enumerate(content):
        original_line = line
        line_modified = False
        indent = re.match(r'^(\s*)', line).group(1)

        for change in changes:
            base = change['base']
            override = change['override']

            log = {
                "line_num": i + 1,
                "base": base,
                "override": override,
                "original": original_line.strip(),
                "skipped": False,
            }

            if base in line and base != override:


                if not line_modified:
                    new_lines.append(f"{indent}##### patched by script ######\n")
                    line_modified = True
                line = line.replace(base, override)

                # tracking
                log['patched'] = line.strip()
                changes_made.append(log)
                unmatched_bases.discard(base)
            elif base in line and base == override:
                # tracking
                log['skipped'] = True
                changes_made.append(log)
                unmatched_bases.discard(base)

        new_lines.append(line)

    # write to the original file
    patch_path = patch_path.with_name(patch_path.name + '.override')
    with open(patch_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    for change in changes_made:
        if not change['skipped']:
            print_color(
                f"🔧 Line {change['line_num']}: Successfully patched '{change['base']}'",
                "cyan"
            )
            print_color(f"   ↳ Before: {change['original']}", "white")
            print_color(f"   ↳ After:  {change['patched']}", "yellow")
        else:
            print_color(
                f"⚠️ Line {change['line_num']}: Base '{change['base']}' is identical to '{change['override']}' and was skipped, check config'",
                "magenta"
            )

    for missing in unmatched_bases:
        print_color(f"❌ Base text not found: {missing}", "red")