import os
import platform
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
                    builtin = to_check in COMMANDS
                except IndexError:
                    print("not found")
                    continue

                if builtin:
                    print(f"{to_check} is a shell builtin")
                    continue
                
                # Search path
                path = os.getenv("PATH")
                if platform.system() == "Windows":
                    delimiter = ";"
                else:
                    delimiter = ":"

                for p in path.split(delimiter):
                    try:
                        entries = os.listdir(p)
                    except FileNotFoundError:
                        continue
                    if to_check in entries:
                        print(f"{to_check} is {p}/{to_check}")
                        executable = True
                        break
                else:
                    executable = False
                
                if not executable and not builtin:
                    print(f"{to_check}: not found")


def main():
    REPL()


if __name__ == "__main__":
    main()
