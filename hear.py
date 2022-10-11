import socket,struct,json,time
addr=(input('server_addr:'),int(input('port:')))
s=socket.socket()
s.connect(addr)
cmd=['new']
cmd=json.dumps(cmd)
s.send(struct.pack('L',len(cmd.encode())))
s.send(cmd.encode())
size=struct.unpack('L',s.recv(4))[0]
messages=json.loads(s.recv(size).decode())
for i in messages:
    print(i[0],':',i[1])
#print(messages)
cmd=['get',messages[-1][0],messages[-1][1],messages[-1][2]]
while True:
    s=socket.socket()
    s.connect(addr)
    #cmd=['get','Bob','sagaesgrfv',1665447617.158555]
    cmd=json.dumps(cmd)
    s.send(struct.pack('L',len(cmd.encode())))
    s.send(cmd.encode())
    size=struct.unpack('L',s.recv(4))[0]
    messages=json.loads(s.recv(size).decode())
    cmd=['get',messages[-1][0],messages[-1][1],messages[-1][2]]
    del messages[0]
    for i in messages:
        print(i[0],':\n',i[1])
    if len(messages)>=1:
        cmd=['get',messages[-1][0],messages[-1][1],messages[-1][2]]
    time.sleep(0.5)
    #cmd=[]
