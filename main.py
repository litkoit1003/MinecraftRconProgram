import time

from mcrcon import MCRcon
print("██████╗░░█████╗░░█████╗░███╗░░██╗")
print("██╔══██╗██╔══██╗██╔══██╗████╗░██║")
print("██████╔╝██║░░╚═╝██║░░██║██╔██╗██║")
print("██╔══██╗██║░░██╗██║░░██║██║╚████║")
print("██║░░██║╚█████╔╝╚█████╔╝██║░╚███║")
print("╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝")
print()
print("Version 1.0 By litkoit")
Ip = input("IP:")
Port = input("Порт:")
Pass = input("Пороль:")
mc = MCRcon(Ip, Pass, int(Port))
print("Подключаюсь...")
mc.connect()
print("Подключено!")
print("Введите quitt для выхода")
while 1 == 1:
    Comm = input(">")
    if Comm == "quitt":
        print("Выходим...")
        mc.disconnect()
        break
    out = mc.command(Comm)
    print(out)
time.sleep(5)