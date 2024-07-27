class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'atacou'

        print(f"O {self.tipo}, {self.nome}, atacou usando {ataque}")


herois = [
    Heroi('Merlin', 150, 'mago'),
    Heroi('Arthur', 30, 'guerreiro'),
    Heroi('Bruce', 40, 'monge'),
    Heroi('Naruto', 20, 'ninja')
]

for heroi in herois:
    heroi.atacar()
