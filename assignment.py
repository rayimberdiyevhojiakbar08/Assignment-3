def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1


def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record


num_of_days = int(input("Enter the number of days: "))
original = []

for i in range(num_of_days):
    num_puzzles_solved = int(
        input("Enter the number of puzzles solved: ")
    )
    original.append(num_puzzles_solved)

updated = original[:]

changing_val_index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of puzzles: "))

replace_value(updated, changing_val_index, new_value)

target = int(input("Enter the number of puzzles to search for: "))

first_index = find_first(updated, target)
matching_count = updated.count(target)

stats_record = summarize(updated)
minimum, maximum, total = stats_record

sorted_value = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_value}")
print(f"Minimum number of puzzles: {minimum}")
print(f"Maximum number of puzzles: {maximum}")
print(f"Total number of puzzles: {total}")

if first_index == -1:
    print("First matching index: Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_count}")
