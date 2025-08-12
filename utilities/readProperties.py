import configparser

config=configparser.RawConfigParser()
config.read('.\\config\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password