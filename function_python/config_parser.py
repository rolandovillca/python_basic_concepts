import ConfigParser

config = ConfigParser.ConfigParser()
print config
print

print config.read('config_parser.ini')

print config.sections()
