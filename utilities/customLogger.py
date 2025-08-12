import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
