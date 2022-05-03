import socket
import requests


ip_local = socket.gethostbyname(socket.gethostname())
print('IP local: {}'.format(ip_local))

ip_publico = requests.get('https://api.ipify.org/').text
print('IP publico: {}'.format(ip_publico))
