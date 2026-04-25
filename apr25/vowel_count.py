s = input("Enter string: ").lower()
count = sum(1 for c in s if c in "aeiou")
print("Vowels:", count)