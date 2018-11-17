class Cl1:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


class Cl2(Cl1):
    def __repr__(self):
        return f'It\'s a Cl2 {var1} {var2}'


cl2 = Cl2('var1', 'var2')

print(cl2)

