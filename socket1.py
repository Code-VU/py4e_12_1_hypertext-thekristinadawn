from base64 import decode
import socket

def getWebData():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    header_lists = list()
    header_dictionary = dict()
       
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        decode_data = data.decode()
        #mysock.close()

    def splitLines(): 
        data = decode_data.replace("\r",' ')
        data = data.splitlines()
        #return data

    for line in data: 
        if line == ' ': 
            break
        else: 
            header_lists.append(line)
    for item in header_lists: 
        item = item.split(": ")
        header_dictionary[item[0]] = item[1]
    
    for key,value in header_dictionary.items(): 
        print(key,value)

    splitLines()
getWebData()
