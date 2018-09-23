import sys
import time
from os import path
from os import system
from configparser import ConfigParser
import dlwp

if len(sys.argv) > 1:
        cff = sys.argv[1]
else:
        cff = './config'

cf = ConfigParser()
cfr = ConfigParser()

cf['source'] = {
        'url': 'https://stodulky.navyrovne.cz/imgs/snap.jpeg',
        'filetype': 'jpg'
}
cf['local'] = {
        'refreshtime': '60',
        'tempdir': './',
        'syntax': 'gsettings set org.gnome.desktop.background picture-uri file://'
}

try:
        if path.isfile(cff):
                cfr.read(cff)
        else:
                with open(cff, 'w') as f:
                        cf.write(f)
                cfr.read(cff)
except:
        print('Cannot access specified config file')
        sys.exit()

while True:
        dlpath = dlwp.get(cfr['source']['url'],cfr['local']['tempdir'],"temp",cfr['source']['filetype'])
        try:
                system(cfr['local']['syntax'] + path.realpath(dlpath))
                time.sleep(int(cfr['local']['refreshtime']))
        except:
                print('Unable to set the wallpaper')
                sys.exit()