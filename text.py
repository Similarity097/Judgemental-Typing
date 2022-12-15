import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('ez.txt') as f:
    lines = f.read().splitlines()

print(lines)

for i in range(1,4):
    print(lines[i])
    print(len(lines[i]))