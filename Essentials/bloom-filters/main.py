# hash() -> # abs() -> # modulus
bits = [0] * 1016

def get_index(key):
    return abs(hash(key)) % 1016

# reading txt file and populating the bits array
with open('insert.txt', 'r') as f:
    for line in f:
        key = line.strip()
        index = get_index(key)
        bits[index] = 1

with open('new.txt', 'r') as f:
    counter_probably_in_set = 0
    counter_definitely_not_in_set = 0
    for line in f:
        key = line.strip()
        index = get_index(key)
        if bits[index] == 1:
            counter_probably_in_set += 1
            print(f"{key} is probably in the set.")
        else:            
            counter_definitely_not_in_set += 1
            print(f"{key} is definitely not in the set.")
    print(f"Total probably in set: {counter_probably_in_set}")
    print(f"Total definitely not in set: {counter_definitely_not_in_set}")
