from pickle import TRUE


cort =("шалаш","дом","мама","ротор")

for key in cort:
    pol = list(filter(lambda key: key == "".join(reversed(key)),cort))
print("Полиморфы:",pol)