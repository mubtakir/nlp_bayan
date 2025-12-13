"""
Setup script for Bayan Programming Language
لغة البيان - أول لغة برمجة هجينة عربية
"""

from setuptools import setup, find_packages

setup(
    name="bayan",
    version="2.0.0",
    author="Basil Yahya Abdullah",
    author_email="mubtakir@example.com",
    description="Bayan - The First True Hybrid Programming Language with Arabic Support",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mubtakir/nlp_bayan",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Arabic",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "flask>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
        ],
        "ai": [
            "numpy>=1.20.0",
        ],
        "nlp": [
            "camel-tools>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bayan=bayan.main:main",
        ],
    },
    keywords=[
        "bayan", "arabic", "programming", "hybrid", "logic",
        "البيان", "عربي", "برمجة", "هجين", "منطق"
    ],
)
