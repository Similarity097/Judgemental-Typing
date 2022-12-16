import random
def random_line(EZ):
    lines = open(EZ).read().splitlines()
    return random.choice(lines)
print(random_line('EZ.txt'))


def random_line(MID):
    lines = open(MID).read().splitlines()
    return random.choice(lines)
print(random_line('MID.txt'))

def random_line(SWEAT):
    lines = open(SWEAT).read().splitlines()
    return random.choice(lines)
print(random_line('SWEAT.txt'))