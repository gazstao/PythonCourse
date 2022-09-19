import qrcode
import re
import string

data = "https://aztechtecnologia.com.br/gazstao/"

img = qrcode.make(data)
img.save('qrcode-{}.png'.format(re.sub('[%s]' % re.escape(string.punctuation), '-', data)))