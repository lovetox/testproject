from setuptools import setup
from setuptools import find_packages

setup(
  name='testproject',
  description='Test Project',
  version='1.0.0',
  packages=find_packages(),
  package_data={
        'testproject': ['py.typed'],
  },
  python_requires='>=3.7',
  long_description_content_type="text/markdown",
  classifiers=[
        "Programming Language :: Python :: 3.7",
  ]
)
