try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'pandas>=1',
    'plotly',
    'lxml',
    'matplotlib',
    'pandoc',
    'plotly',
    'plotly_express',
    'dash',
    'pyqt',
    'scipy',
    'setuptools',
    'sqlite',
    'statsmodels',
    'flask',
    'pyteomics',
    'openpyxl',
    'colorlover',
    'dash-bootstrap-components'
]

config = {
    'name': 'ms-mint',
    'version': '0.0.26',
    'description': 'Metabolomics Integrator (Mint)',
    'long_description': long_description,
    'author': 'Soren Wacker',
    'url': 'https://github.com/soerendip/ms-mint',
    'author_email': 'swacker@ucalgary.ca',
    'scripts': ['scripts/Mint.py', 'scripts/Mint.bat'],
    'packages': ['ms_mint'],
    'data_files': [('scripts', ['scripts/Mint.py', 'scripts/Mint.bat']),
                   ('static', ['static/Standard_Peaklist.csv'])],
    'classifiers': [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
   'python_requires': '>=3.5',
   'install_requires': install_requires
}

setup(**config)
