from setuptools import setup, find_packages

with open('requirements.txt') as f:
    packages = f.read().splitlines()

AUTHOR = '{{cookiecutter.author_name}}'
AUTHOR_EMAIL = '{{cookiecutter.author_email}}'

if __name__ == "__main__":
    setup(
        name='{{cookiecutter.project_name}}',
        version="0.0.1",
        packages=find_packages(),
        license='',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description='',
        install_requires=packages,
        tests_require=['pytest'],
        include_package_data=True,
        python_requires=">=3.12"
    )

