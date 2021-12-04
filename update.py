import re
import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://netcan.github.io/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
```
 _   _      _                                                                                      _
| \ | | ___| |_ ___ __ _ _ __     ___  _ __    _ __  _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___ (_)_ __   __ _
|  \| |/ _ \ __/ __/ _` | '_ \   / _ \| '_ \  | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
| |\  |  __/ || (_| (_| | | | | | (_) | | | | | |_) | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
|_| \_|\___|\__\___\__,_|_| |_|  \___/|_| |_| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
                                              |_|              |___/                                       |___/
* 1996, Summer, Senior Software Engineer
* Skills: C/C++/Rust, Haskell/Scheme, Bash/Python/Javascript/PHP
* Interests: CS, OO/FP, Design/Coding/Writing
```
''')

    f.write(r'''
## Latest talks
''')
    talks = requests.get('https://raw.githubusercontent.com/netcan/presentation/master/README.md').text
    for (topic, url) in re.findall('- (.*): (.*)', talks)[:5]:
        f.write('- [{}]({})\n'.format(topic, url))

    f.write(r'''
## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://netcan.github.io/archives/)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=netcan)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=netcan&hide=ipynb,html&layout=compact)
''')
