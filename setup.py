from setuptools import setup, find_packages


setup(
    name='recaptchav3py',
    version='0.0.2',
    license='MIT',
    author='Tomás Perestrelo',
    author_email='tomasperestrelo21@gmail.com',
    packages=find_packages(exclude=('tests*', 'testing*')),
    url='https://github.com/thicccat688/recaptchav3py',
    download_url='https://pypi.org/project/recaptchav3py/',
    keywords='python, google, recaptchav3',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
      ],
)
