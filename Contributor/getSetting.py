import configparser

config = configparser.ConfigParser()
config.read("settings.txt")

# Get the values of the variables in setting.txt
repLoc = config.get("Required", "repLoc")
txtLoc = config.get("Required", "txtLoc")
min = config.getint("DEFAULT", "min")
max = config.getint("DEFAULT", "max")
tries = config.getint("DEFAULT", "tries")
minutes = config.getint("DEFAULT", "minutes")
