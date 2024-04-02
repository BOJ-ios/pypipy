import setuptools

setuptools.setup(
    include_package_data=True,
    name='pypipy',
    version='0.0.2',
    description='oss-dev my pypi 001',
    author='mingyukim',
    author_email='843850@donga.ac.kr',
    url="https://github.com/BOJ-ios/pypipy",
    download_url="https://github.com/BOJ-ios/pypipy/archive/refs/tags/v0.0.2.zip",
    install_requires=['pytest'],
    long_description='oss-dev pypi python module',
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
