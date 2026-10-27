num_of_days = int(input("Enter the number of days: "))
values = []

for i in range(num_of_days):
    num_puzzles_solved = int(input("Enter the number of puzzles solved: "))
    values.append(num_puzzles_solved)

changing_val_index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of puzzles: "))

def replace_value(values, index, new_value):
    copy_value = values[:]
    copy_value[index] = new_value
    return copy_value


replaced_value = replace_value(values, changing_val_index, new_value)
sorted_value = sorted(replaced_value, reverse=False)

target = int(input("Enter the number of puzzles to search for: "))

def find_first(sorted_value, target):
    num_founds = 0
    index_founds = []
    for i, f in  enumerate(sorted_value):   #i found this way from google
        if f == target:
            num_founds += 1
            index_founds.append(i)
        
    if num_founds != 0:
        print(f"First matching index {index_founds[0]}")
        print(f"Matching values: {num_founds}")    
    else:
        print("Not found.")

def summarize(sorted_value):
    min_value = min(sorted_value)
    max_value = max(sorted_value)
    sum_value = sum(sorted_value)
    print(f"Minimum number of puzzles: {min_value}")
    print(f"Maximum number of puzzles: {max_value}")
    print(f"Total number of puzzles: {sum_value}")

print(f"Original: {values}")
print(f"Updated: {replaced_value}")
print(f"Sorted: {sorted_value}")
summarize(sorted_value)
find_first(sorted_value,target)