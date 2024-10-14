print("hello world 1")
 
 # i want to print formatted string

print(f"hello world {1}")

# ok now I want mutiline string example, with formatted floating point numbers in every line

print(f"""hello world {1}
hello world {2}
hello world {3}
""")

age = 20
name = "John"

print(f"hello world {age} {name}")



height = 1.75
weight = 70

bmi = weight / height ** 2

print(f"hello world {bmi:.4f}")

# def add_numbers(number1, number2):
#     result = number1 + number2
#     return result

# # You can use the function like this:
# sum = add_numbers(5, 3)

# print(f"sum is {sum}")


family = ["Sofija","Milan", "Rada","Filip"]

print(family)

for name in family:
    print(f"hello world {name}")


    # I want dictionary with keys name, age, height, weight, bmi

person = {
    "name": "John",
    "age": 20,
    "height": 1.75,
    "weight": 70,
    "bmi": 20.0
}

print(person)

print(person["name"])




