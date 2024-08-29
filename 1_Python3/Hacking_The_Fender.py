import csv

compromised_users = []

with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row["Username"])

#print(compromised_users) 
#testing updated list

with open("compromised_users.txt", "w") as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

#with open("compromised_users.txt") as compromised_user_file:
    #print(compromised_user_file.read()) 
    #testing  overwritten file

import json

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#with open("boss_message.json") as boss_message:
  #print(json.load(boss_message))
  # testing json message

with open("new_passwords.txt", "w") as new_passwords_obj:
  slush_null_sig = " _  _     ___   __  ____\n/ )( \   / __) /  \(_  _)\n) \/ (  ( (_ \(  O ) )(\n\____/   \___/ \__/ (__)\n_  _   __    ___  __ _  ____  ____\n/ )( \ / _\  / __)(  / )(  __)(    \ \n) __ (/    \( (__  )  (  ) _)  ) D (\n\_)(_/\_/\_/ \___)(__\_)(____)(____/\n       ____  __     __   ____  _  _\n ___  / ___)(  )   / _\ / ___)/ )( \ \n(___) \___ \/ (_/\/    \\___ \) __ (\n      (____/\____/\_/\_/(____/\_)(_/\n __ _  _  _  __    __\n(  ( \/ )( \(  )  (  )\n/    /) \/ (/ (_/\/ (_/\ \n\_)__)\____/\____/\____/"

  new_passwords_obj.write(slush_null_sig)
  #print(slush_null_sig) #testing our code
