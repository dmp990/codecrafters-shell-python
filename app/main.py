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

        match parts[0]:
            case "exit":
                try:
                    exit_code = int(parts[1])
                except (IndexError, ValueError):
                    exit_code = 0
                sys.exit(exit_code)
            case "echo":
                try:
                    print(" ".join(parts[1:]))
                except IndexError:
                    print()
            case "type":
                try:
                    to_check = parts[1]
                    known = to_check in COMMANDS
                except IndexError:
                    known = False

                if known:
                    print(f"{to_check} is a shell builtin")
                else:
                    print(f"{to_check}: not found")


def main():
    REPL()


if __name__ == "__main__":
    main()
