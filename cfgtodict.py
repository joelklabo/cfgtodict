import configparser, re

class ConfigToDictionary:

  def __init__(self, config):
    self.config = config

  def dict(self):
    # Parse config file
    parser = configparser.RawConfigParser(allow_no_value=True)
    parser.optionxform=str
    parser.read(self.config)

    # Set config values on Dictionary
    dict = {}
    
    for section in parser.sections():
      dict[section] = {}
      for option in parser.options(section):
      	value = parser[section][option]
      		if re.match(r'^[1-9]\d*$', value): # types: int
      			dict[section][option] = parser.getint(section, option)
      		elif re.match(r'^[+-]?([0-9]*[.])?[0-9]+', value): # types: float
      			dict[section][option] = parser.getfloat(section, option)
      		elif re.match(r'[True|False|None]', value): # types: bool
      			dict[section][option] = parser.getboolean(section, option)
      		else: # types: string
      			dict[section][option] = parser.get(section, option)
      	except Exception as e:
      		print(f'Issue with value of "{option}" -> ', e)
      		# dict[section][option] = parser.get(section, option)
    return dict
