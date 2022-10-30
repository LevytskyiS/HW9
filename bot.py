def decor(func):
    def wrapper(arg):
        try:
            return func(arg)
        except IndexError:
            return 'There is no phone number. Enter name and phone.' # If user didn`t put the number, only name.
        except ValueError: 
            return 'Number must contain only numbers.' # If number contains letters
        except KeyError:
            return 'Wrong command. Try again.' # This command is not in the dictionary with commands. 

    return wrapper

@decor 
def greeting(greet):
    return 'How can I help you? '

@decor
def exit_func(bye):
    return 'Good bye!'

@decor
def contact_book(show_all):

    full_list = []
    for key, value in all_contact.items():
        res = '{name} - {phone}'.format(name = key, phone = value)
        full_list.append(res)
    all_list = '\n'.join(full_list)
    return all_list

@decor
def new_contact(list_name_number : list):
    all_contact[list_name_number[0].capitalize()] = int(list_name_number[1])

@decor
def change_contact(list_available_name_and_new_number: list):
    if list_available_name_and_new_number[0].capitalize() in all_contact:
        all_contact[list_available_name_and_new_number[0].capitalize()] = int(list_available_name_and_new_number[1])
    else:
        return 'Name not found.'

@decor 
def phone_number(name_in_book: list):
    if name_in_book[0].capitalize() in all_contact.keys():
        return all_contact.get(name_in_book[0].capitalize())
    else:
        return 'This name is not found in your contacts.'


FUNCTIONS = {
    'hello' : greeting, 
    'add' : new_contact,
    'change' : change_contact,
    'phone' : phone_number, 
    'show all' : contact_book,
    'good bye' : exit_func,
    'exit' : exit_func,
    'close' : exit_func,
}

all_contact = {'Anna' : 321} # Key and value were added for testing

@decor
def handle(inp_by_user : str):

    inp_by_user = inp_by_user.lower().split()
    if ' '.join(inp_by_user[0:2]) == 'show all' or ' '.join(inp_by_user[0:2]) == 'good bye':
        func = ' '.join(inp_by_user[0:2])
    else:
        func = inp_by_user[0]
    args = inp_by_user[1:]
    
    if len(inp_by_user) == 1:
        return FUNCTIONS[func](args)

    elif func == 'show all' or func == 'good bye':
        return FUNCTIONS[func](args)

    elif len(inp_by_user) == 2 or len(inp_by_user) > 2:
        return FUNCTIONS[func](args)

while True:
    
    user_input = input('Enter the command: ')
    user_handler = handle(user_input)
    
    if user_handler == 'Good bye!':
        print(user_handler)
        exit()
    elif user_handler:
        print(user_handler)
