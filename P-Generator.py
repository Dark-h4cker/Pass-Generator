import random

print("     ____                     ______                           __             ")
print("    / __ \____ ___________   / ____/__  ____  ___  _________ _/ /_____  _____ ")
print("   / /_/ / __ `/ ___/ ___/  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/ ")
print("  / ____/ /_/ (__  |__  )  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /     ")
print(" /_/    \__,_/____/____/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/      ")
print("																				")                                                                           
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%?0123456789'

number = input('==> Number of passwords: ')
number = int(number)
print("                     ")
length = input('==> Password length: ')
length = int(length)

print('\n==> Your passwords:')
print("                     ")
for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)