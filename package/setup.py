from setuptools import setup, find_packages

setup(
    name="Topsis-Kanika-102313062",
    version="1.0.0",
    author="Kanika",
    author_email="kkanika1_be23@thapar.edu",
    description="Implementation of TOPSIS method as a Python package",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_kanika_102313062.topsis:main"
        ]
    },
    python_requires=">=3.7",
)
