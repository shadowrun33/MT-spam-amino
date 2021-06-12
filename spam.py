import amino
import pyfiglet
from colorama import init, Fore, Back, Style
from threading import Thread

init()
print(Back.BLACK)
print(Fore.YELLOW)

num = 0
comIds = []
chatIds = []

print(pyfiglet.figlet_format("mt spam", font="big"))
print("         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("         ┃by shadowrun                   ")
print("         ┃https://github.com/shadowrun33/")
print("         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
email = str(input("Почта/Email > "))
password = str(input("Пароль/Password > "))
client = amino.Client()
client.login(email=email, password=password)

print("Успешный вход/Login succeded")

com = client.sub_clients(0, 100)
for name, comId in zip(com.name, com.comId):
    print(f"{name} - {comId}")

com1d = str(input("comId > "))

subclient = amino.SubClient(com1d, profile=client.profile)

print("Зашли в сообщество/Entered comunity")

chat = subclient.get_chat_threads(start=0, size=100)
for title, chatId in zip(chat.title, chat.chatId):
    print(f"{title} - {chatId}")

chatId = str(input("chatId > "))
messagetype = int(input("Тип сообщений/Message type > "))
message = str(input("Сообщение/Message > "))
kak = int(input("1) Спам определенного колличества/Define how many.\n2) Спам без остановок/Nonstop spam.\n> "))
if kak == 1:
    n = 0
    colvo = int(input("Сколько/How many?\n1 заход = 6 сообщений/1 = 6 messages.\n> "))
    while n < colvo:
        T = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T2 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T3 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T4 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T5 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T6 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T.start()
        T2.start()
        T3.start()
        T4.start()
        T5.start()
        T6.start()
        n+=1
        print("Спам в процессе/Spamming")
elif kak == 2:
    while True:
        T = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T2 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T3 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T4 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T5 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T6 = Thread(target=subclient.send_message, args=(chatId, message, messagetype))
        T.start()
        T2.start()
        T3.start()
        T4.start()
        T5.start()
        T6.start()
        print("Спам в процессе/Spamming")
else:
    print("Ты дурак?/R u dumb?")
    exit
    


