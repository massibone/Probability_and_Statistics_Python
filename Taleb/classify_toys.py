'''
determine if a toy is "big" or "small" based on whether it's an even or odd number. 
This represents a basic concept of machine learning - learning rules from data (toy sizes) to make decisions (classification).
'''
# Suppose we have a list of toys (represented by numbers)
toys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We want to find out if a toy is big (even numbers) or small (odd numbers)
def classify_toy(size):
    if size % 2 == 0:
        return "big"
    else:
        return "small"

# Let's use machine learning (a simple rule) to classify each toy
for toy in toys:
    toy_size = classify_toy(toy)
    print(f"Toy {toy} is {toy_size}")

# Output:
# Toy 1 is small
# Toy 2 is big
# Toy 3 is small
# Toy 4 is big
# Toy 5 is small
# Toy 6 is big
# Toy 7 is small
# Toy 8 is big
# Toy 9 is small
# Toy 10 is big
