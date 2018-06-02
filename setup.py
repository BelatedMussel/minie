from setuptools import setup, find_packages

setup(name='minie',
      version='0.1',
      description='A simple HTML text editor',
      url='https://github.com/BelatedMussel/minie',
      author='Joshua Kurtenbach',
      author_email='38633896+BelatedMussel@users.noreply.github.com',
      license='GPLv3',
      packages=find_packages(),
      install_requires=[
          'PySide',
          ]
      )
