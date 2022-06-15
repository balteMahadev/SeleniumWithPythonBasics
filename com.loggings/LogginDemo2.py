import os
import logging

logging.basicConfig(filename=os.getcwd()+os.sep+"SeleniumLogs"+os.sep+"test1.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',datefmt="%m-%d-%Y %H:%M:%S",)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")