from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Biblioteca para processamento de imagens
    ],
    description='Um pacote para processamento de imagens',
    author='Seu Nome',
    author_email='seu.email@example.com',
    url='https://github.com/seu_usuario/image_processor',  # URL do repositório do projeto
)
