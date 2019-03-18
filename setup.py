from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.10',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python packages',
    long_description=open('README.md').read(),
    install_requirements=['numpy'],
    url='https://github.com/Muzix1/mypackage',
    author='Muzi',
    author_email='muzixaba@gmail.com'
)