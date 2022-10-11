import socket,struct,json,time
name=input('昵称:')
addr=(input('server_addr:'),int(input('port:')))
while True:
    message=input('>>')
    s=socket.socket()
    s.connect(addr)
    cmd=['send',name,message,time.time()]
    cmd=json.dumps(cmd)
    s.send(struct.pack('L',len(cmd.encode())))
    s.send(cmd.encode())
