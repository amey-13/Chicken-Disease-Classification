import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = 'Chicken-Disease-Classifier'
AUTH_USERNAME = "amey-13"
SRC_REPO = "ChickenDiseaseClassifier"
AUTH_EMAIL = "ameysawant1300@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTH_USERNAME,
    author_email=AUTH_EMAIL,
    description='A small python package for CNN app',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTH_USERNAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTH_USERNAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)