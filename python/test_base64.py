import base64
import sys

if __name__ == '__main__':
    argvs = sys.argv
    code = argvs[1]
    print base64.b64decode(code)
