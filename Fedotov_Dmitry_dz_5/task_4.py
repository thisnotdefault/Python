src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[item] for item in range(1, len(src)) if src[item] > src[item - 1]]
print(result)
