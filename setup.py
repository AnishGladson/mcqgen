from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Anish Gladson",
    author_email="anishgladson.1999@gmail.com",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "langchain-openai",
        "langchain-huggingface",
        "huggingface-hub",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
    ],
)
