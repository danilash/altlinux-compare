from setuptools import setup, find_packages

setup(
    name='altlinux_api',
    version='1.19.16',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'altlinux-compare=altlinux_api.cli:main',
        ],
    },
)