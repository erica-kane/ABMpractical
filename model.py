
import random
# Set y0 and x0 to a random value
y0 = random.randint(0,99)
x0 = random.randint(0,99)
print(y0, x0)

# Move y0 randomly
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

# Move x0 randomly
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print(y0, x0)

# Set y1 and x1 to a random value 
y1 = random.randint(0,99)
x1 = random.randint(0,99)
print(y1, x1)

# Move y1 randomly
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

# Move x1 randomly 
if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print(y1, x1)

# Answer = pythaian distance between y0,x0 and y1,x1
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)