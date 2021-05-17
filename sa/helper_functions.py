from random import sample

def generate_data(l):
    """Funkcja generująca dane do pomiaru czasu"""
    x = sample(range(1, int(1e12)), int(l))
    return x

