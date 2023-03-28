import math


def if_first_number():
    integers_line = input("Podaj liczby oddzielone spacją: ")
    integers_line = integers_line.replace("\n", " ").replace("\t", " ").strip()
    integers = integers_line.split()
    result = []
    for integer in integers:
        integer = int(integer)
        if integer < 2:
            result.append(f"{integer} is not prime")
        elif integer == 2:
            result.append(f"{integer} is prime number")
        elif integer % 2 == 0:
            result.append(f"{integer} is not prime")
        else:
            is_first = True
            for divider in range(3, int(math.sqrt(integer)) + 1, 2):
                if integer % divider == 0:
                    is_first = False
                    break
            if is_first:
                result.append(f"{integer} is prime number")
            else:
                result.append(f"{integer} is not prime")
    print("\n".join(result))


if_first_number()
