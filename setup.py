from setuptools import setup, find_packages
import codecs

version = __import__('background_task').__version__

classifiers = [c for c in open('classifiers').read().splitlines() if '#' not in c]

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='django-background-tasks-async-update',
    version=version,
    description='Database backed asynchronous task queue',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='arteria GmbH, John Montgomery, Alberto Petrucci, Jon Miller',
    author_email='iamjonamiller@gmail.com',
    url='https://github.com/django-background-tasks/django-background-tasks',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    zip_safe=True,
    classifiers=classifiers,
)
