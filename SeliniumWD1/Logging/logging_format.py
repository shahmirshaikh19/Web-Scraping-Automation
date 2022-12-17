import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p' ,level=logging.DEBUG)

logging.warning("its a warning!!")
logging.info("here goes some info")
logging.error("its an error msg!!")

