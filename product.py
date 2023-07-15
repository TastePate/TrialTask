import correct_input


def get_product_from_file(path: str) -> float:
    product = 1
    not_numbers = []
    with open(path, 'r') as f:  # Open file using 'with' construction which allows us to close a file automatically
        for line in f:  # Loop will read file line by line
            try:
                product *= int(line)  # Try to parse a line and add it to product
            except ValueError:
                print(
                    f'File "{path}" contains value "{line}" that is not a number')  # In case when we catch not a number we should write a message and ignore this value
        return product  # Print a product of sequense


def get_product_from_console() -> float:
    n = -1
    product = 1
    print('Enter numbers one by one. Sequence stop on 0')
    while n != 0:  # While we get another number we add it to product. If number is 0 then we break sequence
        n = correct_input.get_number()  # Get number
        if n != 0:
            product *= n  # Add it to product
    return product
