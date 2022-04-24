import time


class student:
    def __init__(self,firstName = "Dzmitry", lastName = "Popov", groupNumber = 2, age = 24):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age
    
    def getFullName(self):
        print(f'Имя студента: {self.firstName} {self.lastName}')
    def getAge(self):
        print(f'Возраст студента: {self.age}')
    def getGroupNumber(self):
        print(f'Номер группы студента: {self.groupNumber}')
    def setNameAge(self,new_firstName, new_lastName, new_age):
        self.firstName = new_firstName
        self.lastName = new_lastName
        self.age = new_age
    def setGroupNumber(self,new_GroupNumber):
        self.groupNumber = new_GroupNumber
dzmitry = student()
dzmitry.getFullName()
dzmitry.getAge()
dzmitry.getGroupNumber()
print("---------------------------")
"""Первый студент"""
vasya = student()
vasya.setNameAge("Vasya",'Komorov',19)
vasya.getFullName()
vasya.getAge()
vasya.setGroupNumber(6)
vasya.getGroupNumber()
print("---------------------------")
"""Второй студент"""
oleg = student()
oleg.setNameAge("Oleg",'Vobla',26)
oleg.getFullName()
oleg.getAge()
oleg.setGroupNumber(1)
oleg.getGroupNumber()
print("---------------------------")
"""Третий студент"""
semen = student()
semen.setNameAge("Semen",'Korotkov',18)
semen.getFullName()
semen.getAge()
semen.setGroupNumber(4)
semen.getGroupNumber()
print("---------------------------")
"""Четвертый студент"""
olga = student()
olga.setNameAge("Olga",'Menshova',29)
olga.getFullName()
olga.getAge()
olga.setGroupNumber(3)
olga.getGroupNumber()
print("---------------------------")
"""Пятый студент"""