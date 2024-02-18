-! Due to recent changes in the Python programming language, particularly in the newer versions, certain libraries, including Telnet and others, are no longer compatible with our current script. As a result, the existing version of the script won't work. An update is comming soon. !-

# Knoot
![Pingu+Noot+white+edge](https://github.com/Wisp404/Knoot/assets/107390816/735d82b4-8747-4b19-8da7-485968bee244)


Knoot is a Port Knocking python script including TOTP, all-in-one (server and client) with no dependencies to install.

Port knocking is a technique used in computer networking to enhance the security of a system by opening ports on a firewall in response to a specific sequence of connection attempts.

The first sequence consists of a TOTP key exchange between the Client and the Server. 

If the code is correct, the Server listens on the three ports generated from the secret keys you've determined. 
The TOTP implementation allows the server to change its listening ports every 30 seconds. 

Once the client has Knocked on all three ports, the firewall rule sequence you've defined runs to open a port for the client's IP address.

Knoot is compatible with Linux & Windows.

Before running the script, you must :
- Modify all secret keys so that they are unique to you.
- Define firewall rules in the script to match your server's configuration.
- Add the secret key for the first exchange with the server to your Google Auth or other application.
  
