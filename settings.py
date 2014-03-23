import json

config = None

def loadConfig(filename):
	""" Load and return config file from json """
	global config
	with open(filename, 'rb') as configfile:
		config = json.load(configfile)

	return config


def main():
	global config

	loadConfig('config.json')
	if config is not None:
		print config

if __name__ == u'__main__':
	main()
