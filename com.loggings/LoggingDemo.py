import os
import logging

logging.basicConfig(filename=os.getcwd()+os.sep+"SeleniumLogs"+os.sep+"test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',datefmt="%m-%d-%Y %H:%M:%S",
                    level=logging.DEBUG,
                    )
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")