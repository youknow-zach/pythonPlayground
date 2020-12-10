from appscript import *

psApp = app('/Applications/Adobe Photoshop 2020/Adobe Photoshop 2020.app')
path = '/Users/ZachGuest/Desktop/'
fname = path + 'creep.psd'

psApp.open(mactypes.Alias(fname))
