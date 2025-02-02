# A: T: G: C:     -- Only these 4 can be entered.


# Get DNA String and pattern from user:
dna_string = input("Enter DNA String: ")
enzyme_recognition_pattern = input("Enter the pattern you are looking for: ")

# Below is used for showing inputed String and pattern.
# print(f"DNA String: {dna_string} \n DNA Pattern: {enzyme_recognition_pattern}")

# Define a list to store places that the pattern is found
found_pattern = []
fragments = []

last_index = 0

# define a loop to look for pattern inside inputed String
for i in range(len(dna_string) - len(enzyme_recognition_pattern) + 1):
    if dna_string[i:i+len(enzyme_recognition_pattern)] == enzyme_recognition_pattern:
        found_pattern.append(i)
        fragments.append(dna_string[last_index:i])
        last_index = i + len(enzyme_recognition_pattern)


print(found_pattern)
print(fragments)