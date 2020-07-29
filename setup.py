from setuptools import setup, find_packages

setup(
    name = 'dric_client',
    version = '1.1.0',
    description = 'Python client interface to Dr.IC platform',
    author = 'Kang-Woo Lee',
    author_email = 'kwlee@etri.re.kr',
    url = 'https://github.com/kwlee0220/dric.client.python',
    install_requires = [
        'PyYAML',
        'paho-mqtt',
        'protobuf',
        'fastavro',
        'grpcio'
    ],
    packages = find_packages(),
    data_files=['marmot_dataset_pb2.py'],
    python_requires = '>=3',
    zip_safe = False
)