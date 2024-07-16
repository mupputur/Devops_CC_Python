# Write a program count each occurance of a vowel
s = "vdac institute"

#  a : ?  , e : ?  i : ? o: ? u ?

d = {}
vowels = "aeiou"
for ch in s:
    if ch in vowels:
        if ch not in d:
            d[ch] = 1   #  a: 1, i:1
        else:
            d[ch] = d[ch] + 1
print(f"Vowel Frequency: {d}")




