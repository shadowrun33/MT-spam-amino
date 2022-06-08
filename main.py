import amino
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
client = amino.Client()
try:
    client.login(email=email, password=password)
except amino.lib.util.exceptions.VerificationRequired as e:
    print(f'Verification Required, verification link:\n{e.args[0]["url"]}')
    input("\nWhen ready press enter.")

print("Успешный вход/Login succeeded")

com = client.sub_clients()
for name, comId in zip(com.name, com.comId):
    print(f"{name} - {comId}")

comId = int(input("Id сообщества/Community Id > "))

subclient = amino.SubClient(comId = comId, profile = client.profile)

chat = subclient.get_chat_threads(start = 0, size = 100)
for title, chatId in zip(chat.title, chat.chatId):
    print(f"{title} - {chatId}")
chatId = str(input("Id чата/Chat Id > "))

messageType = int(input("Тип сообщений/Message type > "))

message = str(input("Сообщение/Message > "))

while True:
    threads = [Thread(target = subclient.send_message, args=(chatId, message, messageType)) for x in range(100)]
    for t in threads:
        t.start()
