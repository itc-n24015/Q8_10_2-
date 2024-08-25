import logging

def devide(x1, x2):
    return x1 / x2

logging.basicConfig(filame='testlog.log',level=logging.WARNIG,format='%(levelname)s:%(astctime)s:%(message)s')

try:
    ret = devide(10,0)
except:
    logging.exception('test exception message')
logging.shutdown()


