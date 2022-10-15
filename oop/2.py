class Cat:
    def __init__(self, name, hp=20, power=20, color='black'):
        print('Создан новый кот', name)
        self.color = color
        self.name = name
        self.hp = hp
        self.power = power

    def __str__(self):
        return 'Кот ' + self.name + ', цвет ' + self.color + ', hp ' + str(self.hp)

    def meow(self, times=1):
        print(self.name, ':', end=' ')
        for i in range(times):
            print('Мяу', end=' ')
        print()

    def getDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(self.name, ': Пока!')
            self.hp = 0
    
    def setDamage(self, enemy):
        pass
        # нужно нанести коту enemy случайный урон от 0 до self.power

barsik = Cat('Барсик', 10, 10, 'grey')
barsik.meow(5)
murzik = Cat('Мурзик')
murzik.meow()
print(barsik)
