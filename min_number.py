import sys

min_number = sys.maxsize
while True:
    command = input()
    if command == 'Stop':
        break
    if min_number > int(command):
        min_number = int(command)
print(min_number)