from base64 import decode
import socket

def getWebData():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
       
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        decode_data = data.decode()
    
    header_lists = list()
    header_dictionary = dict()

    def splitLines(): 
        data = decode_data.replace("\r",' ')
        data = decode_data.splitlines()
        #return data

        for line in data: 
            if line == ' ': 
                break
            else: 
                header_lists.append(line)
        for item in header_lists: 
            item = item.split()
        print(item)
    
        for key,value in header_dictionary.items(): 
            print(key,value)

    mysock.close()
    splitLines()
getWebData()
