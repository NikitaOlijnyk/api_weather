import json
import os

FILE_PATH = "/Users/mykytaoliinyk/PycharmProjects/PythonProject4/.venv/jica_home/homework_4/products.json"


if os.path.exists(FILE_PATH):
    try:
        with open(FILE_PATH, "r") as file:
            products = json.load(file)
    except (json.JSONDecodeError, IOError):
        products = []
else:
    products = []

def is_add(command):
    return command.lower() == "add"

def is_delete(command):
    return command.lower() in ["del", "delete"]

def is_list(command):
    return command.lower() in ["list", "history"]

def save_to_file():
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(products, file, indent=4)
    except IOError:
        print(" Błąd zapisu do pliku.")

while True:
    try:
        item = input(" Wpisz nazwę produktu: ").strip()
        action = input("  Co zrobić z tym? (add/del/list): ").strip()

        if is_add(action):
            products.append(item)
            print("Pozycja została dodana.")
            save_to_file()

        elif is_delete(action):
            try:
                products.remove(item)
                print("️  Pozycja została usunięta.")
                save_to_file()
            except ValueError:
                print(" Nie znaleziono takiej pozycji w liście.")

        elif is_list(action):
            if products:
                print(" Lista produktów:")
                for i, p in enumerate(products, 1):
                    print(f"{i}: {p}")
            else:
                print(" Lista jest pusta.")

        else:
            print(" Nieznana komenda. Użyj: add, del, list.")

    except KeyboardInterrupt:
        print("\n Program zakończony.")
        break
