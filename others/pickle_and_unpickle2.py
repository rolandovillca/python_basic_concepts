import pickle
import random

# =======================
# PICKLING DATA INTO FILE:
# =======================

# Opening a file handler:
fh = open('obj.txt', 'w')

# Create a new object:
eggs = {
    'green eggs': 'ham',
    'sam': 'I am'
}

# Lets see what is there:
print (eggs)

# Creating a new pickler:
pickler = pickle.Pickler(fh)

# Dump eggs object to file:
pickler.dump(eggs)

# =========================
# UNPICKLING DATA FROM FILE:
# =========================

# Opening out object dumpfile:
fh = open('obj.txt', 'r')

# Creating the unpickler object:
unpk = pickle.Unpickler(fh)

# Re-load the eggs object from our dumpfile:
eggs = unpk.load()

# Here is our object, safe and sound:
print(eggs)
