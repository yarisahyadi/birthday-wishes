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
import os

# Credentials
MY_EMAIL = os.environ.get("MY_EMAIL") # change this to your email
PASSWORD = os.environ.get("PASSWORD")
birthday_file = "birthdays.csv"

# today's birthday checker
def is_there_birthday(today_birthday, date):
  # check if there is any birthday in today's date
  return date in today_birthday

# today's birthday data
today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_data = pd.read_csv(birthday_file)
today_data = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_data.iterrows()}

# establishing connection and preparing email account
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)

# Check if today matches a birthday in the birthdays.csv
if is_there_birthday(today_data, today):
  # establishing connection and preparing email account
  with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    # Sending the email
    for date in today_data:
      person = today_data[date]
      with open(f"/content/letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        letter = letter_file.read().replace("[NAME]", person["name"])
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                          msg=f"Subject: Happy Birthday {person["name"]}!!\n{letter}".encode("utf-8"))

else:
  print("No one is having birthday today :v")
