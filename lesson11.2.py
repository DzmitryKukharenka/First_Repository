import re
regul = '^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'

inpTime = input("Введите время: ")

result = re.match(regul, inpTime)
if result:
    print("Время корректно")
else:
    print("Ошибка ввода.")