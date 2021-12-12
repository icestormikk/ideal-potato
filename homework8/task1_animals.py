import random


class Food:
    def __init__(self, saturation, healing):
        self.saturation = saturation
        self.healing = healing

class Fish(Food):
    def __init__(self):
        super().__init__(40,30)

class Candy(Food):
    def __init__(self):
        super().__init__(15, 10)

class Bone(Food):
    def __init__(self):
        super().__init__(14, 6)

class Meat(Food):
    def __init__(self):
        super().__init__(60, 70)

class Apple(Food):
    def __init__(self):
        super().__init__(30, 20)

class Animal:
    def __init__(self, eyes_count, limbs_count, food, health, hunger, isSleeping):
        self.eyes_count = eyes_count
        self.limbs_count = limbs_count
        self.food = food # список с объектами-наследника класса Food
        self.health = health # уровень здоровья существа
        self.hunger = hunger # уровень голода
        self.isSleeping = isSleeping
        self.name = "Animal" + str(self.__hash__())

    def makeSound(self):
        """Воспроизведение звуков, которые издаёт объект."""

        print(self.name, "издало звуки, не поддающиеся объяснению")

    def sleep(self):
        """Мгновенный перевод существа в сон."""

        self.isSleeping = True
        print(f'{self.name} теперь спит')
    
    def eat(self, meal: Food):
        """Накормить существо объектом meal."""
        
        if (self.hunger > 0):
            if [str(x) for x in self.food].contains(meal): 
                if (self.hunger - meal.saturation > 0):
                    self.hunger -= meal.saturation
                else:
                    self.hunger = 0
                self.health += meal.healing
            else:
                print(f'{self.name} не ест такое.')
        else:
            print(self.name, "не голодно")

    def info(self):
        """Вывод информации о всех атрибутах существа."""

        for i in self.__dict__:
            print(f'{i}: {self.__getattribute__(i)}')

class Mammals(Animal):
    def __init__(self, eyes_count, limbs_count, food, health, hunger, isSleeping):
        super().__init__(eyes_count, limbs_count, food, health, hunger, isSleeping)
        self.isMammalian = True

class Human(Mammals):
    def __init__(self, food, health, hunger, isSleeping,
                name, age, gender, height, weight, profession, happiness):
        super().__init__(2, 4, food, health, hunger, isSleeping)
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height 
        self.weight = weight
        self.profession = profession
        self.happiness = happiness

    def greeting(self):
        """Приветствие"""
        
        print(f'Привет, я {self.name}, мне {self.age} и моя профессия - {self.profession}') 
    
    def makeSound(self):
        sounds = ["wow", "привет", "хихи", "i know i'm not alone", "кхе", "пока", "i love cats"]

        print(self.name, end=' ')
        if (self.gender.lower() == "woman"):
            print("сказала: \"", end='')
        else:
            print("сказал: \"", end='')
        
        print(f'{sounds[random.randint(0, len(sounds) - 1)]}"')
    
    def eat(self, meal: Food):
        if (self.hunger > 0):
            if [x.__class__.__name__ for x in self.food].__contains__(meal.__class__.__name__):
                if (self.hunger - meal.saturation > 0):
                    self.hunger -= meal.saturation
                else:
                    self.hunger = 0
                self.health += meal.healing
                print(f'{self.name} съел(а) {meal.__class__.__name__}')
            else:
                print(f'{self.name} не ест такое.')
        else:
            print(f'{self.name} не голод(ен/на).', end='')

class Pet(Mammals):
    def __init__(self, eyes_count, limbs_count, food, health, hunger, isSleeping,
                 name, age, height, weight, happiness):
        super().__init__(eyes_count, limbs_count, food, health, hunger, isSleeping)
        self.isPet = True
        self.name = name
        self.age = age
        self.height = height
        self.wetght = weight
        self.health = health
        self.happiness = happiness

    def play(self):
        """Заставить существо Pet играть в одиночку."""

        happiness_up = random.randint(1,15)
        
        self.happiness += happiness_up
        
        print(f'{self.name} поиграл(а) сам(а) с собой. (+{happiness_up} к счастью)')
    
    def playWith(self, another_player):
        """Заставить сущетсво Pet играть с another_player."""

        happiness_up_self, happiness_up_ap = random.randint(15,30), random.randint(10,25)
        
        self.happiness += happiness_up_self
        another_player.happiness += happiness_up_ap

        print(f'{self.name} поиграл(а) с {another_player.name}.', end=' ')
        print(f'(+{happiness_up_self} к счастью {self.name}, +{happiness_up_ap} к счастью {another_player.name})')

    def hurt(self, target):
        """Заставить существо Pet нанести вред существу target."""
    
        if (self.happiness > 20):
            print(f'{self.name} слишком счастлив(а), чтобы бить кого-то.')
        else:
            if (target. health > 20):
                damage = random.randint(1,20)
                target.health -= damage
                print(f'{self.name} поцарапал {target.name}! Это было больно.. (-{damage} здоровья у {target.name})')
            else:
                print(f'{target.name} имеет низкий уровень здоровья!')

    def eat(self, meal):
        if (self.hunger > 0):
            if [x.__class__.__name__ for x in self.food].__contains__(meal.__class__.__name__):
                if (self.hunger - meal.saturation > 0):
                    self.hunger -= meal.saturation
                else:
                    self.hunger = 0
                self.health += meal.healing
                print(f'{self.name} успешно съел(а) {meal.__class__.__name__}')
            else:
                print(f'{self.name} не ест такое.')
        else:
            print(f'{self.name} не голод(ен/на).', end='')

class Cat(Pet):
    def __init__(self, health, hunger, name, age, height, weight, happiness):
        super().__init__(2, 4, [Fish(), Meat()], 
                         health, hunger, False, name, age, height, weight, happiness)
    
    def makeSound(self):
        print("Мяу")
    
    def to_purr(self):
        """Заставить кошку мурлыкать."""

        print(f'{self.name} издаёт довольное урчание.')

class Dog(Pet):
    def __init__(self, health, hunger, name, age, height, weight, happiness):
        super().__init__(2, 4, True, [Fish(), Meat(), Bone(), Apple()],
                         health, hunger, False, name, age, height, weight, happiness)
        self.founded_bones_count = 0
    
    def makeSound(self):
        print("Гав")

    def to_found_bone(self):
        """Отправить собаку на поиск косточки."""

        print(f'{self.name} пробует найти кость: ', end='')
        if (random.random() >= 0.5):
            self.founded_bones_count += 1
            print(f'удачно ({self.founded_bones_count} итого)')
        else:
            print("неудачно.")

hum = Human([Candy(), Apple(), Fish()], 100, 20, False, "Olya", 19, "Woman", 165, 53, "student", 80)
cat = Cat(100, 20, "Super Cat", 3, 40, 12, 60)

# приветствие субъекта Olya
hum.greeting()
# Super Cat играет с Olya
print()
cat.playWith(hum)
# Olya пробует мясо
print()
hum.eat(Meat())
# Olya пробует что-то сладкое
print()
hum.eat(Candy())
