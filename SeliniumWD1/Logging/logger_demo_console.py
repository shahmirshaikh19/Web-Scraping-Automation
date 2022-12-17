import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s: - %(name)s - %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.debug('Debug Message!!')
        logger.info('Info message!!')
        logger.warning('It is a warning!!')
        logger.error('There is an error!!')
        logger.critical('Things went critical here!!')

ff = LoggerDemoConsole()
ff.testLog()