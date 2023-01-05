def get() -> list[str]:
    with open('themes/themes.txt', 'r', encoding='utf-8') as f:
        themes = [theme.strip('\n') for theme in f]
    return themes

def display(themes):
    print('Choose a theme')
    for index, theme in enumerate(themes):
        if index % 5 == 0 and index > 0:
            print()
        print(f' {index+1}. {theme.upper()}', end='')
    print()

def find(theme) -> int:
    try:
        index = int(theme)
        if index <= len(THEMES):
            return index - 1
        else:
            return 'err'
    except ValueError:
        if theme in THEMES:
            return THEMES.index(theme)
        else:
            return 'err'

THEMES = get()