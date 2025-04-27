from utils import *
import shutil, re

def disable_rwg(config, options):
    server_rwg_jar = config.get_server_rwg_path(options.server_workdir)
    disable_jar(server_rwg_jar)

    workdir = options.get_workdir('server')
    patch_path = workdir.joinpath(config.rwg.patch.filepath)

    shutil.copy(patch_path, f'{patch_path}.bak')

    with open(patch_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    log = {
        "line_num": 0,
        "base": "",
        "override": "",
        "original": "",
        "skipped": False,
    }

    new_lines = []
    for i, line in enumerate(content):
        original_line = line
        line_modified = False
        indent = re.match(r'^(\s*)', line).group(1)

        for change in config.rwg.patch.changes:
            base = change.base
            override = change.override

            if base in line and base != override:
                if not line_modified:
                    new_lines.append(f"{indent}##### patched by script ######\n")
                    line_modified = True
                line = line.replace(base, override)

                # tracking
                log['base'] = base
                log['override'] = override
                log['patched'] = line.strip()
                log['original'] = original_line.strip()
            elif base in line and base == override:
                # tracking
                log['skipped'] = True

        new_lines.append(line)

    patch_path = patch_path.with_name(patch_path.name + '.override')
    with open(patch_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print_patch_log(log)