cort = ("шалаш","дом","мама","ротор")
for key in cort:
    print(key)
    pol = list(filter(lambda x: str(key) == "".join(reversed(key)),cort))
print("Полиморфы:",pol)