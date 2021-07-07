from setuptools import setup

setup(
    name='booktetium',
    version='0.1',
    packages=['booktetium'],
    url='https://github.com/search5/booktetium',
    license='BSD3',
    author='이지호',
    author_email='search5@gmail.com',
    description='도서 공식 홈페이지',
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask-sqlalchemy', 'psycopg2-binary']
)
