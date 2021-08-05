from setuptools import setup

from setuptools import setup



setup(name='ONUR_Voice_Assistant',
version='0.1.0',
description="""A modular and expandable voice assistant""",
long_description="""
# ONUR Voice Assistant | [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/onuratakan/ONUR_Voice_Assistant)](https://github.com/onuratakan/ONUR_Voice_Assistant/blob/master/LICENSE)
A modular and expandable voice assistant.
# Install
```
pip3 install ONUR_Voice_Assistant
```
# Using
## In another script
```python
from ONUR_Voice_Assistant import ONUR

ONUR.run()
```
## In command line
```console
ONUR
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
    "say-me-something==0.1.1",
    "ask-me-something==0.1.1",
    "selenium==3.141.0",
    "SpeechRecognition==3.8.1",
],
entry_points = {
    'console_scripts': ['ONUR=ONUR_Voice_Assistant.ONUR_Voice_Assistant:ONUR_Voice_Assistant'],
},
python_requires=">= 3, < 3.7",
zip_safe=False)