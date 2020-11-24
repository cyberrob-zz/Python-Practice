import json

dictionary = "files/data.json"

data = json.load(open(dictionary))

def translate(word_input):
    if word_input.lower() in data.keys():
        return data[word_input.lower()]
    else:
        return "No translation exist! Try other word."

user_input = input("Enter a word for translation: ")

print(translate(user_input))