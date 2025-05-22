from setuptools import setup, find_packages

setup(
    name="programming_ii",
    version="0.1.0",
    description="Exercises and examples for Programming II",
    author="Lucas Portela",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'gitpython',      
        'ipykernel',
        'pytest',
        'numba',
        'pygame',
        'openpyxl',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
