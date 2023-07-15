import product as product
import correct_input  # Module needed to get correct values

if __name__ == '__main__':
    choise = correct_input.get_input_option()  # Сhoose how to enter data

    if choise == 'file':  # Do this if option is 'file'
        path = correct_input.get_file_name()
        product = product.get_product_from_file(path)
        print(f'Product of these sequence are {product}')  # Print a product of sequense

    if choise == 'console':  # Do this if option is 'console'
        product = product.get_product_from_console()
        print(f'Product of these sequence are {product}')  # Print a product of sequense




