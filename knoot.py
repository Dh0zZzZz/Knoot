choice = ""

while True:
    print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   *&@@@@&/   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@% @@@@@@@@@@@@@@@@@@@@@@ ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@ @@,(@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/ (@@@@@*@@@@@@@@@@@@@@@@@@@  @&###& @@@@@@@@@
@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     *@@@@@        %@@@@@&&&%#######%@ @@@@@@@@
@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@,@@@@@##########################&%@@@@@@@@
@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*    /@@@@%##########################&@%@@@@@@@
@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##########################&@ @@@@@@@
@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##########################&&@@@@@@@@
@@@@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&%%%%#%##############@ @@@@@@@@
@@@@@@@@@@@@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@&(.    %@@&###&,@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/@@@@@@@@@@@@@@@@@@@@@@@ @@& @@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@ (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@/**************,@@@@@@@@@@@@@@@@@@@@@ @@`\n""")
    print("Welcome to Knoot, if this is your first launch, be sure to change the keys, and server address (Line 26 of the script).")
    print("Linux Firewall Rules : Lines 397 & 401 for Normal Sequence, 468 & 472 for -30 Seconds Code(in order to prevent potential delay) ")
    print("Windows Firewall Rules : 636 & 640 for Normal Sequence, 707 & 711 for -30 Seconds Code(in order to prevent potential delay) ")
    #Secret key for the first exchange
    secret = 'XAXOTPPROJETAZAZ'
    #Secret key for the first port of the sequence
    secretport1cle = 'KCXWXPWFFHAPPCZE'
    #Secret key for the second port of the sequence
    secretport2cle = 'QBRNIHOVVBXAIAVF'
    #Secret key for the third port of the sequence
    secretport3cle = 'GLHFYXQIKWZXWAMR'
    #Server IP
    Addr_serv = "localhost"
    print("1) Client")
    print("2) Server")
    print("3) Credit")
    print("4) Exit")
          
    choice = input("Enter Choice:")

    choice = choice.strip()

    if (choice == "1"):
        print("1")
        logo = """██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗   
        ██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝   
        █████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝    
        ██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗    
        ██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗   
        ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   
                                                    
        ██████╗██╗     ██╗███████╗███╗   ██╗████████╗
        ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝
        ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   
        ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   
        ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   
        ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                    
        """
        print(logo)
        import socket
        import os
        import time
        import socket
        import datetime
        import subprocess
        import time
        from time import sleep
        import os
        import re
        import hmac, base64, struct, hashlib, time
        import platform
        from datetime import datetime
        now = datetime.now()
        def is_between(time, time_range):
                if time_range[1] < time_range[0]:
                    return time >= time_range[0] or time <= time_range[1]
                return time_range[0] <= time <= time_range[1]
        print(int(now.strftime("%S")))
        print((now.strftime("%S")))
        # Create hotp token
        def get_hotp_token(secret, intervals_no):
            key = base64.b32decode(secret, True)
            msg = struct.pack(">Q", intervals_no)
            #conversions between Python values and C structs represente
            h = hmac.new(key, msg, hashlib.sha1).digest()
            o = o = h[19] & 15
            #Generate a hash using both of these. Hashing algorithm is HMAC
            h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
            #unpacking
            return h
        def get_totp_token(secret):
            #ensuring to give the same otp for 30 seconds
            x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
            #adding 0 in the beginning till OTP has 6 digits
            while len(x)!=6:
                x+='0'
            return x
        if int(now.strftime("%S"))>=20 and int(now.strftime("%S"))<=30 :
                    print("Next OTP too close, waiting for a new one")
                    sleep(6)
        if int(now.strftime("%S"))>=50 and int(now.strftime("%S"))<=59 :
                    print("Next OTP too close, waiting for a new one")
                    sleep(6)
        #clé
        def get_totp_token_30(secret):
            current_time = int(time.time())
            f =str(get_hotp_token(secret, intervals_no=(current_time-30)//30))
            while len(f)!=6:
                f+='0'
            return f

        if platform.system() == 'Linux':
            ipserveur = input("Enter server IP or press enter for localhost :") or "localhost";
            if ipserveur == "localhost":
                print("Localhost by default")
            print(int(now.strftime("%S")))
            if int(now.strftime("%S"))>=20 and int(now.strftime("%S"))<=30 :
                print("Next OTP too close, waiting for a new one")
                sleep(11)
            if int(now.strftime("%S"))>=50 and int(now.strftime("%S"))<=59 :
                print("Next OTP too close, waiting for a new one")
                sleep(11)
            data = input("Enter TOTP code : \n");
            lecodeutiise = data
            print("telnet {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2]));
            # Create a client socket
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            # Connect to the server
            print(ipserveur)
            clientSocket.connect(("{}".format(ipserveur),9090));
            # Send data to server : data = "Hello Server!";
            clientSocket.send(data.encode());
            # Receive data from server
            dataFromServer = clientSocket.recv(1024);
            # Print to the console
            print(dataFromServer.decode());
            print(type(dataFromServer));
            encoding = 'utf-8'
            b'hello'.decode(encoding)
            bytes(dataFromServer).decode("utf-8") 
            #while True:
            print(dataFromServer)
            sleep(1)
            if dataFromServer == (b'Hello Client!') and lecodeutiise == (get_totp_token(secret)) :
                print("Sequence Normal")
                sleep(2)
                print(dataFromServer)
                #os.system("telnet {} {}".format(ipserveur, secretport1))
                sleep(0)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport2))
                sleep(0)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport2cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport2cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport3))!:
                sleep(0)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport3cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport3cle))[:-2], 2))
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif dataFromServer == (b'Hello Client!') and lecodeutiise == (get_totp_token_30(secret)):
                print("OTP - 30 OTP - 30 OTP - 30 OTP - 30 OTP - 30 :")
                sleep(1)
                print(dataFromServer)
                #os.system("telnet {} {}".format(ipserveur, secretport1))
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport1cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport1cle))[:-2], 2))
                sleep(0)
                #os.system("telnet {} {}".format(ipserveur, secretport2))
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport2cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport2cle))[:-2], 2))
                sleep(0)
                #os.system("telnet {} {}".format(ipserveur, secretport3))!:
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport3cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport3cle))[:-2], 2))
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                print("Wrong code")
                os.execl(sys.executable, sys.executable, *sys.argv)
        elif platform.system() == 'Windows':
            print("Windows")
            ipserveur = input("Enter server IP or press enter for localhost") or "localhost";
            if ipserveur == "localhost":
                print("Localhost by default")
            data = input("Entrez code OTP : \n");
            lecodeutiise = data
            print("telnet {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2]));
            # Create a client socket
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            # Connect to the server
            print(ipserveur)
            clientSocket.connect(("{}".format(ipserveur),9090));
            # Send data to server : data = "Hello Server!";
            clientSocket.send(data.encode());
            # Receive data from server
            dataFromServer = clientSocket.recv(1024);
            # Print to the console
            print(dataFromServer.decode());
            print(type(dataFromServer));
            encoding = 'utf-8'
            b'hello'.decode(encoding)
            bytes(dataFromServer).decode("utf-8") 
            #while True:
            print(dataFromServer)
            print(lecodeutiise)
            print(get_totp_token(secret))
            sleep(3)
            if dataFromServer == (b'Hello Client!') and lecodeutiise == (get_totp_token(secret)):
                print("Sequence Normal")
                print(dataFromServer)
                #os.system("telnet {} {}".format(ipserveur, secretport1))
                sleep(1)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport1cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport2))
                sleep(1)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport2cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport2cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport3))!:
                sleep(1)
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport3cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token(secretport3cle))[:-2], 2))
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif dataFromServer == (b'Hello Client!') and lecodeutiise == (get_totp_token_30(secret)):
                print("OTP - 30:")
                sleep(3)
                if int(now.strftime("%S"))>=25 and int(now.strftime("%S"))<=30 :
                    print("Next code is too close, waiting for a new one ...")
                    sleep(7)
                if int(now.strftime("%S"))>=55 and int(now.strftime("%S"))<=59 :
                    print("Next code is too close, waiting for a new one ...")
                    sleep(7)
                print(dataFromServer)
                else:
                print("Wrong code")
                os.execl(sys.executable, sys.executable, *sys.argv)
                #os.system("telnet {} {}".format(ipserveur, secretport1))
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport1cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport1cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport2))
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport2cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport2cle))[:-2], 2))
                #os.system("telnet {} {}".format(ipserveur, secretport3))!:
                os.system("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport3cle))[:-2], 2))
                print("nc -vz {} {}".format(ipserveur, (get_totp_token_30(secretport3cle))[:-2], 2))
                os.execl(sys.executable, sys.executable, *sys.argv)
    elif (choice == "2"):
      print(2)
      logo = """██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗               
                ██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝               
                █████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝                
                ██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗                
                ██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗               
                ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝               
                                                                        
                ███████╗███████╗██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ 
                ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██║   ██║██╔══██╗
                ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██║   ██║██████╔╝
                ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██║   ██║██╔══██╗
                ███████║███████╗██║  ██║ ╚████╔╝ ███████╗╚██████╔╝██║  ██║
                ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                """
    print(logo)


    import time
    import platform
    time.sleep(3)
    if platform.system() == 'Linux':
        print("")
        import socket
        import datetime
        from datetime import datetime
        from datetime import timedelta
        import subprocess
        import time
        from time import sleep
        import os
        import re
        import hmac, base64, struct, hashlib, time
        import sys
        from datetime import datetime
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        now = datetime.now()
        def act(x):
            return x+10
        X = 30
        result = datetime.now() - timedelta(seconds=X)


        def wait_start(runTime, action):
            startTime = time(*(map(int, runTime.split(':'))))
            while startTime > datetime.today().time(): 
                sleep(1)
            return action

        def is_between(time, time_range):
            if time_range[1] < time_range[0]:
                return time >= time_range[0] or time <= time_range[1]
            return time_range[0] <= time <= time_range[1]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        def get_hotp_token(secret, intervals_no):
            key = base64.b32decode(secret, True)
            msg = struct.pack(">Q", intervals_no)
            h = hmac.new(key, msg, hashlib.sha1).digest()
            o = o = h[19] & 15
            h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
            #unpacking
            return h
        def get_totp_token(secret):
            x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
            while len(x)!=6:
                x+='0'
            return x
        
        def get_totp_token_30(secret):
            current_time = int(time.time())
            f =str(get_hotp_token(secret, intervals_no=(current_time-30)//30))
            while len(f)!=6:
                f+='0'
            return f


        

        knock_sequence = []


        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        serverSocket.bind(("{}".format(Addr_serv),9090));
        serverSocket.listen();

        while(True): 
            (clientConnected, clientAddress) = serverSocket.accept();
            print("Request from client : %s:%s"%(clientAddress[0], clientAddress[1]));
            dataFromClient = clientConnected.recv(1024)
            print("Code received :%s"%(dataFromClient.decode()));

            if (dataFromClient.decode()) != (get_totp_token(secret)) and (dataFromClient.decode()) != (get_totp_token_30(secret)) :
                clientConnected.send("Wrong code".encode());
                log_nonformat = 'Connection from {} with wrong code {}/{} at {}:{}:{}'.format((clientAddress[0]),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                log_format = str(log_nonformat)
                with open('logax.txt', 'a') as f:
                    f.write(log_format + '\n')
            elif (dataFromClient.decode()) == (get_totp_token(secret)):    
                    print("SEQUENCE DE PORT NORMAL")
                    stockage = (dataFromClient.decode)
                    clientConnected.send("Hello Client!".encode())
                #if int(now.strftime("%S"))>=32 and int(now.strftime("%S"))<=40 :
                #    print("Prochain OTP trop proche, attendre 5 seconde")
                #    sleep(6)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    #insert timeout
                    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    PORTS = [(get_totp_token(secretport1cle))[:-2], (get_totp_token(secretport2cle))[:-2], (get_totp_token(secretport3cle))[:-2]]
                    sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                    for i, s in enumerate(sockets):
                        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        #sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                        #serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                        #serverSocket.bind(("0.0.0.0",9999));
                        #serverSocket.listen();
                        #s.listen(1)
                        #conn, addr = clientConnected.accept()
                        #print('Knock depuis:', addr)
                        #knock_sequence.append(PORTS[i])
                        s.bind(('{}'.format(Addr_serv), int(PORTS[i])))
                        s.listen(1)
                        print('Le serveur écoute sur le port', PORTS[i])
                    knock_sequence = []
                    while True:
                        for i, s in enumerate(sockets):
                            s.listen()
                            conn, addr = s.accept()
                            print('Knock depuis:', addr)
                            knock_sequence.append(PORTS[i])
                            if knock_sequence == PORTS:
                        #
                        #
                        #
                                s = clientAddress[0]
                                print(f"ClientAddress: {clientAddress}")
                        #
                                #now = datetime.datetime.now()
                                print('sequence ok!')
                                log_nonformat = 'Connection from {}  Normal sequence  {}/{} a {}:{}:{}'.format((s),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                                log_format = str(log_nonformat)
                                with open('logax.txt', 'a') as f:
                                    f.write(log_format + '\n')
                        #
                                os.system("iptables -I INPUT 1 -s {} -j ACCEPT ; echo regle_ouverture_valide".format(s))
                                print('Ouverture du port pour {} '.format(s))
                                time.sleep(5)
                        #
                                os.system("iptables -D INPUT 1 ; echo regle_fermeture_valide")
                                print('Fermeture du port pour {}'.format(s))
                                knock_sequence = []
                                sleep(5)
                                print("purge socket")
                                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                #
                                serverSocket.close()
                                conn.close()
                                #
                                #                          
                                s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                os.execl(sys.executable, sys.executable, *sys.argv)
            elif (dataFromClient.decode()) == (get_totp_token_30(secret)):
                print("SEQUENCE DE PORT -30")
                stockage = (dataFromClient.decode)
                clientConnected.send("Hello Client!".encode())
                #if int(now.strftime("%S"))>=32 and int(now.strftime("%S"))<=40 :
                #    print("Next TOTP too close waiting for a new one ...")
                #    sleep(6)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                #insert timeout
                s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                PORTS = [(get_totp_token_30(secretport1cle))[:-2], (get_totp_token_30(secretport2cle))[:-2], (get_totp_token_30(secretport3cle))[:-2]]
                sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                for i, s in enumerate(sockets):
                        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        #sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                        #serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                        #serverSocket.bind(("0.0.0.0",9999));
                        #serverSocket.listen();
                        #s.listen(1)
                        #conn, addr = clientConnected.accept()
                        #print('Knock depuis:', addr)
                        #knock_sequence.append(PORTS[i])
                        s.bind(('{}'.format(Addr_serv), int(PORTS[i])))
                        s.listen(1)
                        print('Le serveur écoute sur le port :', PORTS[i])
                knock_sequence = []
                while True:
                    for i, s in enumerate(sockets):
                        s.listen()
                        conn, addr = s.accept()
                        print('Knock depuis:', addr)
                        knock_sequence.append(PORTS[i])
                        if knock_sequence == PORTS:
                    #nettoyer les règles déja éxistantes dans l'iptables
                    #[EMPLACEMENT]
                    #Créer une variable "s" qui convertira "addr" en str pour extraire l'ip source et l'utilisé dans la règle.
                            s = clientAddress[0]
                            print(f"ClientAddress: {clientAddress}")
                    #s = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s).group+()
                            #now = datetime.datetime.now()
                            print('sequence ok!')
                            log_nonformat = 'Connection from {} with previous totp {}/{} at {}:{}:{}'.format((s),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                            log_format = str(log_nonformat)
                            with open('logax.txt', 'a') as f:
                                f.write(log_format + '\n')
                    #ajouter li [INTERFACE] , si mauvaise par défault
                            os.system("iptables -I INPUT 1 -s {} -j ACCEPT ; echo regle_ouverture_valide".format(s))
                            print('Ouverture du port pour {} '.format(s))
                            time.sleep(3)
                    #ajoute li [INTERFACE] , si mauvaise par défault
                            os.system("iptables -D INPUT 1 ; echo regle_fermeture_valide")
                            print('Fermeture du port pour {}'.format(s))
                            knock_sequence = []
                            sleep(5)
                            print("purge socket")
                            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                            serverSocket.close()
                            conn.close()
                            #s.close()
                            #os.execv(sys.executable, ['python'] + sys.argv)
                            s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            os.execl(sys.executable, sys.executable, *sys.argv)
            else : print("else")

    elif platform.system() == 'Windows':
        print("Windows")
        print("Launching") 
        import socket
        import datetime
        from datetime import datetime
        from datetime import timedelta
        import subprocess
        import time
        from time import sleep
        import os
        import re
        import hmac, base64, struct, hashlib, time
        import sys
        import telnetlib
        from datetime import datetime
        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        now = datetime.now()
        print((now.strftime("%S")))
        def act(x):
            return x+10
        X = 30
        result = datetime.now() - timedelta(seconds=X)


        def wait_start(runTime, action):
            startTime = time(*(map(int, runTime.split(':'))))
            while startTime > datetime.today().time(): 
                sleep(1)
            return action

        def is_between(time, time_range):
            if time_range[1] < time_range[0]:
                return time >= time_range[0] or time <= time_range[1]
            return time_range[0] <= time <= time_range[1]
        print(int(now.strftime("%S")))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        def get_hotp_token(secret, intervals_no):
            key = base64.b32decode(secret, True)
            msg = struct.pack(">Q", intervals_no)
            h = hmac.new(key, msg, hashlib.sha1).digest()
            o = o = h[19] & 15
            h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
            #unpacking
            return h
        def get_totp_token(secret):
            x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
            while len(x)!=6:
                x+='0'
            return x
        
        def get_totp_token_30(secret):
            current_time = int(time.time())
            f =str(get_hotp_token(secret, intervals_no=(current_time-30)//30))
            while len(f)!=6:
                f+='0'
            return f


        

        knock_sequence = []


        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        serverSocket.bind(("{}".format(Addr_serv),9090));
        serverSocket.listen();

        while(True): 
            (clientConnected, clientAddress) = serverSocket.accept();
            print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
            dataFromClient = clientConnected.recv(1024)
            print(clientAddress[0])
            print(dataFromClient.decode());

            print(dataFromClient)
            print("client0")
            print(clientAddress[0])
            print("client1")
            print(clientAddress[1])
            if (dataFromClient.decode()) != (get_totp_token(secret)) and (dataFromClient.decode()) != (get_totp_token_30(secret)):
                clientConnected.send("Wrong code".encode());
                log_nonformat = 'Connection from {} with wrong code {}/{} a {}:{}:{}'.format((clientAddress[0]),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                log_format = str(log_nonformat)
                with open('logax.txt', 'a') as f:
                    f.write(log_format + '\n')
            elif (dataFromClient.decode()) == (get_totp_token(secret)):    
                    print("SEQUENCE DE PORT NORMAL")
                    stockage = (dataFromClient.decode)
                    clientConnected.send("Hello Client!".encode())
                #if int(now.strftime("%S"))>=32 and int(now.strftime("%S"))<=40 :
                #    print("Prochain OTP trop proche, attendre 5 seconde")
                #    sleep(6)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    #insert timeout
                    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    PORTS = [(get_totp_token(secretport1cle))[:-2], (get_totp_token(secretport2cle))[:-2], (get_totp_token(secretport3cle))[:-2]]
                    sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                    for i, s in enumerate(sockets):
                        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        #sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                        #serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                        #serverSocket.bind(("0.0.0.0",9999));
                        #serverSocket.listen();
                        #s.listen(1)
                        #conn, addr = clientConnected.accept()
                        #print('Knock depuis:', addr)
                        #knock_sequence.append(PORTS[i])
                        s.bind(('{}'.format(Addr_serv), int(PORTS[i])))
                        s.listen(1)
                        print('Le serveur écoute sur le port', PORTS[i])
                    knock_sequence = []
                    while True:
                        for i, s in enumerate(sockets):
                            s.listen()
                            conn, addr = s.accept()
                            print('Knock depuis:', addr)
                            knock_sequence.append(PORTS[i])
                            if knock_sequence == PORTS:
                        #nettoyer les règles déja éxistantes dans l'iptables
                        #[EMPLACEMENT]
                        #Créer une variable "s" qui convertira "addr" en str pour extraire l'ip source et l'utilisé dans la règle.
                                s = clientAddress[0]
                                print(f"ClientAddress: {clientAddress}")
                        #s = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s).group+()
                                #now = datetime.datetime.now()
                                print('sequence ok!')
                                log_nonformat = 'Connection from {}  with normal sequence {}/{} at {}:{}:{}'.format((s),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                                log_format = str(log_nonformat)
                                with open('logax.txt', 'a') as f:
                                    f.write(log_format + '\n')
                        #ajouter li [INTERFACE] , si mauvaise par défault
                                subprocess.run(['netsh', 'advfirewall', 'fireewall', 'add', 'rule', '{}', 'name=SSH', 'dir=in', 'action=allow', 'protocol=TCP', 'localport=22'.format(s)])
                                print('Ouverture du port pour {} '.format(s))
                                time.sleep(3)
                        #ajoute li [INTERFACE] , si mauvaise par défault
                                subprocess.run(['netsh', 'advfirewall', 'firewall', '***', 'rule', '{}', 'name=SSH', 'dir=in', 'action=allow', 'protocol=TCP', 'localport=22'.format(s)])
                                print('Fermeture du port pour {}'.format(s))
                                knock_sequence = []
                                sleep(5)
                                print("purge socket")
                                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                                serverSocket.close()
                                conn.close()
                                #s.close()
                                #os.execv(sys.executable, ['python'] + sys.argv)                            
                                s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                os.execl(sys.executable, sys.executable, *sys.argv)
            elif (dataFromClient.decode()) == (get_totp_token_30(secret)):
                print("SEQUENCE DE PORT -30")
                stockage = (dataFromClient.decode)
                clientConnected.send("Hello Client!".encode())
                #if int(now.strftime("%S"))>=32 and int(now.strftime("%S"))<=40 :
                #    print("Prochain OTP trop proche, attendre 5 seconde")
                #    sleep(6)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                #insert timeout
                s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                PORTS = [(get_totp_token_30(secretport1cle))[:-2], (get_totp_token_30(secretport2cle))[:-2], (get_totp_token_30(secretport3cle))[:-2]]
                sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                for i, s in enumerate(sockets):
                        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        #sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
                        #serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                        #serverSocket.bind(("0.0.0.0",9999));
                        #serverSocket.listen();
                        #s.listen(1)
                        #conn, addr = clientConnected.accept()
                        #print('Knock depuis:', addr)
                        #knock_sequence.append(PORTS[i])
                        s.bind(('{}'.format(Addr_serv), int(PORTS[i])))
                        s.listen(1)
                        print('Le serveur écoute sur le port :', PORTS[i])
                knock_sequence = []
                while True:
                    for i, s in enumerate(sockets):
                        s.listen()
                        conn, addr = s.accept()
                        print('Knock depuis:', addr)
                        knock_sequence.append(PORTS[i])
                        if knock_sequence == PORTS:
                    #nettoyer les règles déja éxistantes dans l'iptables
                    #[EMPLACEMENT]
                    #Créer une variable "s" qui convertira "addr" en str pour extraire l'ip source et l'utilisé dans la règle.
                            s = clientAddress[0]
                            print(f"ClientAddress: {clientAddress}")
                    #s = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s).group+()
                            #now = datetime.datetime.now()
                            print('sequence ok!')
                            log_nonformat = 'Connection from {} with previous TOTP {}/{} a {}:{}:{}'.format((s),(now.day),(now.month),(now.hour),(now.minute),(now.second))
                            log_format = str(log_nonformat)
                            with open('logax.txt', 'a') as f:
                                f.write(log_format + '\n')
                    #ajouter li [INTERFACE] , si mauvaise par défault
                            subprocess.run(['netsh', 'advfirewall', 'fireewall', 'add', 'rule', '{}', 'name=SSH', 'dir=in', 'action=allow', 'protocol=TCP', 'localport=22'.format(s)])
                            print('Ouverture du port pour {} '.format(s))
                            time.sleep(3)
                    #ajoute li [INTERFACE] , si mauvaise par défault
                            subprocess.run(['netsh', 'advfirewall', 'firewall', '***', 'rule', '{}', 'name=SSH', 'dir=in', 'action=allow', 'protocol=TCP', 'localport=22'.format(s)])
                            print('Fermeture du port pour {}'.format(s))
                            knock_sequence = []
                            sleep(5)
                            print("purge socket")
                            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                            serverSocket.close()
                            conn.close()
                            #s.close()
                            #os.execv(sys.executable, ['python'] + sys.argv)
                            s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            serverSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            os.execl(sys.executable, sys.executable, *sys.argv)
            else : print("else")
