from themes import THEMES


def get(theme_index) -> list[str]:
    theme = THEMES[theme_index]
    with open(f'themes/{theme}.txt', 'r', encoding='utf-8') as f:
        words = [word.strip('\n') for word in f]
    return words