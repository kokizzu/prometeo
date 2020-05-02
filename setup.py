from setuptools import setup, find_packages, dist

class BinaryDistribution(dist.Distribution):
    def has_ext_modules(foo):
        return True

setup(name='prometeo',
    version='0.1',
    python_requires='>=3.6, <=3.9',
    description='a prototyping and modelling tool for embedded optimization',
    url='http://github.com/zanellia/prometeo',
    author='Andrea Zanelli',
    license='LGPL',
    packages = find_packages(),
    entry_points={'console_scripts': ['pmt=prometeo.__main__:console_entry']},
    install_requires=[
        'astpretty',
        'strip_hints',
        'astunparse',
        'numpy',
        'scipy',
        'multipledispatch',
        'pyparsing',
        'casadi==3.4.5',
        'jinja2'
    ],
    package_data={'': \
        ['lib/prometeo/libcpmt.so', \
        'lib/blasfeo/libblasfeo.so', \
        'include/prometeo/*', \
        'include/blasfeo/*']},
    include_package_data=True,
    zip_safe=False)
