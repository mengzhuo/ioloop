#!/usr/bin/env python
# encoding: utf-8

import socket
from ioloop import IOLoop, READ, ERROR, WRITE

main_sock_fd = None
loop = IOLoop()


socks = {}
buff = ''

def handle_read(fd, events):
    global buff
    sock = socks[int(fd)]
    data = sock.recv(10)
    print 'Recv:%s' %  data
    sock.send('pikachu\n')
    buff += data

def handle_write(fd, events):
    global buff
    sock = socks[int(fd)]
    sock.send(buff)
    buff = ''

def handle_events(fd, events):

    if fd == main_sock_fd:
        # new connection
        print 'new connection'
        conn, _  = socket.fromfd(fd,
                             socket.AF_INET,
                             socket.SOCK_STREAM).accept()
        socks[conn.fileno()] = conn
        print socks
        conn.setblocking(0)
        loop.add_handler(conn.fileno(), READ|ERROR, handle_events)

    else:
        print "new request %s" % bin(events)
        if events & ERROR:
            raise ValueError('Error on fd:%d' % fd)
        if events & READ:
            handle_read(fd, events)
        if events & WRITE:
            handle_write(fd, events)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ss.setblocking(0)
ss.bind(('0.0.0.0', 12000))
ss.listen(512)
main_sock_fd  = ss.fileno()
print 'main sock fd:%d' % main_sock_fd
loop.add_handler(ss.fileno(), READ, handle_events)
loop.start()
