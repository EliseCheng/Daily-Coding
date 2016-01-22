class Test(object):
    ip = '0.0.0.0'
    port = 0
    #def __init__(self, ip, port):
    #    self.ip = ip
    #   self.port = port

    @staticmethod
    def printself():
        print Test.ip
        print Test.port

if __name__ == "__main__":
    print "--------main---------"
    test = Test()
    Test.ip = '10.0.0.0'
    Test.port = 9000
    test.printself()
