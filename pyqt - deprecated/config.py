from configparser import ConfigParser


config_object = ConfigParser()

config_object["databaseconfig"] = {
    "dblocation": "",
    "dbname": "openrack",
}

config_object["libraryconfig"] = {
    "librarypath": ""
}

config_object["userconfig"] = {
    
}

config_object["firstrun"] = {
    "firstrun" : "true"
}

with open('openrack.ini', 'w') as conf:
    config_object.write(conf)