from distutils.core import setup

import linguo


setup(
    name='django-bilinguo',
    packages=['linguo', 'linguo.tests'],
    package_data={'linguo': ['tests/locale/*/LC_MESSAGES/*']},
    version=linguo.__version__,
    description=linguo.__doc__,
    long_description=open('README.rst').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    author='Zach Mathew, Tintu Jacob',
    url='https://github.com/tintujacob/django-linguo',
    license='BSD',
)
