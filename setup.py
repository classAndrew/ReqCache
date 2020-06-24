import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reqcache-classAndrew", # Replace with your own username
    version="0.0.1",
    author="Andrew",
    author_email="andrewspam314@gmail.com",
    description="A Python3 library for caching requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/classAndrew/ReqCache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)