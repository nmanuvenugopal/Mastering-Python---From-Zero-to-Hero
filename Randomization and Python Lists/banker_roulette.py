import random


names = "Angela, Ben, Jenny, Michael, Chloe"

names_list = names.split(",")
print(names_list)

random_num = random.randint(0, len(names_list))
pay_person  = names_list.pop(random_num)

print(f"{pay_person} is going to buy the meal today")
