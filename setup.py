"""
Flask-VBL
-------------

A Flask plugin to allow authentication against VBL
"""
from setuptools import setup


setup(
    name='Flask-VBL',
    version='0.1.0',
    url='https://github.com/artificialexit/flask-VBL',
    license='Modified BSD',
    author='Nathan Mudie',
    author_email='nathan.mudie@synchrotron.org.au',
    description='A Flask plugin to allow authentication against VBL',
    long_description=__doc__,
    py_modules=['flask_vbl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Modified BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)