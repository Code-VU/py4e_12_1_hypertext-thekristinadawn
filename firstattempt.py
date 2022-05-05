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
        #print(decode_data) #it is printing everything it should
    

         #pos = decode_data.find("\r\n\r\n") #find header [-1]
        #print(pos)
        def SplitLines():
            data = decode_data.splitlines() #this separates the data from the headers
            print(data)  #not sure if this is accurate, I've tried multiple ways of splitting and it still splits at "for"

        #for line in data: 
            #if line startswith:
                #break
        #else: 
            #header_lists.append(line) #or append?
            #print(header_lists)

    
     #for key,value in header_dictionary.items(): 
       #print(key,value)
    mysock.close()
    SplitLines()
getWebData()
