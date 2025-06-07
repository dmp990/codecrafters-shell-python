import sys

from app.commands import COMMANDS

def REPL():
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        parts = command.strip().split(" ")

        if parts[0] not in COMMANDS:
            print(f"{command}: command not found")
            continue

        if parts[0] == "exit":
            try:
                exit_code = int(parts[1])
            except (IndexError, ValueError):
                exit_code = 0
            sys.exit(exit_code)
        


def main():
    REPL()


if __name__ == "__main__":
    main()
