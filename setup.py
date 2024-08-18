from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->list[str]:
    '''

    we are creating a fx to install all the packages in requirement.txt

    '''

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name = "Machinelearning",
version='0.0.0',
author='Rohan',
author_email='rohan.sharma2467@gmail.com',
packages=find_packages(),
install_require=get_requirements['requirements.txt']
)