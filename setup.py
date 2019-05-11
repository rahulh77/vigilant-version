import setuptools

setuptools.setup(# Needed to silence warnings (and to be a worthwhile package)
    name='vigilant-version',
    url='https://github.com/rahulh77/vigilant-version',
    author='Rahul',
    author_email='rahul999@gmail.com',
    # Needed to actually package something
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    # Needed for dependencies
    # install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown"
)
