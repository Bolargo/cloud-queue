import setuptools

setuptools.setup(
    name='cloud_queue',
    version='0.0.3',
    description='An abstraction of SQS and Azure Queue Storage',
    packages=setuptools.find_packages(exclude=('tests',)),
    author='Francisco José Cotán López',
    keywords=['queue', 'cloud', 'aws', 'azure'],
    url='https://github.com/Bolargo/cloud_queue',
    python_requires='>=3.8'
)