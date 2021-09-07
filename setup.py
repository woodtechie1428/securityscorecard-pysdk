from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('src/securityscorecard_api/version2.py').read())

setup(
    name="securityscorecard_api",
    version=__version__,
    author="Wood Techie",
    author_email="woodtechie1428@gmail.com",
    description="Python SDK for interacting with the SecurityScorecard API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woodtechie1428/securityscorecard-pysdk",
    project_urls={
        "Bug Tracker": "https://github.com/woodtechie1428/securityscorecard-pysdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    py_modules=["securityscorecard_api"],
    install_requires=['requests']

)
