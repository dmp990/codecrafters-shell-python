import sys

def REPL():
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        print(f"{command}: command not found")

def main():
    REPL()


if __name__ == "__main__":
    main()
