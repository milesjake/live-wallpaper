import sys
from os import path
from os import remove
from PIL import Image
import requests

def get(url, folder, filename, filetype):
    if filetype != ('jpg' or 'png'):
        print('Unknown filetype, use JPG or PNG')
        sys.exit()
    
    try:
        if not path.isdir(folder):
                mkdir(folder)
    except:
        print('Cannot access specified folder')
        sys.exit()

    if folder.endswith('/'):
        f = folder
    else:
        f = folder + '/'
    try:
        if path.isfile(f + filename + '.' + filetype):
            remove(f + filename + '.' + filetype)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(f + filename + '.' + filetype, "wb") as imgfile:
                for chunk in r.iter_content(1024):
                    imgfile.write(chunk)
        else:
            print('Cannot download the file')
            sys.exit()
    except:
        print('Cannot download the file')
        sys.exit()

    if filetype == 'png':
        try:
            if path.isfile(f + filename + '.jpg'):
                remove(f + filename + '.jpg')
            img = Image.open(f + filename + '.' + filetype)
            img.save(f + filename + '.jpg')
        except:
            print("Unable to convert file")
            sys.exit()
    return f + filename + '.jpg'