class Weird:
    f1, f2 = 0, 1
    for _ in range(10):
        f1, f2 = f2, f1 + f2


