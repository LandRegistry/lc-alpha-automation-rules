

class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    AUTOMATION_IND = True


class PreviewConfig(Config):
    AUTOMATION_IND = True
