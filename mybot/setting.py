import configparser


conf = configparser.ConfigParser()
conf.read("setting.ini")

url = str(conf["base"]["url"])
driver_path = str(conf["base"]["driver_path"])
username = str(conf["base"]["username"])
password = str(conf["base"]["password"])

login_button = conf["path"]["login_path"]
later_button = conf["path"]["later_path"]
off_button = conf["path"]["off_path"]

tag_box = conf["path"]["tag_box"]
tag = conf["path"]["tag"]
target = conf["path"]["target"]
post = conf["path"]["post"]
good = conf["path"]["good"]
next = conf["path"]["next"]