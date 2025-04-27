def print_color(text, color="reset", bold=False):
    colors = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "reset": 0
    }
    code = colors.get(color.lower(), 0)
    prefix = f"\033[{'1;' if bold else ''}{code}m"
    print(f"{prefix}{text}\033[0m")

def disable_jar(jar_file):
    if jar_file.is_file():
        print_color(f'found jar at: {jar_file}', 'cyan')
    else:
        print_color(f'jar not found at path: {jar_file}', 'red')
        return

    print_color(f'disabling jar at: {jar_file}', 'white')
    bk = jar_file.with_name(jar_file.name + '.bak')
    jar_file.rename(bk)
    print_color(f'{jar_file} Renamed to {bk}', 'cyan')

def print_patch_log(change):
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