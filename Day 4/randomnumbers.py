import random
import mymodule

random_integer = random.randint(1, 20)
print(random_integer)
print(mymodule.pi)

###################################################

random_float = random.random() * 5
print(random_float)

###################################################

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")