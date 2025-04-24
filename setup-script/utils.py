def print_color(text, color="reset", bold=False):
    colors = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "reset": 0
    }
    code = colors.get(color.lower(), 0)
    prefix = f"\033[{'1;' if bold else ''}{code}m"
    print(f"{prefix}{text}\033[0m")