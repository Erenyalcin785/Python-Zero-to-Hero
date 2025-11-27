def to_number(roman):
    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    prev = 0

    for x in roman:
        value = numbers.get(x) #m 1000


        if value > prev and prev != 0:

            # total = total - prev + (value - prev) = total + value - 2*prev
            total += value- 2 * prev
        else:
            total += value

        prev = value #prev 1000

    return total


print(to_number("MCMVII"))  # 1907
print(to_number("MMXI"))    # 2011
print(to_number("XC"))      # 90
print(to_number("MCMXC"))   # 1990
