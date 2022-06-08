import random
import math

def three_a(x):
    y = (x + random.randint(-10, 10)*math.sin(x))
    return y

