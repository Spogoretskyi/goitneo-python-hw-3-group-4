from setuptools import setup, find_packages

setup(
    name='cli_bot',
    version='3.0.0',
    description='cli_bot',
    url='https://github.com/Spogoretskyi/goitneo-python-hw-3-group-4.git',
    author="Sergii Pogoretskyi",
    author_email="spogoretskyi@gmail.com",
    packages=find_packages(),
    entry_points={'console_scripts': [
        'cli_bot = CLI_BOT.cli_bot.main:main']},
)