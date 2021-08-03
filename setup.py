from setuptools import setup, find_namespace_packages

packages = find_namespace_packages()
setup(
    name="samtestci",
    version="0.1.dev0",
    author="Sam",
    author_email="sam@sam.edu",
    packages=packages,
    license="BSD 3-Clause License",
    description="dummy test stuff",
    url="https://github.com/sschmidt23/samtestci",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD 3-Clause",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        ],
    install_requires=['numpy',
                      'matplotlib',
                      ],
    python_requires=">=3.5",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
