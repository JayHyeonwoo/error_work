import time
import _thread
import os
import sys

class service_test:
    def __init__(self):
        _thread.start_new(self.do_exe, tuple())
        while True:
            if getattr(sys, 'stopservice', False):
                sys.exit()
                time.sleep(0.3)



    def do_exe(self):
        while(1):
            fname = "C:\\Users\\SKTelecom\\Desktop\\test.txt"
            f = open(fname, 'a')
            f.write('test ok\n')
            f.close()
            time.sleep(1)

if __name__ == "__main__":
    tst = service_test()