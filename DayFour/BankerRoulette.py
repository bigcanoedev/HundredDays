names = ["Ted, Tim, Teddy, Chris, Evan, Wes"]
name = names.split(", ")

import random

num_of_names = len(names)

random_name = random.randint(0, num_of_names - 1)

payer = names[random_name]

print(payer + " will pay the banker")