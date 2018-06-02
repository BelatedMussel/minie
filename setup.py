from setuptools import setup

setup(name='minie',
      version='0.1',
      description='A simple HTML text editor',
      url='https://github.com/BelatedMussel',
      author='Joshua Kurtenbach',
      author_email='',
      license='GPLv3',
      packages=['minie'],
      install_requires=[
          'SidePy',
          'sys',
          'ext',
          ]
      )
