def is_unique(s):
    return len(s) == len(set(s))

# მაგალითები
print(is_unique("html"))  # → True
print(is_unique("hello"))   # → False
