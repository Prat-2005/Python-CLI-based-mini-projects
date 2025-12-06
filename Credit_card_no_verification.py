# Luhn Algorithm: It is used for error-checking in various applications, such as verifying card numbers.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

card_number = input("Enter your credit card number(use '-' after each 4 digits):")

# 'maketrans()' which defined in 'str' used for changing things into other form.  
card_tranalation = str.maketrans({'-': '', ' ': '' }) 

# 'translate()' used for replacing each character in the card_number using the 'card_translation'
transalted_card_number = card_number.translate(card_tranalation)

# Check whether the credit card number is valid or not
if verify_card_number(transalted_card_number):
    print("VALID!")
else:
    print("INVALID!")