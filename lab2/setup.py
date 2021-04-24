from setuptools import find_packages, setup


setup(
name="LAB2",
version="1.0",
packages=find_packages(include=['modules','modules.*']),
entry_points={
'console_scripts': [
'parser=modules.MySerializer:main',
],
},
install_requires=[
'coverage==5.5',
'entrypoints==0.3',
'py==1.10.0',
'pytest==6.2.3',
'pytest-cov==2.11.1',
'python-apt==3.0.0+ubuntu0.20.4.4',
'PyYAML==5.4.1',
'simplejson==3.16.0',
'toml==0.10.2',
'virtualenv==20.0.17',
]
)
