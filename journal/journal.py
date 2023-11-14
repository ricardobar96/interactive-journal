import os
from pathlib import Path
from os import system

entries_path = Path("Entries")

def count_entries(path):
    counter = 0
    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter

def start():
    system('cls')
    print('*' * 50)
    print('*' * 5 + " JOURNAL INITIATED " + '*' * 5)
    print('*' * 50)
    print("\n")
    print(f"Total entries: {count_entries(entries_path)}")

    option_menu = 'x'
    while not option_menu.isnumeric() or int(option_menu) not in range(1,7):
        print("Choose an option:")
        print('''
        [1] - Read entry
        [2] - New entry
        [3] - New category
        [4] - Delete entry
        [5] - Delete category
        [6] - Exit''')
        option_menu = input()
    return option_menu

def show_categories(path):
    print("Categories:")
    categories_path = Path(path)
    list_categories = []
    counter = 1

    for folder in categories_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - [{folder_str}]")
        list_categories.append(folder)
        counter += 1
    return list_categories

start()

menu = 0

if menu == 1:
    categories = show_categories(entries_path)
    pass
elif menu == 2:
    categories = show_categories(entries_path)
    pass
elif menu == 3:
    pass
elif menu == 4:
    categories = show_categories(entries_path)
    pass
elif menu == 5:
    categories = show_categories(entries_path)
    pass
elif menu == 6:
    pass