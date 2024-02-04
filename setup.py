# This file is responsible in creating ML application as a package
# This can then be installed and used in other ML projects

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    # Open file as temporary file object
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()   # read every line
        # List comprehension to replace \n characters from readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        # removes the '-e .' command which runs setup.py and makes
        # packages editable
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Emad',
author_email='emadahmedc16@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   

  
      )