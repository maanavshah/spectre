import os

from setuptools import setup

version = __import__('review').get_version()

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name = 'spectre',
    version = version,
    packages = ['review'],
    include_package_data = True,
    install_requires = [line for line in read('requirements.txt').split('\n')
                        if line and not line.startswith('#')],
    license = 'MIT License',
    description = 'An easy way to start writing blog posts.',
    long_description = readme,
    url = 'https://github.com/maanavshah/spectre',
    author = 'Maanav Shah',
    author_email = 'shah.maanav.07@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
