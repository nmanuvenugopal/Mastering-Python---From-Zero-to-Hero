import random
# random.randint() will generate a random integer
# random.random() will generate a random floating point number.

random_num  = random.randint(0,1)
if random_num == 1:
    print("Heads")
else:
    print("Tails")
