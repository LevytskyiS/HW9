def exit_func():
    return 'Good bye!'

def greeting():
    return 'How can I help you?' 

def contact_book():
    return contacts

def new_contact(new_contact):
    try:
        contacts[new_contact[0].capitalize()] = int(new_contact[1])
    except ValueError:
        print('There is no number.')

def change_contact(changes):
    contacts[changes[0].capitalize()] = changes[1]

def phone_number(contact_name):

    if contact_name.lower() in contacts.keys() or contact_name.capitalize() in contacts.keys():
        res = contacts.get(contact_name.capitalize())
        print(res)
        return res
    else:
        print('Name not found.')

user_commands = {
    'hello' : greeting, 
    'add' : new_contact,
    'change' : change_contact,
    'phone' : phone_number, 
    'show all' : contact_book,
    'good bye' : exit_func,
    'exit' : exit_func,
    'close' : exit_func
}

contacts = {'Anna' : 852}

def get_handler(cmd):

    if isinstance(cmd, list):
        if len(cmd) > 2:
            return user_commands[cmd[0]](cmd[1 : ]) # для команд 'add', 'change'
        elif len(cmd) == 2:
            return user_commands[cmd[0]](cmd[1]) # для команди 'phone'
    else:
        return user_commands[cmd]() # для команд 'hello', 'exit', 'close', 'good bye', 'show all'


def main():
    while True: 
        user_input = input('Enter the command: ').lower()

        if user_input in user_commands.keys():
            if user_input == 'good bye' or user_input == 'exit' or user_input == 'close':
                print(get_handler(user_input))
                exit()
                
            if user_input == 'show all':
                print(get_handler(user_input))
            
            if user_input == 'hello':
                print(get_handler(user_input))
 
        else:
            user_com_list = user_input.strip().split()

            for key in user_commands.keys():
                    
                if len(user_com_list) == 3 and user_com_list[0] == key: # для команд 'add', 'change'
                    get_handler(user_com_list)
                    
                elif len(user_com_list) == 2 and user_com_list[0] == key: # для команди 'phone'
                    get_handler(user_com_list)
                    
                else:
                    continue

if __name__ == '__main__':
    main()
