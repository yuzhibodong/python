# -*- coding:utf-8 -*-
import os

print 'Process %s ' % os.getpid()

pid = os.fork()

if pid == 0:
    print 'I am child process %s and my parent is %s' % (os.getpid(), os.getppid())

else:
    print 'I %s just create a child process %s' % (os.getpid(), pid)
