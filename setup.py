from setuptools import setup

from setuptools import setup



setup(name='ONUR_Voice_Assistant',
version='0.1.0',
description="""""",
long_description="""
# Say Me Something
A text to speak library with embedded cache system.
# Install
```
pip3 install say-me-something
```
# Using
## In another script
```python
from say_me_something import say

# say(text = None, language = "en", no_cache = False, reset = False, no_speak = False)

say("Hello")
```
## In command line
```console
  -h, --help            show this help message and exit
  -t TEXT [TEXT ...], --text TEXT [TEXT ...]
                        Text
  -l LANGUAGE, --language LANGUAGE
                        Language
  -nc, --nocache        No cache
  -r, --reset           Reset (removing the caches)
  -ns, --nospeak        No speak
```

```console
say -t Hello
```
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/say_me_something',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["ONUR_Voice_Assistant"],
package_dir={'':'src'},
install_requires=[
    "say-me-something==0.1.0"
],
entry_points = {
    'console_scripts': ['onur=ONUR_Voice_Assistant.ONUR_Voice_Assistant:ONUR_Voice_Assistant'],
},
python_requires='>=3',
zip_safe=False)
