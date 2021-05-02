
from .key_check import key_check

def start():
    while True:
        keys = key_check()
        print("waiting press B to start")
        if keys == "B":
            print("Starting")
            break


if __name__ == '__main__':
    start()