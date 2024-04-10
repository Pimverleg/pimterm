from setuptools import setup, find_packages

setup(
    name="pimterm",
    version="1.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pimterm=pimterm.main:main',
        ],
    },
    description="A simple Python package that helps you find the command you need.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Pim Verleg",
    author_email="pim_iets@hotmail.com",
    license="MIT",
    install_requires=[
        'openai',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
