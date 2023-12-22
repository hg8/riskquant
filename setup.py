from setuptools import setup, find_packages

version = '0.1.0'  # Must correspond to a git tag

setup(
    name='riskquant',
    packages=["riskquant", "riskquant.model"],
    version=version,
    license='apache-2.0',
    author='Netflix Detection team',
    author_email='detection@netflix.com',
    description='A library for applying quantitative risk models.',
    keywords='riskquant risk quantify statistics',
    classifiers=[
                 'Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Topic :: Security',
                 'Intended Audience :: Information Technology',
                 'Intended Audience :: Financial and Insurance Industry',
                 'Intended Audience :: System Administrators',
                 'Topic :: Office/Business :: Financial'
    ],
    url='https://github.com/hg8/riskquant',
    setup_requires=['setupmeta'],
    python_requires='>=3.7',
    install_requires=[
        'matplotlib',
        'numpy >=1.19.0',
        'scipy',
        # Tensorflow probability is tested and stable against Tensorflow 2.1.0
        # https://github.com/tensorflow/probability/releases
        'tensorflow',
        'tensorflow_probability'
    ],
)
