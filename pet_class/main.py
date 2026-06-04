from pet import Pet

test_pet = Pet()
name = input("Assign pet name: ")
test_pet.set_name(name)
animal_type = input(f"what animal type {name} is? eg. Dog, Cat, Bird: ")
test_pet.set_animal_type(animal_type)
while True:
    age = input(f"how old {name} is?: ")
    try:
        age = int(age)
        if age < 0:
            print("Invalid input!")
            pass
        test_pet.set_age(age)
        break
    except Exception as e:
        print("Invalid age")
print(f"The name of the user pet is {test_pet.get_name()}")
print(f"The animal type of {test_pet.get_name()} is {test_pet.get_animal_type()}")
print(f"{test_pet.get_name()} age is {test_pet.get_age()}")

