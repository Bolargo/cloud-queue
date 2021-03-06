import setuptools

setuptools.setup(
    name='cloud_queue',
    version='0.0.4',
    description='An abstraction of SQS and Azure Queue Storage',
    packages=setuptools.find_packages(exclude=('tests',)),
    author='Francisco José Cotán López',
    keywords=['queue', 'cloud', 'aws', 'azure'],
    url='https://github.com/Bolargo/cloud-queue',
    python_requires='>=3.8',
    install_requires=[
        'boto3', 'azure-storage-queue'
    ]
)