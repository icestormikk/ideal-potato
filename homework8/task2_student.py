import random

class Human():
    def __init__(self, name, age, gender, height,
                 weight, profession, happiness):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height 
        self.weight = weight
        self.profession = profession
        self.happiness = happiness

    def greeting(self):
        """Приветствие"""
        
        print(f'Привет, я {self.name}, мне {self.age} и я моя профессия - {self.profession}')

class Student(Human):
    def __init__(self, name, age, gender, height, 
                 weight, happiness, homework_done_count):
        super().__init__(name, age, gender, height, weight, "student", happiness)
        self.homework_done_count = homework_done_count

# создаём список из студентов и выводим его на экран
student_list = [Student("student" + str(i), 18, "Man", 
                170, 60, 0, random.randint(1, 8)) for i in range(10)]

# находим длину самого длинного имени студента
maxLength = 0
for i in student_list:
    if (len(i.name) > maxLength):
        maxLength = len(i.name)
print("%-15s%-20s" % ("Имя студента".ljust(maxLength + 4), "Кол-во сделанных д/з"))
for i in student_list:
    print("%-15s%-20s" % (i.name.ljust(maxLength + 4), i.homework_done_count))