from distutils.core import setup

setup(
    name="cloudwatch_handler",
    version="0.2",
    description="Shamelessly stolen from https://github.com/ernestomonroy/cloudwatch - I'd have forked but that repo has been deleted",
    author="Chris Fernando",
    author_email="chris.t.fernando@gmail.com",
    url="https://github.com/chris-t-fernando/cloudwatch-handler",
    #packages=["cloudwatch_handler"],
    py_modules = ['cloudwatch_handler.cloudwatch']
)