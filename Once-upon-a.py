import os
import subprocess

# 
os.system('sudo apt install apt-transport-https')


# file = open('tor.list',mode='x')
# file.write('deb [arch=amd64 signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org focal main\ndeb-src [arch=amd64 signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org focal main')

subprocess.run(['wget', '-O-','https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc', '| gpg --dearmor', '|', 'tee /usr/share/keyrings/tor-archive-keyring.gpg', '>/dev/null'])




subprocess.run(['cd', '/etc/apt/sources.list.d/', '&&', 'touch tor.list'] )
