x = "vdac institute"

# count total number of vowels from the given string
#vowels = ['a', 'e', 'i', 'o', 'u']
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for ch in x:
    if ch in vowels:
        count = count + 1

print(f"Total number of vowels : {count}")