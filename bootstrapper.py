import os, datetime, math, time, sys, shutil
from myosotis import * 

HIGHEST_NUMBER = 16
TEARDOWN = True
WAIT = False
HANG_TIME = 0.25


def teardown():
    user_input = input("Press any key to begin teardown...")
    # Delete the numbers folder
    shutil.rmtree('numbers')

def is_prime(number):
    # Check if a number is prime
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False 
    return True 

def get_prime_factors(number):
    # Get the prime factors of a number
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number = number / i
            if number > 2:
                factors.append(int(number))
    return factors

# Create a new folder for the numbers
os.makedirs('numbers', exist_ok=True)

counter = 3
while counter < HIGHEST_NUMBER:
    # Wait for a bit
    if WAIT:
        time.sleep(HANG_TIME)
    #if not is_prime(counter):
    # create a new file in the numbers folder 
    with open(os.path.join('numbers', str(counter)) + ".md", 'w') as f:
        # write the header 
        f.write("# " + str(counter))
        # write a newline and then any prime factors
        f.write("\n\nPrime factors: ")
        prime_factors_for_this_number = get_prime_factors(counter)
        for factor in prime_factors_for_this_number:
            f.write(f"[[{factor}]] , ")
        f.close()
    counter += 1


if TEARDOWN:
    teardown()