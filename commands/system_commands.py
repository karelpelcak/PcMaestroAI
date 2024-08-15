import os
import pyautogui
import json
import logging

logging.basicConfig(level=logging.DEBUG)
ACTIONS_FILE = 'actions.json'

def execute_system_command(command, inputUser):
    actions = load_actions()
    logging.debug(f"Loaded actions: {actions}")
    try:
        logging.debug(f"Executing system command: {command}")
        for action in actions:
            if action in command:
                action_type = actions[action]
                if action_type == "create_new_project":
                    project_name = inputUser.replace("Vytvoř nový projekt", "").strip()
                    if project_name:
                        create_new_project(project_name)
                    else:
                        logging.warning("Název projektu není zadaný.")
                else:
                    pyautogui.hotkey(*action_type.split('+'))
                return True
        logging.warning(f"Unknown command: {command}")
        return False
    except Exception as e:
        logging.error(f"Error executing command: {e}")
        return False

def create_new_project(project_name):
    documents_path = os.path.expanduser("~/Documents")
    new_folder_path = os.path.join(documents_path, project_name)
    
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        logging.info(f"Složka '{project_name}' byla vytvořena v '{documents_path}'.")
    except Exception as e:
        logging.error(f"Chyba při vytváření složky: {e}")

def load_actions():
    if os.path.exists(ACTIONS_FILE):
        try:
            with open(ACTIONS_FILE, 'r') as file:
                actions = json.load(file)
                logging.debug(f"Actions loaded: {actions}")
                return actions
        except Exception as e:
            logging.error(f"Chyba při načítání akcí: {e}")
            return {}
    else:
        return {}

def add_new_action(english_action, action_type):
    actions = load_actions()
    actions[english_action] = action_type
    with open(ACTIONS_FILE, 'w') as file:
        json.dump(actions, file, indent=4)
