import ConfigParser

class Config():

  def __init__(self, file):
    self.parser = ConfigParser.ConfigParser()
    self.parser.read(file)

  def section(self, section):
    options = self.parser.options(section)
    dict1 = {}
    for option in options:
        try:
            dict1[option] = self.parser.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1