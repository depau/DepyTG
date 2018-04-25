from setuptools import setup

with open("README.md") as f:
    DESCRIPTION = f.read()

setup(
    name='DepyTG',
    version='3.6.2',
    packages=['depytg'],
    url='https://github.com/Depau/DepyTG',
    author='Davide Depau',
    author_email='davide@depau.eu',
    description='The only Telegram bot library that does nothing',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='telegram bot development',
    python_requires='>=3',
    requires=["requests"],
    extras_require={
        'flask': ['Flask']
    }
)
