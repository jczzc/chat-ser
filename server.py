import socket,struct,json
import multiprocessing
class handler:
    def __init__(self,address,port):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.TCP_NODELAY=False
        self.s.bind((address,port))
        self.s.listen(200)
        try:
            with open('log.json','w') as f:
                self.lis=json.load(f)
        except:
            self.lis=[['system','hello',0],]
    def message_recv(self):
        while True:
            c,addr=self.s.accept()
            print(addr)
            lenth=struct.unpack('L',c.recv(4))[0]
            cmd=c.recv(lenth)
            cmd=json.loads(cmd)
            #print(addr,':',cmd[0])
            if cmd[0]=='send':
                print(addr,':',cmd[0])
                print(addr[0],':',cmd[1],':',cmd[2],':',cmd[3])
                self.lis.append([cmd[1],cmd[2],cmd[3]])
                with open('log.json','w') as f:
                    json.dump(self.lis,f)
            elif cmd[0]=='get':
                index=self.lis.index([cmd[1],cmd[2],cmd[3]])
                messages=self.lis[index:]
                package=json.dumps(messages).encode()
                lenth=struct.pack('L',len(package))
                c.send(lenth)
                c.send(package)
            elif cmd[0]=='new':
                print(addr,':',cmd[0])
                messages=[self.lis[0],self.lis[-1]]
                package=json.dumps(messages).encode()
                lenth=struct.pack('L',len(package))
                c.send(lenth)
                c.send(package)
            c.close()
hand=handler('127.0.0.1',1024)
while True:
    try:
        hand.message_recv()
    except Exception as e:
        print(e)
