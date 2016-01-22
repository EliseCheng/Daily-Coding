a=0
def fun():
    if 0 < 5 and \
                   ('' == '<urlopen error [Errno 104] Connection reset by peer>' or '' == ''):
        print "**"
    global a
    print a
    a = a+1
    print a
#fun()

def foo(d, **kwargs):
    for key, value in kwargs.iteritems():
        d[key] = value
    return d

test = {}
print foo(test, a='f', b='3')


