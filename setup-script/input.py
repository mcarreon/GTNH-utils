def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Please enter either y or n')
