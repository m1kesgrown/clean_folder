from setuptools import setup, find_namespace_packages

setup(
    name='Clean folder function',
    version='0.1.4',
    description='This is my frist package from homework',
    author='Oleksii Chygrin',
    author_email='czygrin.oleksii@gmail.com',
    url='https://github.com/m1kesgrown/basics/clean_folder',
    license='MIT',
    packages=find_namespace_packages(where='clean_folder'),
    packages_dir={'': 'src'},
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
    include_package_data=True,
    install_requires=[''],
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:sort']}
)
