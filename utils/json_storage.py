import json
import os

DATA_FILE = os.path.join('data', 'data.json')

def read_json():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

def write_json(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_recipe(user, recipe):
    data = read_json()
    for user_data in data['users']:
        if user_data['username'] == user:
            user_data['recipes'].append(recipe)
            write_json(data)
            return
    # Caso o usuário não exista, adicionar
    new_user = {"username": user, "recipes": [recipe]}
    data['users'].append(new_user)
    write_json(data)

def get_recipes(user):
    data = read_json()
    for user_data in data['users']:
        if user_data['username'] == user:
            return user_data['recipes']
    return []

def remove_recipe(user, recipe_id):
    data = read_json()
    for user_data in data['users']:
        if user_data['username'] == user:
            user_data['recipes'] = [
                recipe for recipe in user_data['recipes'] if recipe['id'] != recipe_id
            ]
            write_json(data)
            return
