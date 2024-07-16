x = "vdac institute"

# count total number of vowels from the given string
count = 0
for ch in x:
    if ch == 'a' or ch == 'e'\
            or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1

print(f"Total number of vowels : {count}")