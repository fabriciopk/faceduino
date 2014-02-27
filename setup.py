from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="Faceduino",
    version="0.0.1",
    description="Python Framework for interation between facebook and arduino ",
    author="Fabricio",
    author_email="fabricio-bit@hotmail.com",
    packages=find_packages(),
    install_requires=['pyserial'],
    url="http://github.com/fabriciopk/faceduino",
    keywords=["arduino", "facebook"],
    long_description=readme()
)
