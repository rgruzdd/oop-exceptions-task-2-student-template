from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    num = []

    for x in str_with_ints.split():
        try:
            num.append(int(x))
        except ValueError:
            print('Error code: invalid literal for int() with base 10: ' + "'" + x + "'")
            return
    try:
        num_list = num[0] / num[1]
        return float(num_list)

    except ZeroDivisionError:
        print('Error code: division by zero')





