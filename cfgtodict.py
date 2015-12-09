import configparser

class ConfigToDictionary:

  def __init__(self, config):
    self.config = config

  def dict(self):
    # Parse config file
    parser = configparser.ConfigParser()
    parser.read(self.config)

    # Set config values on Dictionary
    dict = {}
    
    for section in parser.sections():
      dict[section] = {}
      for option in parser.options(section):
        dict[section][option] = parser.get(section, option)

    return dict
