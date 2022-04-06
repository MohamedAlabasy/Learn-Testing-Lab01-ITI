def add_numbers(*args):
    if not args:
        return "empty args"
    elif len(args) > 0:
        result = 0
        for number in args:
            result += number
        else:
            return result


def compare_numbers(first_number, second_number):
    if first_number == second_number:
        return True
    elif first_number != second_number:
        return False
    else:
        print("Error")
