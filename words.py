with open('words.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n\n')
    data = [item.split('\n') for item in data]

THEMES = [item[0] for item in data]
WORDS = [item[1:] for item in data]