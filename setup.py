from setuptools import setup , find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requiremnts_list()-> List[str]:
    with open("requirements.txt") as f:
        requirement_list =  f.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

            return requirement_list
    


setup(
    name = "ML Project",
    version="1.0.0",
    author= "Karan",
    description= "Predicts the delivery time of the food",
    author_email= "godthatback21@gmail.com",
    packages = find_packages(),
    install_requires = get_requiremnts_list()
)