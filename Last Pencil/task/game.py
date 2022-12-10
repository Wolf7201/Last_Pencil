from random import randint

dict_name = {
    1: 'John',
    -1: 'Jack'
}

pencil_limit = ['1', '2', '3']


def be_first(name):
    if name == 'John':
        return 1
    return -1


def be_digit(input_str):
    while True:
        if input_str == '0':
            input_str = input('The number of pencils should be positive\n')
        elif input_str.isdigit():
            return int(input_str)
        else:
            input_str = input('The number of pencils should be numeric\n')


def true_gamers(input_name):
    all_gamers = dict_name.values()
    while True:
        if input_name in all_gamers:
            return be_first(input_name)
        input_name = input('Choose between {} and {}\n'.format(*all_gamers))


def pencil_limit_check(input_str, pencil_on_table):
    while True:
        if input_str in pencil_limit:
            if int(input_str) <= pencil_on_table:
                return int(input_str)
            input_str = input("Too many pencils were taken\n")
            continue
        input_str = input("Possible values: '1', '2' or '3'\n")


def game(count_pencil, gamer_key):
    while count_pencil > 0:
        print('|' * count_pencil)

        if dict_name[gamer_key] == 'John':
            print(f'{dict_name[gamer_key]}\'s turn!')
            move = input()
        else:
            print(f'{dict_name[gamer_key]}\'s turn:')
            move = bot(count_pencil)

        count_pencil -= pencil_limit_check(move, count_pencil)
        gamer_key *= -1

    return gamer_key


def bot(count_pencil):
    if count_pencil % 4 == 0:
        move = 3
    elif count_pencil % 4 == 3:
        move = 2
    else:
        move = 1
    print(move)
    return str(move)


def main():
    count_pencil = be_digit(input('How many pencils would you like to use:\n'))
    gamer_key = true_gamers((input('Who will be the first ({}, {})\n'.format(*dict_name.values()))))
    gamer_win = dict_name[game(count_pencil, gamer_key)]
    print(f'{gamer_win} won!')


if __name__ == '__main__':
    main()
