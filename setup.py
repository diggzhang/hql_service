import os
import subprocess
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_git_sha():
    try:
        s = str(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
        return s.strip()
    except:
        return ""


GIT_SHA = get_git_sha()
print("-==-" * 15)
print("Version: " + GIT_SHA)
print("-==-" * 15)

setup(
    name='hql_service',
    description=(
        "A interactive hql command query visualization platform"),
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.12.2',
        'Flask-RESTful==0.3.6',
        'PyHive==0.5.0',
        'requests==2.18.4',
        'thrift==0.10.0',
        'thrift-sasl==0.3.0',
    ],
    url='https://github.com/diggzhang/hql_service',
    author='diggzhang',
    author_email='diggzhang@gmail.com',
)