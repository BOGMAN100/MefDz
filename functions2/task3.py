def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(*args):
    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result


result1 = gcd_multiple(3)
print(result1)  #  3

result2 = gcd_multiple(36, 48, 156, 100500)
print(result2)  #  12