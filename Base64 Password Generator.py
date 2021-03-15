import base64
print(' ____                   __ _  _     _____                                         _    _____                           _             ')
print('|  _ \                 / /| || |   |  __ \                                       | |  / ____|                         | |            ')
print('| |_) | __ _ ___  ___ / /_| || |_  | |__) |_ _ ___ ___  _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ')
print("|  _ < / _` / __|/ _ \ '_ \__   _| |  ___/ _` / __/ __|/ _ \ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|")
print('| |_) | (_| \__ \  __/ (_) | | |   | |  | (_| \__ \__ \ (_) \ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   ')
print('|____/ \__,_|___/\___|\___/  |_|   |_|   \__,_|___/___/\___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   ')
print("                                                                                                       Author: KonstantinosAnonymous")


print("Welcome to Base64 Password Generator!")
print("This Program Is Based On Base64 Which Is A Type Of Cryptography  And It Will Help You To Make Your Passwords More Secure By Encoding Your Password many times")
loop = int(input("How Many Times Do You Want To Encode Your Password?   "))
password = input('Input Your Password:    ')
etimes = 0
encode = base64.b64encode(bytes(password, 'utf-8'))
print(encode)

for i in range(loop):
    etimes+=1
    encode = base64.b64encode(bytes(encode))
    ask2 = input("Would You Like To Continue?     ")
    if ask2=='yes' or ask2=="ye" or ask2=='y':
        print(encode)
    else:
        print('Ok We Stop Here')
        print('You Encoded Your Password',etimes,'Times')
        print("Your Password Is ",encode)
        break
