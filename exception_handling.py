def check_number():
    try:
        num1 = int(input('Enter a number'))
        if num1%2 == 0:
            print('Even')
        else:
            print('Odd')
    except Exception as e:
        print('Invalid input', e)
    finally:
        # print('Some relavent message')
        check_number()

check_number()