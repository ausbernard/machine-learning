import random
import os

def get_true_random_seed():
    """_summary_
    # Use os.urandom to get a true random seed from the operating system
    # The randomness is derived from the operating system's entropy pool, which collects environmental noise from device drivers and other sources.
    # Even though we still have to generate a true random number, which is slow, because we only have to generate a single true random number—and not an entire sequence of them—it is actually a fast enough operation.
    Returns:
        _type_: int
    """
    return int.from_bytes(os.urandom(8), 'big')

def initialize_prng():
    # get a true random seed
    seed = get_true_random_seed()
    #initialize the PRNG with the true random seed
    random.seed(seed)

def reseed_prng():
    # Periodically reseed the PRNG with a new true random seed
    seed = get_true_random_seed()
    random.seed(seed)

# initialize seed
initialize_prng()

# generate random numbers //adding time
# Default Behavior Without Seed Initialization. If you do not explicitly initialize the PRNG with a seed using random.seed(), Python uses a default seed. The default seed is typically derived from the current time or another source of entropy, ensuring that the sequence of random numbers is different each time the program runs.
for _ in range(10):
    print(random.randint(0,100))

# Reseed the PRNG periodically (e.g., after a certain number of operations or time interval)
reseed_prng()

# Generate more random numbers
for _ in range(10):
    print(random.randint(0, 100))
    
    
# O(1) time complexity
# The provided code snippet initializes the PRNG once, which involves a series of constant-time operations. There are no loops or recursive calls that would increase the time complexity based on the size of the input.