heights_in_feet = [5.0, 5.9, 6.1, 5.7, 6.5]

total = 0

for x in range(0, len(heights_in_feet)):
    total += heights_in_feet[x]

average_height = total / (len(heights_in_feet - 1))