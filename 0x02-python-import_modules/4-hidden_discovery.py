#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        magic_number = file.read(4)
        timestamp = file.read(4)

        dis.dis(file.read())
