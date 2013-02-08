# coding: utf-8
from distutils.core import setup

setup(
    name="Easy ToDo",
    version='0.1',
    author='Wojciech Żółtak',
    packages=['easy_todo', 'easy_todo.storage'],
    scripts=['easy_todo/bin/easy-todo']
)

