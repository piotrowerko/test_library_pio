from setuptools import find_packages, setup


setup(
    name='te_li_pio',
    packages=find_packages(include=['te_li_pio']),
    version='0.1.0',
    description='this is only a testing library',
    author='Piotr Owerko',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)



