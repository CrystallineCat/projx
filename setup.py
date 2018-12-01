from distutils.core import setup


setup(
    name="projx",
    version="0.3.6-mn",
    url="http://projx.readthedocs.org/en/latest/#",
    license="MIT",
    author="mniederlechner",
    author_email="mniederlechner@gmx.net",
    description="Graph transformations in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["projx", "projx.modules"],
    install_requires=[
        "networkx==2.2",
        "pyparsing==2.0.2"
    ]
)
