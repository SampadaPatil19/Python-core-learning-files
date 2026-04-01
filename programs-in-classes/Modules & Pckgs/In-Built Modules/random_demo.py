import random

print("Random float number between 0 and 1:\n",random.random())

print("Random integer between 10 and 50:\n",random.randint(10, 50))

colors = ['red', 'blue', 'green', 'yellow', 'orange']
print("Random choice from colors list:\n",random.choice(colors))

cards = ['2H', '3D', '5S', '9C', 'KH']
random.shuffle(cards)
print("Shuffled cards list:\n",cards)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampled_numbers = random.sample(numbers, 4)
print("Random sample of 4 numbers from the list:\n",sampled_numbers)

print("Random uniform float between 1 and 10:\n", random.uniform(1, 10))

# random.gauss is used to generate a random number based on Gaussian distribution
# Gaussian Distribution is defined by its mean(average) & standard deviation(width of distribution)

mean = 0
std_dev = 1
print("Random number based on Gaussian Distribution with mean 0 and std deviation 1:\n", random.gauss(mean, std_dev))