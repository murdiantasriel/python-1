# File: my_project/test.py
from src import greeting

def main():
    name = "Alice"
    message = greeting(name)
    print(message)

if __name__ == "__main__":
    main()
