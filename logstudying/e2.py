import logging
logging.basicConfig(filename='elog', level=logging.INFO, \
                    format='%(asctime)s+++%(levelname)s***%(message)s')

logging.debug('debug log')
logging.info('info log')