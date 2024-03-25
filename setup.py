from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='pydatascraper',
    version='1.0.4',
    packages=['pydatascraper'],  # Explicitly include your main package here
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'tldextract',
        'openpyxl',
    ],
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='A Python application that provides web scraping capabilities, including fetching Google and Yelp reviews.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/arjunlimat/pydatascraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
