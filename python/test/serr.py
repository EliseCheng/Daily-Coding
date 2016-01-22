from socket import error as serr
def foo():
    try:
        raise serr(113, 'noroute to host')
    except IOError, e:
        print "error 113"

foo()
