from os import system
from from_binary_unsign import unsign_binary
from from_deci_unsigned import unsign_deci
from from_octal_unsign import unsign_octal
from from_hexa_unsign import unsign_hexa
from from_binary import signed_binary
from from_deci import signed_deci
from from_octal import signed_octal
from from_hexa import signed_hex
from add_operation import bin_addition
from devi_operation import bin_division
from multi_operation import bin_multiplication
from sub_operation import bin_subtraction
from twos_complement import final_phase


def binary_conversion_menu():
    setting = 'unsign'
    while True:
        print("BINARY CONVERSION")
        print(f'CURRENT SETTING: {setting}')
        print("[*] CHANGE UNSIGN OR SIGN")
        print("[1] BINARY")
        print("[2] DECIMAL")
        print("[3] OCTAL")
        print("[4] HEXADECIMAL")
        print("[5] EXIT (GO BACK TO MAIN MENU)\n")

        choice = input("\nEnter your choice: ")
        system('cls')

        if choice == '*':
            print('[1] unsign\n[2] sign')
            user_choice = input('\nChange Settings: ')
            if user_choice == '1':
                setting = 'unsign'
            elif user_choice == '2':
                setting = 'sign'
            else:
                print('Wrong input!')
            system('cls')

        if choice == '1':
            user = input('\n\nEnter BINARY: ')
            if setting == 'unsign':
                unsign_binary(user)
                stop = input('\nEnter to continue...  ')

            elif setting == 'sign':
                signed_binary(user)
                stop = input('\nEnter to continue...  ')
            
            system('cls')
        elif choice == '2':
            user = input('\n\nEnter DECIMAL: ')
            if setting == 'unsign':
                unsign_deci(user)
                stop = input('\nEnter to continue...  ')

            elif setting == 'sign':
                signed_deci(user)
                stop = input('\nEnter to continue...  ')
            system('cls')

        elif choice == '3':
            user = input('\n\nEnter OCTAL: ')
            if setting == 'unsign':
                unsign_octal(user)
                stop = input('\nEnter to continue...  ')

            elif setting == 'sign':
                signed_octal(user)
                stop = input('\nEnter to continue...  ')
            system('cls')

        elif choice == '4':
            user = input('\n\nEnter HEXADECIMAL: ')
            if setting == 'unsign':
                unsign_hexa(user)
                stop = input('\nEnter to continue...  ')

            elif setting == 'sign':
                signed_hex(user)
                stop = input('\nEnter to continue...  ')
            system('cls')

        elif choice == '5':
            system('cls')
            break
        

        else:
            system('cls')

def binary_operation_menu():
    while True:
        print("BINARY OPERATION")
        print("[1] ADDITION")
        print("[2] SUBTRACTION")
        print("[3] MULTIPLICATION")
        print("[4] DIVISION")
        print("[5] TWO'S COMPLEMENT")
        print("[6] EXIT (GO BACK TO MAIN MENU)\n")

        choice = input("Enter your choice: ")
        system('cls')

        if choice == '1':
            print("Binary Operation: Addition")
            user1 = input("Enter First Number: ")
            user2 = input("Enter Second Number: ")

            print(f"ADDITION OUTPUT: {bin_addition(user1, user2)}")
            close = input("\nEnter to continue... ")
            system('cls')
        

        elif choice == '2':
            print("Binary Operation: Subtraction")
            user1 = input("Enter First Number: ")
            user2 = input("Enter Second Number: ")

            print(f"SUBRACTION OUTPUT: {bin_subtraction(user1, user2)}")
            close = input("\nEnter to continue... ")
            system('cls')

        elif choice == '3':
            print("Binary Operation: Multiplication")
            user1 = input("Enter First Number: ")
            user2 = input("Enter Second Number: ")

            print(f"MULTIPLICATION OUTPUT: {bin_multiplication(user1, user2)}")
            close = input("\nEnter to continue... ")
            system('cls')

        elif choice == '4':
            print("Binary Operation: Division")
            user1 = input("Enter First Number: ")
            user2 = input("Enter Second Number: ")

            print(f"DIVISION OUTPUT: {bin_division(user1, user2)}")
            close = input("\nEnter to continue... ")
            system('cls')

        elif choice == '5':
            print("Binary Operation: Two's Complement")
            user = input("Enter Binary: ")

            print(f'TWO COMPLEMENT OUTPUT: {final_phase(user)}')
            close = input("\nEnter to continue... ")
            system('cls')

        elif choice == '6':
            system('cls')
            break 

        else:
            system('cls')


def main_menu():
    while True:
        print("MAIN MENU")
        print("[1] BINARY CONVERSION")
        print("[2] BINARY OPERATION")
        print("[3] EXIT (CLOSES THE PROGRAM)\n")

        choice = input("Enter your choice: ")
        system('cls')

        if choice == '1':
            binary_conversion_menu()

        elif choice == '2':
            binary_operation_menu()

        elif choice == '3':
            print("Exiting the program.")
            exit()

        else:
            system('cls')



if __name__ == "__main__":
    main_menu()
