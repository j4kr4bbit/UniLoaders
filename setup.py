from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='UniLoaders',
    version='0.0.1',
    description='Loading everything from URLs to powerpoints',
    author='Enzo Bonelli', 
    long_description=long_description,
    long_description_content_type="text/markdown", 
    packages=find_packages(),
    install_requires=[
        "langchain",
        "pypdf",
        "unstructured[pdf]",
        "unstructured[docx]",
        "unstructured[ppt]",
        "docx2txt",
        "unstructured",
        "pdfminer"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache-2.0', 
    python_requires='>=3.6',
)