# Gerer la lecture des niveaux

def read_level(file):
    with open(file, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]
    