import sys
import socket

conexao = int(input("Digite o numero do tipo de conexao a ser realizada no scan: TCP(1) ou UDP(2)? "))

if conexao == 1:
    ip = input("Digite o IP: ")
    port = 1

    f = open("portscannertcp.txt", "w+")
    print("SCANNING...")
    while port < 65536:
        teste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        teste.settimeout(0.1)

        req = teste.connect_ex((ip, port))
        if req == 0:
            print("[TCP] " + str(port) + " [OPEN]")
            f.write("[TCP] " + str(port) + " [OPEN] \r\n")
        teste.close()
        port = port + 1 

if conexao == 2:
    ip = input("Digite o IP: ")
    port = 1 

    f = open("portscannerudp.txt", "w+")
    print("SCANNING...")
    while port < 65536:
        teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        teste.settimeout(0.1)

        req = teste.connect_ex((ip, port))
        print(req)
        if req != 0:
            print("[UDP] " + str(port) + " [OPEN]")
            f.write("[UDP] " + str(port) + " [OPEN] \r\n")
        teste.close()
        port = port + 1

print("DONE")
