import random as r
from datetime import datetime

test_samples = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


# task 3
def bruteforce(key):
    # time measurement start
    start = datetime.now()

    # bruteforce  process
    current_key = 0x0
    while current_key != key:
        current_key += 1

    # time measurement end
    end = datetime.now()
    print(f"{(end - start).total_seconds() * 1000} milliseconds are needed to bruteforce next key:\n{key:#x}")


for bits in test_samples:
    # task 1
    # as each bit represents 1 or 0 in particular position (2 possible values),
    # the amount of keys that can be represented using N-bit sequence is equal to 2^N
    amount_of_possible_uniq_keys = pow(2, bits)

    # task 2
    # as amount_of_possible_uniq_keys represents amount of all possible uniq keys including the one, where all the bits
    # are equal to 0, we need to decrease our variable by 1
    random_key = (r.randint(0, amount_of_possible_uniq_keys - 1))

    print(f"For {bits}-bit sequence:\n"
          f"Amount of uniq keys: {amount_of_possible_uniq_keys}\n"
          f"Randomly generated key: {random_key}\n")
    bruteforce(random_key)

