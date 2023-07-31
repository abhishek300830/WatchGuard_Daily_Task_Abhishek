import logging

'''
CRITICAL
ERROR
Warning
INFO
DEBUG
'''
# to set logging show level by default set to warning and above.
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    filename="July-31-2023\\09-logs.txt"
                    )


logger = logging.getLogger("test_logger")

logger.info("This will not show up")
logger.warning("This is warning")