#!/usr/bin/env python
1;95;0c
from distutils.core import setup

setup(name='hgedb',
      version='1.0.0',
      description='AS5 HGE database',
      author='David Nidever',
      author_email='dnidever@montana.edu',
      url='https://github.com/dnidever/hgedb',
      packages=['hgedb'],
      package_dir={'':'python'},
      #package_data={'hgedb': ['data/*','data/params/*','data/params/*/*']},
      #scripts=['bin/ukidssjobs','bin/ukidssjob_manager','bin/ukidss_launcher','bin/ukidss_download',
      #         'bin/ukidss_measure','bin/ukidss_calibrate',
      #         'bin/ukidss_calibrate_healpix','bin/ukidss_combine'],
      #py_modules=['nsc_instcal',''],
      requires=['numpy','astropy','scipy','requests'],
      #include_package_data=True
)
