from setuptools import setup, find_packages

setup(
    name='LclSymbolicLinking',
    version='0.0.1',
    description='LCL C-ymbolic (C - symbolic) Link-ing (link introduce linking)',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/LCL',
    packages=find_packages(exclude=[]),
    install_requires=['PyPInclude'],
    keywords=['python', 'PyPI', 'PyPInclude', "LCL", "lcl", "Cymbolic", "C", "c", "CPP", "cpp", "symbolic", "link", "linking", "introduce"],
    python_requires='>=3.6',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)