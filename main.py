age = int(input("How old are you?"))
if age < 18:
    print("kids")
elif age >= 18 and age <= 65:
    print("adults")
else:
    print("seniors")
