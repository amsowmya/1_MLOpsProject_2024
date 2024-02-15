from typing import List

HYPEN_DOT_E = "-e ."

def get_requirement(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements



get_requirement("requirements_dev.txt")