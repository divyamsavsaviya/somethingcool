from setuptools import setup, find_packages

setup(
    name="ai_coding_assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flet==0.7.4",
        "neurum==1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai_coding_assistant=src.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered coding assistant using Flet and Neurum",
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/divyamsavsaviya/somethingcool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)