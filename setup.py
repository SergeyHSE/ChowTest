from setuptools import setup, find_packages

setup(
    name='ChowTest',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'scipy',
        'pandas',
        'numpy',
    ],
    author='Your Name',
    author_email='snmikhaylov@edu.hse.ru',
    description='Chow Test implementation',
    url='https://github.com/SergeyHSE/ChowTest',
)
