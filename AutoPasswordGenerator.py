import random
from symtable import Symbol

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!~@#$%^&*/.,<>\+-_"

print('''
    _         _        ____                                     _  ____                           _
   / \  _   _| |_ ___ |  _ \ __ _ ___ _____      _____  _ __ __|  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
  / _ \| | | | __/ _ \| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | |  _ / _ | '_ \ / _ | '__/ _` | __/ _ \| '__|
 / ___ | |_| | || (_) |  __| (_| \__ \__ \\ V  V | (_) | | | (_| | |_| |  __| | | |  __| | | (_| | || (_) | |
/_/   \_\__,_|\__\___/|_|   \__,_|___|___/ \_/\_/ \___/|_|  \__,_ \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|

                                                                                      -by Jaydeep Shirsath

''')

print("""
1.For Upper_case + Lower_case + Numbers + Symbols

2.For Upper_case + Lower_case + Numbers

3.For Upper_case + Lower_case + Symbols

4.For Upper_case + Lower_case

5.For Upper_case + Numbers

6.For Lower_case + Numbers
""") 
use = int(input("Enter your number: "))

if use == 1:
    Use_for = upper_case + lower_case + numbers + symbols
elif use == 2:
    Use_for = upper_case + lower_case + numbers
elif use == 3:
    Use_for = upper_case + lower_case + symbols
elif use == 4:
    Use_for = upper_case + lower_case
elif use == 5:
    Use_for = upper_case + numbers
elif use == 6:
    Use_for = lower_case + numbers

length = int(input("Enter length for password: "))

password = "".join(random.sample(Use_for, length))

print("Your password is ",password)

print('''
 _____ _                 _        _____          _   _     _
|_   _| |__   __ _ _ __ | | _____|  ______  _ __| | | |___(_)_ __   __ _
  | | | '_ \ / _` | '_ \| |/ / __| |_ / _ \| '__| | | / __| | '_ \ / _` |
  | | | | | | (_| | | | |   <\__ |  _| (_) | |  | |_| \__ | | | | | (_| |
  |_| |_| |_|\__,_|_| |_|_|\_|___|_|  \___/|_|   \___/|___|_|_| |_|\__, |
                                                                   |___/
''')