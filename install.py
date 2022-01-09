import os

try:
    file = open('main.py','x')
except FileExistsError:
    print('The file already exists, do you wish to reinstall?')
    userin = 'y'#input('(y/n)')
    if userin not in 'yY':
        quit()
    os.remove('main.py')
    file = open('main.py','x')

init_list = [
    "first_int = int(input('Please enter the first number: ' ))\n",
    "sign_str = input('Please enter a sign from among the following +-/*: ')\n",
    "second_int = int(input('Please enter the second number: '))\n\n",
]

file.writelines(init_list)

for i in range(460):
    for a in range(460):
        file.write(f'if first_int == {i} and second_int == {a}:\n')
        file.write(f"   if sign_str == '+':\n")
        file.write(f'       print({i + a})\n')
        file.write(f"   elif sign_str == '-':\n")
        file.write(f'       print({i - a})\n')
        file.write(f"   elif sign_str == '/':\n")
        if a == 0:
            file.write("""       print("Can't divide by zero!")\n""")
        else:
            file.write(f'       print({i / a})\n')
        file.write(f"   elif sign_str == '*':\n")
        file.write(f'       print({i * a})\n')

file.close()