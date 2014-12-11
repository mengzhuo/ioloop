#!/usr/bin/env python
# encoding: utf-8

import threading
import select

_EPOLLIN = 0x001
_EPOLLOUT = 0x004
_EPOLLERR = 0x008
_EPOLLHUP = 0x010

# Our events map exactly to the epoll events
NONE = 0
READ = _EPOLLIN
WRITE = _EPOLLOUT
ERROR = _EPOLLERR | _EPOLLHUP


class IOLoop(object):

    
    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        """Returns a global `IOLoop` instance.

        Most applications have a single, global `IOLoop` running on the
        main thread.  Use this method to get this instance from
        another thread.  To get the current thread's `IOLoop`, use `current()`.
        """
        if not hasattr(IOLoop, "_instance"):
            with IOLoop._instance_lock:
                if not hasattr(IOLoop, "_instance"):
                    # New instance after double check
                    IOLoop._instance = IOLoop()
        return IOLoop._instance   

    
    def __init__(self, impletement=None):
       
        if impletement:
            self._impl = impletement
        elif hasattr(select, 'kqueue'):
            from ioloop.platform.kqueue import KQueueLoop
            self._impl = KQueueLoop
        elif hasattr(select, 'epoll'):
            from ioloop.platform.epoll import EPollLoop
            self._impl = EPollLoop
        else:
            raise NotImplemented()
        
        self._impl()
