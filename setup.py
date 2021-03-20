import setuptools


install_requires = [
    'pyserial==3.5',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name = 'HC_SR04',
    version = '0.0.2',
    license = 'GPL-3.0 License',
    description = 'HC-SR04 Python module via Serial protocol',
    author = 'KKimj',
    author_email = 'kkimj@hanyang.ac.kr',
    url = 'https://github.com/KKimj/HC-SR04_Python-library',

    install_requires=install_requires,
    #packages = setuptools.find_packages(),
    packages_dir = {'src' : 'HC_SR04'},
    packages = ['src'],
    classifiers = [
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Terminals :: Serial",
        "Natural Language :: Korean",
    ],
    python_requires='>=3',
)
