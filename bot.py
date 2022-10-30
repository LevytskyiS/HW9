def exit_func(args):
    return 'Good bye!'
    
def greeting(args):
    return 'How can I help you? '

def contact_book(args):

    full_list = []

    for key, value in contacts.items():
        res = '{name} - {phone}'.format(name = key, phone = value)
        full_list.append(res)
    
    all_list = '\n'.join(full_list)
    
    return all_list


def input_error(func):
    def inner(args):
        try:
            return func(args)
        except IndexError:
            print('You also need to write a number.')
            main()
        except ValueError:
            print('This name is not in the contact book.')
            main()
        except NameError:
            print('There is no name.')
            main()
    return inner
    

@input_error 
def new_contact(new_contact):
    contacts[new_contact[0].capitalize()] = int(new_contact[1])
    return new_contact

@input_error 
def change_contact(changes):
    if changes[0].capitalize() in contacts.keys():
        contacts[changes[0].capitalize()] = changes[1]

@input_error 
def phone_number(args):
    return contacts.get(args[0].capitalize())

def parse_string(string: str):
	func = None
	args = None
	strings = string.strip()
	strings_lower = string.strip().lower()
	for key in FUNCTIONS:
		if strings_lower.startswith(key):
			func = key
			args = strings.replace(strings[:len(key)], '').strip().split()
			return FUNCTIONS[func](args)
	return func, args

contacts = {'Anna' : 456}

FUNCTIONS = {
    'hello' : greeting, 
    'add' : new_contact,
    'change' : change_contact,
    'phone' : phone_number, 
    'show all' : contact_book,
    'good bye' : exit_func,
    'exit' : exit_func,
    'close' : exit_func
}

def main():

    while True:

        user_input = input('Enter a command: ')

        if parse_string(user_input) == None:
            continue
        elif parse_string(user_input) == 'Good bye!':
            print(parse_string(user_input))
            exit()
        else:
            print(parse_string(user_input))


if __name__ == '__main__':
    main()