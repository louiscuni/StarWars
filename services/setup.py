from setuptools import setup

setup(
    name= 'give-me-the-odds', 
    version= '0.1',
    packages= ['src', 'src.controller', 'src.database', 'src.ressource', 'src.default_file'],
    include_package_data= True,
    entry_points = {
        'console_scripts' : [
            'give-me-the-odds = src.__main__:main'
            ]
    })