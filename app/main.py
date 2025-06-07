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


def main():
    REPL()


if __name__ == "__main__":
    main()
