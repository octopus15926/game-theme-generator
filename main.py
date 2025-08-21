import random

if __name__ == '__main__':
    with open("themes.txt", 'r') as t:
        themes = t.readlines()
    
    with open("special_objects.txt", 'r') as s:
        special_objects = s.readlines()
    
    random_theme_index = random.randint(0, len(themes) - 1)
    random_object_index = random.randint(0, len(special_objects) - 1)

    print(f'Create a game with a theme of: {themes[random_theme_index]}\nHere is an optional "special object": {special_objects[random_object_index]}')
