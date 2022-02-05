import requests
import json
from datetime import datetime

i = int(datetime.now().strftime('%d'))
j = int(datetime.now().strftime('%m'))
k = int(datetime.now().strftime('%Y'))
h = i-10
b = 0
c = []
d = []
g = []
m = []

while h != i+1:
    a = requests.get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(k,j,str(h))).text
    json_data = json.loads(a)
    for x in json_data:
        try:
            if x['ip'] in ['127.0.0.1','172.18.0.1']:
                m.append(x['addr'])
            else:
                if json_data[b]['type'] == 1:
                    c.append(json_data[b]['addr'])
                elif json_data[b]['type'] == 2:
                    d.append(json_data[b]['addr'])
                elif json_data[b]['type'] == 4:
                    g.append(json_data[b]['addr'])
                else:
                    print('garbage value')
                b = b + 1
        except:
            pass
    h = h + 1
    b = 0

c = list(dict.fromkeys(c))
d = list(dict.fromkeys(d))
g = list(dict.fromkeys(g))

for x in m:
    try:
        c.remove(x)
    except:
        pass
    try:
        d.remove(x)
    except:
        pass
    try:
        g.remove(x)
    except:
        pass

with open('http.txt','w') as f:
    for x in c:
        f.write(x+'\n')

with open('https.txt','w') as f:
    for x in d:
        f.write(x+'\n')

with open('socks5.txt','w') as f:
    for x in g:
        f.write(x+'\n')
