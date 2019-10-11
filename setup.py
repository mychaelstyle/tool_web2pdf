from setuptools import setup, find_packages


install_requires = ['PyPDF2','pytest']

dependency_links = []

setup(
    name='mychaelstyle_tool_web2pdf',
    version='0.1',
    description='',
    author='Masanori Nakashima',
    author_email='m_nakashima@beecomb-grid.co.jp',
    url='',
    install_requires=install_requires,
    dependency_links=dependency_links,
    license=license,
    packages=find_packages()
)
