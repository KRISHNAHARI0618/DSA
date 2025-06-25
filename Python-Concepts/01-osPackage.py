import datetime
import os
from datetime import datetime

# print(dir(os))

print(os.getcwd())
print(os.listdir())

mod_time = os.stat('osPackage.py').st_mtime

print(datetime.fromtimestamp(mod_time))

 
import logging
import mylib # type: ignore

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="Arrays.py",level=logging.INFO)
    logger.info('started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()




    


