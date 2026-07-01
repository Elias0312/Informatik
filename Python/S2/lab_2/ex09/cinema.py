rooms = [[10, 10, 10, 10], [15, 15, 15], [15, 20, 30, 40, 50]]
count = 0

for i in range(3):
    current = rooms.pop(0)
    current_count = 0
    for k in current:
        current_count += k
    print( f"Cinema {i + 1} has {current_count} seats")
    count += current_count

print(f"All rooms together have {count} seats")