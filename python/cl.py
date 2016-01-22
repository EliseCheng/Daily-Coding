class Foo(object):
    t = 1
    @staticmethod
    def test(val):
        Foo.t = val
        print Foo.t

