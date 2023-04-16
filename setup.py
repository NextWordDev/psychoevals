from setuptools import setup, find_packages

setup(
    name='psychoevals',
    version='0.8',
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
        "pandas>=1.3.0",
        "tenacity>=8.0.0",
        "python-dotenv>=0.15.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.7',
    author='John (@nextword)',
    author_email='public@nextword.dev'
)