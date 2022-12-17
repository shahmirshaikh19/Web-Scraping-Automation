import logging
import Logging.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('Debug Message!!')
        self.log.info('Info message!!')
        self.log.warning('It is a warning!!')
        self.log.error('There is an error!!')
        self.log.critical('Things went critical here!!')

    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug('Debug Message!!')
        m2log.info('Info message!!')
        m2log.warning('It is a warning!!')
        m2log.error('There is an error!!')
        m2log.critical('Things went critical here!!')

    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.debug('Debug Message!!')
        m3log.info('Info message!!')
        m3log.warning('It is a warning!!')
        m3log.error('There is an error!!')
        m3log.critical('Things went critical here!!')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()