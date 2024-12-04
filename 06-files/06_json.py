import json

user = {
    "name": "Kevin",
    "programming_languages": ["TS", "JS", "Go", "Python", "PHP"],
    "interest": ["3D Printing", "Climbing"],
    "alive": True,
    "height": 1.82
}

with open("user.json", "w") as file:
    file.write(json.dumps(user))

with open("user.json") as file:
    # contents = file.read()  -> use loads if it is a string!
    loaded_user = json.load(file)
    print(loaded_user)