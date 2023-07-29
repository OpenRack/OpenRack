import yaml

with open('config.yml','r+') as file:
    config = yaml.safe_load(file)
    
def addfolder():
        folder = "C:/Test"
        folders = list(yaml.load(['folders:'][0]))
        folders.append(folder)        
        yaml.dump(config.yml, file)

testdir = ['C:/testdir1','C:/testdir2']


addfolder()
#print(yaml.dump(folders,sort_keys=False))


