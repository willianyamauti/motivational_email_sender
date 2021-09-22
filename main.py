import smtplib
import random
import datetime as dt

my_email = "willianyamauti@yahoo.com"
password = 'mulvbxzxzmolllhh'

now = dt.datetime.now()
with open('quotes.txt', 'r') as quotes:
    quote_list = quotes.readlines()
    quote_of_the_day = random.choice(quote_list)

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="primordiosdubhe@gmail.com",
                        msg=f'Subject:Quote of the day\n\n{quote_of_the_day}')


