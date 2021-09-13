import AminoLab  #библиотека https://github.com/LilZevi
import pyfiglet
from colorama import init, Fore, Back, Style
from threading import Thread


init()
print(Back.BLACK)
print(Fore.YELLOW)

print(pyfiglet.figlet_format("mt spam", font="big"))
print("         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("         ┃by shadowrun                   ")
print("         ┃https://github.com/shadowrun33/")
print("         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

email = str(input("Почта/Email > "))
password = str(input("Пароль/Password > "))
client = AminoLab.Client()
client.auth(email=email, password=password)

print("Успешный вход/Login succeeded")

com = client.my_communities()
for name, ndc_Id in zip(com.name, com.ndc_Id):
    print(f"{name} - {ndc_Id}")
ndc_Id = int(input("Id сообщества/Communit Id > "))

chat = client.my_chat_threads(ndc_Id = ndc_Id, size = 100)
for title, thread_Id in zip(chat.title, chat.thread_Id):
    print(f"{title} - {thread_Id}")
thread_Id = str(input("Id чата/Chat Id > "))

message_type = int(input("Тип сообщений/Message type > "))

message = str(input("Сообщение/Message > "))

while True:
    threads = [Thread(target = client.send_message, args=(ndc_Id, thread_Id, message, message_type)) for x in range(100)]
    for t in threads:
        t.start()
    print("spamming")


