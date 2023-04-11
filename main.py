import sys
import io
import time
from mcrcon import MCRcon
fileread = 0
print("██████╗░░█████╗░░█████╗░███╗░░██╗")
print("██╔══██╗██╔══██╗██╔══██╗████╗░██║")
print("██████╔╝██║░░╚═╝██║░░██║██╔██╗██║")
print("██╔══██╗██║░░██╗██║░░██║██║╚████║")
print("██║░░██║╚█████╔╝╚█████╔╝██║░╚███║")
print("╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝")
print()
print("Version 1.2 By litkoit")
print("Чтение файла...")
with open("db.txt", mode="at") as f:
    f.close()
with open("db.txt", mode="rt") as f:
    try:
        ipf = f.readline()
        portf = f.readline()
        passf = f.readline()
        ipf = ipf[:-1]
        portf = portf[:-1]
        passf = passf[:-1]
        print("Чтение успешно!")
        print("ip: "+ipf)
        print("port: "+portf)
        print("pass: "+passf)
        f.close()
        res = input("Применить настройки? (y or n):")
        if res == "y":
            fileread = 1
        else:
            print("Отмена изменений...")
    except io.UnsupportedOperation:
        print("Ошибка чтения файла!")
if fileread == 0:
    with open("db.txt", mode="wt") as f:
        Ip = input("IP:")
        Port = input("Порт:")
        Pass = input("Пороль:")
        mc = MCRcon(Ip, Pass, int(Port))
        print("Запись в файл...")
        filedata = [Ip, Port, Pass]
        f.write(filedata[0] + "\n")
        f.write(filedata[1] + "\n")
        f.write(filedata[2] + "\n")
        f.close()
        print("Файл записан!")
else:
    mc = MCRcon(ipf, passf, int(portf))
print("Подключаюсь...")
try:
    mc.connect()
except BaseException:
    print("Выходим...")
    time.sleep(2)
    print("Ошибка Подключения!")
    input("Нажмите ENTER для продолжения")
    sys.exit("Error 1")
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