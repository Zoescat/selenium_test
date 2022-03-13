
from distutils.log import error
import logging

err=logging.log(3,'创建一条严重级别为error的日志')
print(err)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')