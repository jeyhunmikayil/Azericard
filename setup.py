import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
REQUIRED = [
    'requests',
]
setuptools.setup(
    name="azericard-django", # Replace with your own username
    version="0.0.1",
    author="Cavid Rzayev",
    author_email="rzayev592@gmail.com",
    description="Django ucun standart azericard odenis kitabxanasi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIRED,
    url="https://github.com/CavidRzayev/Azericard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
