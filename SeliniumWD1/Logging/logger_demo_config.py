import logging
import logging.config

class LoggerDemoConfig():

    def testLog(self):

        # create logger
        logging.config.fileConfig('logging.conf')
        logger =  logging.getLogger(LoggerDemoConfig.__name__)

        # logging messages
        logger.debug('Debug Message!!')
        logger.info('Info message!!')
        logger.warning('It is a warning!!')
        logger.error('There is an error!!')
        logger.critical('Things went critical here!!')

demo = LoggerDemoConfig()
demo.testLog()