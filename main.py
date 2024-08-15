from speech.recognizer import recognize_speech
from commands.system_commands import execute_system_command, add_new_action
from models.command_classifier import classify_command, learn_new_command

def main():
    print("Spouštím AI pro ovládání PC. Poslouchám...")

    while True:
        try:
            command = recognize_speech()
            if command:
                # Klasifikace příkazu
                action = classify_command(command)
                
                # Debugging print
                print(f"Rozpoznaný příkaz: {command}")
                
                if action:
                    print(f"Akce: {action}")
                    if not execute_system_command(action, command):
                        print(f"Akce '{action}' není definována.")
                        learn_new_command(command)
                else:
                    print(f"Příkaz '{command}' není rozpoznán.")
                    learn_new_command(command)
        except (Exception, KeyboardInterrupt) as e:
            print(f"Chyba: {e}")
            break

if __name__ == "__main__":
    main()
