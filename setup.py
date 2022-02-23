from setuptools import setup

from setuptools import setup



setup(name='ONUR_Voice_Assistant',
version='0.1.8',
description="""A modular and expandable voice assistant""",
long_description="""
# ONUR Voice Assistant | [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/onuratakan/ONUR_Voice_Assistant)](https://github.com/onuratakan/ONUR_Voice_Assistant/blob/master/LICENSE)
A modular and expandable voice assistant.
# Install
```
pip install ONUR-Voice-Assistant
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
url='https://github.com/onuratakan/ONUR_Voice_Assistant',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["ONUR_Voice_Assistant", "ONUR_Data"],
package_dir={'':'src'},
install_requires=[
    "Linear-Congruential-Generator==0.1.5",
    "flask==2.0.0",
    "waitress==2.0.0",
    "get-crypto-price==0.2.2",
],
entry_points = {
    'console_scripts': ['onur_api=ONUR_Voice_Assistant.ONUR_Voice_Assistant:ONUR.run_api'],
},
python_requires=">= 3",
zip_safe=False)
