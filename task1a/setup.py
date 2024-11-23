from setuptools import find_packages, setup

package_name = 'task1a'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bismuth',
    maintainer_email='siddharthaswarnkar@gmail.com',
    description='Python script for Task1A',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['task_node = task1a.task:main'
        ],
    },
)
