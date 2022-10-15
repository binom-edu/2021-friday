class Cat:
    def meow(self):
        print('Мяу')

    color = 'black'

barsik = Cat()
barsik.meow()
murzik = Cat()
murzik.meow()
barsik.color = 'red'
print(barsik.color)
print(murzik.color)
