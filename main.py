import random

def flager(answer):
    while True:
        if answer.lower() == "да":
            return True
        if answer.lower() == "нет":
            return False
        else:
            print("Введено не валидное значение")
            print("Укажите (Да/Нет): ", end="")
            answer = input()

def generate_password(length, chars):
    for _ in range(chars):
        password = ""
        pass_list = random.sample(symd, length)
        for i in range(len(pass_list)):
            password += pass_list[i]
        print(password)

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"
AMBIGUOUS_SYMBOLS = "il1Lo0O"

chars = ""
pass_amount = 0
pass_length = 0
pass_numder = False
pass_cap_let = False
pass_str_let = False
pass_symbol = False
pass_ambiguous_symbols = False


print("Укажите колличество паролей: ", end="")
pass_amount = int(input())
print("Укажите необходимую длину пароля(-ей): ", end="")
pass_length = int(input())
print("Пароль содержит цифры (Да/Нет): ", end="")
pass_numder = flager(input())
print("Пароль содержит прописные буквы (Да/Нет): ", end="")
pass_cap_let = flager(input())
print("Пароль содержит строчные буквы (Да/Нет): ", end="")
pass_str_let = flager(input())
print("Пароль содержит символы (Да/Нет): ", end="")
pass_symbol = flager(input())
print("Исключать ли неоднозначные символы (Да/Нет): ", end="")
pass_ambiguous_symbols = flager(input())

if pass_numder:
    chars += DIGITS
if pass_cap_let:
    chars += LOWERCASE_LETTERS
if pass_str_let:
    chars += UPPERCASE_LETTERS
if pass_symbol:
    chars += PUNCTUATION
if pass_ambiguous_symbols:
    for c in chars:
        chars.replace(c, "")

symd = ".".join(chars)
symd = symd.split(".")

generate_password(pass_length, pass_amount)
