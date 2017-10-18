import numpy as np
from utils import *
import random

data = open('dinos.txt', 'r').read()
data= data.lower()
chars = list(set(data))
print(sorted(chars))
data_size, vocab_size = len(data), len(chars)
print('There are %d total characters and %d unique characters in your data.' % (data_size, vocab_size))