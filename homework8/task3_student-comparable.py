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

    def __setattr__(self, __name: str, __value: any) -> None:
        if (not ["name", "gender", "profession"].__contains__(__name)):
            return super().__setattr__(__name, max(0, __value))
        return super().__setattr__(__name, __value)

class Student(Human):
    def __init__(self, name, age, gender, height, 
                 weight, happiness, homework_done_count):
        super().__init__(name, age, gender, height, weight, "student", happiness)
        self.homework_done_count = homework_done_count
    
    def __eq__(self, __o: object) -> bool:
        return int(self.homework_done_count == __o.homework_done_count)

    def __ne__(self, __o: object) -> bool:
        return int(self.homework_done_count != __o.homework_done_count)

    def __lt__(self, __o: object) -> bool:
        return int(self.homework_done_count < __o.homework_done_count)

    def __gt__(self, __o: object) -> bool:
        return int(self.homework_done_count > __o.homework_done_count)
    
    def __le__(self, __o: object) -> bool:
        return int(self.homework_done_count <= __o.homework_done_count)

    def __ge__(self, __o: object) -> bool:
        return int(self.homework_done_count >= __o.homework_done_count)
        

# создаём список студентов и сортируем их по кол-ву выполненных д/з
student_list = [Student("student" + str(i), random.randint(6, 20), "Man", 
                170, 60, 0, random.randint(0, 8)) for i in range(10)]
student_list.sort()

# находим длину самого длинного имени студента
maxLength = 0
for i in student_list:
    if (len(i.name) > maxLength):
        maxLength = len(i.name)
print("%-15s%-20s" % ("Имя студента".ljust(maxLength + 4), "Кол-во сделанных д/з"))
for i in student_list:
    print("%-15s%-20s" % (i.name.ljust(maxLength + 4), i.homework_done_count))