from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
	""
	requirements = []
	with open(file_path) as file_obj:
		requirements = file_obj.readlines()
		requirements = [req.replace("\n","") for req in requirements]
		if "-e ." in requirements:
			requirements.remove("-e .")

    
setup(
	name="ML_PROJECT",
	version="0.0.1",
	author="Aayush kanungo",
	author_email="aayushak98.ak@gmail.com",
	packages=find_packages(),
	install_requires=get_requirements('requirement.txt')
	
	)