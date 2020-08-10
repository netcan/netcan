import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://netcan.github.io/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
```
_   _      _
| \ | | ___| |_ ___ __ _ _ __
|  \| |/ _ \ __/ __/ _` | '_ \
| |\  |  __/ || (_| (_| | | | |
|_| \_|\___|\__\___\__,_|_| |_|
```

## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('\n[➡️ More blog posts](https://netcan.github.io/archives/)\n\n---\n')
    f.write('![Stats](https://github-readme-stats.vercel.app/api?username=netcan)\n')
    f.write('![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=netcan&hide=ipynb,html&layout=compact)\n')
