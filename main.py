from random import choices
import string
import argparse


def generator(length=12, upper=False, lower=False, digit=False, pun=False):
    character = ''

    if upper:
        character += string.ascii_uppercase
    if lower:
        character += string.ascii_lowercase
    if digit:
        character += string.digits
    if pun:
        character += string.punctuation
    if character == '':
        character += string.ascii_letters

    return ''.join(choices(character, k=length))


def main():
    parse = argparse.ArgumentParser(description='Password Generator')
    parse.add_argument('length', type=int, help='Length of Password')
    parse.add_argument(
        '-u', '--upper', help='upper case character', action='store_true')
    parse.add_argument(
        '-l', '--lower', help='lower case character', action='store_true')
    parse.add_argument(
        '-d', '--digit', help='digit case character', action='store_true')
    parse.add_argument(
        '-p', '--pun', help='pun case character', action='store_true')

    args = parse.parse_args()
    password = generator(
        length=args.length,
        upper=args.upper,
        lower=args.lower,
        digit=args.digit,
        pun=args.pun)

    print(password)


if __name__ == '__main__':
    main()
