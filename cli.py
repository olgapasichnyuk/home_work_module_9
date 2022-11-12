contacts_book = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'There is no phone with that name, please enter valid name.'
        # except ValueError:
        # return 'Give me name and phone please'
        except IndexError:
            return 'Input please name and phone after the command "change" or "add"\nor name after the command "phone"'

    return inner


@input_error
def add(raw_user_input):
    global contacts_book
    name = raw_user_input[1].capitalize()
    number = raw_user_input[2]
    contacts_book[name] = number
    return f'The contact with name {name} and number {number} was added'


@input_error
def change(raw_user_input):
    global contacts_book
    name = raw_user_input[1].title()
    number = raw_user_input[2]
    old_number = contacts_book[name]
    contacts_book[name] = number
    msg = f'The phone number for contact with name {name} was changed:\n old number {old_number}\n new number {number}'

    return msg


@input_error
def get_number(raw_user_input):
    global contacts_book
    name = raw_user_input[1].title()
    number = contacts_book[name]
    msg = f"The contact with name {name} contain number {number}"
    return msg


def show_all(*_):
    global contacts_book
    if contacts_book:

        msg = ["-" * 40, "{:^20} | {:^17}".format("NAME", "TELEPHONE NUMBER"), "-" * 40]

        for key, value in contacts_book.items():

            contact = "{:^20} | {:^17}".format(key, value)

            msg.append(contact)

        msg = "\n".join(msg)

    else:
        msg = "Your contacts book is empty."

    return msg


def main():
    handler = {
        'add': add,
        'change': change,
        'phone': get_number,
        'show': show_all
    }

    while True:
        user_command = input('For starting write the word "hello", please: ')
        if user_command == 'hello':
            print('How can I help you?')
            break

    while user_command not in ['good bye', 'close', 'exit']:
        user_command = input('Write command: ')
        user_input = user_command.lower().split()
        cmd_name = user_input[0]

        if cmd_name in handler:
            msg = handler[cmd_name](user_input)

        elif cmd_name not in handler:
            msg = 'I do not understand the command'

        print(msg)

    print('Good bye!')


if __name__ == '__main__':
    main()
