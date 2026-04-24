with open("test.txt") as f:
    words = f.read().split()
    print("Word count:", len(words))