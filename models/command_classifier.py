# Importy
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import json
import os
from commands.system_commands import load_actions, add_new_action

# Cesty k souborům
MODEL_FILE = 'models/model.pkl'
ACTIONS_FILE = 'actions.json'
TRAINING_DATA_FILE = 'training_data.json'  # Nebo 'training_data.csv'

# Funkce pro načítání modelu
def load_model():
    try:
        with open(MODEL_FILE, 'rb') as f:
            model, vectorizer = pickle.load(f)
            return model, vectorizer
    except FileNotFoundError:
        return LogisticRegression(), CountVectorizer()

# Funkce pro uložení modelu
def save_model(model, vectorizer):
    with open(MODEL_FILE, 'wb') as f:
        pickle.dump((model, vectorizer), f)

def classify_command(command):
    model, vectorizer = load_model()
    try:
        command_vec = vectorizer.transform([command])
        logging.debug(f"Transformed command vector: {command_vec}")
        if command_vec.nnz == 0:
            logging.warning("Příkaz není rozpoznán.")
            return None
        prediction = model.predict(command_vec)
        logging.debug(f"Prediction: {prediction}")
        return prediction[0]
    except Exception as e:
        logging.error(f"Chyba při klasifikaci příkazu: {e}")
        return None

# Funkce pro načítání tréninkových dat
def load_training_data():
    if os.path.exists(TRAINING_DATA_FILE):
        try:
            with open(TRAINING_DATA_FILE, 'r') as file:
                data = json.load(file)
                return [(item['command'], item['action']) for item in data]
        except Exception as e:
            print(f"Chyba při načítání tréninkových dat: {e}")
            return []
    else:
        return []

# Funkce pro učení nových příkazů
def learn_new_command(command):
    model, vectorizer = load_model()
    actions = load_actions()

    # Získání uživatelského vstupu
    english_action = input("Zadej anglický název akce (např. 'create_new_project'): ")
    action_type = input("Zadej typ akce (např. 'keyboard_shortcut' nebo 'create_new_project'): ")

    if action_type == 'keyboard_shortcut':
        keys = input("Zadej klávesovou zkratku (např. 'ctrl+t'): ")
        add_new_action(english_action, f"keyboard_shortcut:{keys}")
    elif action_type == 'create_new_project':
        add_new_action(english_action, "create_new_project")
    else:
        print("Neznámý typ akce.")

    # Přidání nového příkazu do tréninkových dat
    training_data = load_training_data()
    training_data.append({"command": command, "action": english_action})
    
    # Příprava tréninkových dat
    X_train, y_train = zip(*[(item['command'], item['action']) for item in training_data])
    X_train_vec = vectorizer.fit_transform(X_train)
    model.fit(X_train_vec, y_train)

    # Uložení modelu a tréninkových dat
    save_model(model, vectorizer)
    with open(TRAINING_DATA_FILE, 'w') as file:
        json.dump(training_data, file, indent=4)

    print(f"Příkaz '{command}' byl naučen s anglickou akcí '{english_action}'.")
def learn_new_command(command):
    model, vectorizer = load_model()
    actions = load_actions()

    # Získání uživatelského vstupu
    english_action = input("Zadej anglický název akce (např. 'create_new_project'): ")
    action_type = input("Zadej typ akce (např. 'keyboard_shortcut' nebo 'create_new_project'): ")

    if action_type == 'keyboard_shortcut':
        keys = input("Zadej klávesovou zkratku (např. 'ctrl+t'): ")
        add_new_action(english_action, keys)
    elif action_type == 'create_new_project':
        add_new_action(english_action, "create_new_project")
    else:
        print("Neznámý typ akce.")

    # Přidání nového příkazu do tréninkových dat
    training_data = load_training_data()
    training_data.append({"command": command, "action": english_action})
    
    # Příprava tréninkových dat
    X_train, y_train = zip(*[(item['command'], item['action']) for item in training_data])
    X_train_vec = vectorizer.fit_transform(X_train)
    model.fit(X_train_vec, y_train)

    # Uložení modelu a tréninkových dat
    save_model(model, vectorizer)
    with open(TRAINING_DATA_FILE, 'w') as file:
        json.dump(training_data, file, indent=4)

    print(f"Příkaz '{command}' byl naučen s anglickou akcí '{english_action}'.")

# Počáteční tréninková data

