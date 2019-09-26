import configparser


conf = configparser.ConfigParser()
file_path = "conf_test"
read_ok = conf.read(file_path)
if not read_ok:
    print("read fail")

sections = conf.sections()
print(sections)

options = conf.options('tcp')
print(options)

items = conf.items('tcp')
print(items)

value = conf.get('tcp', 'ip')
print(value)
