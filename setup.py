import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="miinfra-asg1612",
    version="0.0.1",
    author="Andrés Sánchez García",
    author_email="asg1612@gmail.com",
    description="cli para controlar mi infraestructura",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asg1612/miinfra",
    project_urls={
        "Bug Tracker": "https://github.com/asg1612/miinfra/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)