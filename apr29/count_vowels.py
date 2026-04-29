s = "Hello World"
count = sum(1 for c in s.lower() if c in "aeiou")
print("Vowels:", count)