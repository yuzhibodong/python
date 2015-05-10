from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(),i
        gevent.sleep(0)

g1 = gevent.spawn(f,500000)
g2 = gevent.spawn(f,500000)
g3 = gevent.spawn(f,500000)
g1.join()
g2.join()
g3.join()
