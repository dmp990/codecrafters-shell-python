import sys

def REPL():
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    print(f"{command}: command not found")

def main():
    while True:
        REPL()


if __name__ == "__main__":
    main()
