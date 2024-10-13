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


