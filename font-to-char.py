"""
    This python code was created by pradosh-arduino 
    and when you use this code you must credit me.
"""

import sys

file_path = sys.argv[1]

try:
    with open(file_path, 'rb') as file:
        byte_count = 0
        byte = file.read(1)
        while byte:
            print(f'0x{byte.hex()}', end=", ")
            byte_count += 1
            if byte_count % 16 == 0:
                print()  # Start a new line every 16 bytes
                print("    ", end="")
            byte = file.read(1)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
