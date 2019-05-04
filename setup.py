from setuptools import setup

setup(name='factortable',
      version='0.1',
      description='Print a factortable on screen',
      url='https://github.com/rmonico/factortable',
      author='Rafael Monico',
      author_email='rmonico1@gmail.com',
      license='GPL3',
      packages=['factortable'],
      entry_points = {
          'console_scripts': ['factortable=factortable.factortable:main'],
      },
      zip_safe=False)