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
print("Version 1.1 By litkoit")
print("Reading a file...")
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
        print("Reading successful!")
        print("ip: "+ipf)
        print("port: "+portf)
        print("pass: "+passf)
        f.close()
        res = input("Apply settings? (y or n):")
        if res == "y":
            fileread = 1
        else:
            print("Cancel changes...")
    except io.UnsupportedOperation:
        print("File read error!")
if fileread == 0:
    with open("db.txt", mode="wt") as f:
        Ip = input("IP:")
        Port = input("Port:")
        Pass = input("Password:")
        mc = MCRcon(Ip, Pass, int(Port))
        print("Writing to file...")
        filedata = [Ip, Port, Pass]
        f.write(filedata[0] + "\n")
        f.write(filedata[1] + "\n")
        f.write(filedata[2] + "\n")
        f.close()
        print("The file has been written!")
else:
    mc = MCRcon(ipf, passf, int(portf))
print("Connecting...")
mc.connect()
print("Connected!")
print("Write quitt to exit")
while 1 == 1:
    Comm = input(">")
    if Comm == "quitt":
        print("Exiting...")
        mc.disconnect()
        break
    out = mc.command(Comm)
    print(out)
time.sleep(5)