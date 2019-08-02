import logging

logging.basicConfig()

logging.debug('this is a debug log')
logging.info('this is a info log')


logging.log(logging.WARNING, 'this is a warning log')
logging.log(logging.ERROR, 'this is a error log')

# 这里只显示了两条日志,是因为默认的等级为warning,而debug和info未达到级别,故不显示