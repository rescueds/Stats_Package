import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Stats_Package_TEST',
    version='0.0.4',
    author='E.Jones',
    author_email='ejones@rescueagency.com',
    description='Stats Package for use by the Rescues Research Dept',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rescueds/Stats_Package_TEST.git',
    project_urls = {
    },
    license='MIT',
    packages=['Stats_Package_TEST'],
    install_requires=['pandas', 'numpy', 'matplotlib', 'researchpy', 'scipy'],
)
