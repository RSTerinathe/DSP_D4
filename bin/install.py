import os
# This 'install' script initializes the config files that are not pushed to github

# If the config folder does not exist yet, create it and add the config file with placeholders
relative_config_path = '../config'
if not (os.path.exists(relative_config_path)):
    os.mkdir(relative_config_path)
    config = open(relative_config_path + '/config.ini', 'w')
    config.write("""[HERE_MAPS_KEY]
api_key = placeholder""")
    config.close()
