from setuptools import setup, find_packages

setup(
    name='toTrello',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['toTrello = trello_tool.publish_story_to_trello:main']
    },
    install_requires=[
        "requests==2.25.1"
    ],
    url='https://github.com/LogosFu/trello-tool',
    license='GNU General Public License v3.0',
    author='LogosFu',
    author_email='logosfu@gmail.com',
    description='publish work flow to trello'
)
