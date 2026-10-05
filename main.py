##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Import all the required packages
import datetime as dt
import pandas as pd
import random
import smtplib

# Credentials
MY_EMAIL = "" # change this to your email
PASSWORD = ""

# today's birthday checker
def is_there_birthday(today_birthday):
  today = dt.datetime.now().day
  return today in today_birthday.to_list()

# today's birthday data
today = dt.datetime.now().day

with open("/content/birthdays.csv", "r") as birthday_file: # change the file path, I'm using dummy data in colab here
    birthdays_data = pd.read_csv(birthday_file)
    today_birthday = birthdays_data[birthdays_data.day == today]
    person_data = today_birthday.to_dict(orient="records")
    # print(person_data)

# establishing connection and preparing email account
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)

# Check if today matches a birthday in the birthdays.csv
if is_there_birthday(birthdays_data.day):
  letter_number = random.randint(1, 3)
  # Sending the email
  for person in person_data:
    with open(f"/content/letter_templates/letter_{letter_number}.txt") as letter_file:
      letter = letter_file.read().replace("[NAME]", person["name"])
      connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                        msg=f"Subject: Happy Birthday {person["name"]}!!\n{letter}".encode("utf-8"))

  connection.close()
else:
  print("No one is having birthday today :v")
