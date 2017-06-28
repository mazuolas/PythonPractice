def div_count(num):
    count = 0
    while num >= 2:
        count += 1
        num = num//2
    return count

print(div_count(4))
print(div_count(2))
print(div_count(5))
