import setuptools

with open("README.md","r") as rm:
    long_description=rm.read()


setuptools.setup(
        #Name of the project
        name="WATF",
        #version 
        version="0.0.1",
        #one-liner description or tag line of the 
        #project
        description="Web Application Testing Framework",
        #Name of the author or the organisation
        author= "Pooja Sharma",
        author_email="pooja.sharma@atlascopco.com",
        url="https://github.com/Sharma-poo/WATF.git",
        #classifiers helps to find some additional
        #metadata about the project
        classifiers=[
            #'python_requires' for the project
            "Programming Language :: Python :: 3.6",
            #How mature the project? Common Stages of 
            #Development are
            #3-Alpha
            #4-Beta
            #5-Production/Stable
            #6-Mature
            "Development Status :: 3 - Alpha",
            ],
        #Python version supported by the project
        python_requires= '>=3.6',
        #Another packages dependencies
        install_requires=[
            "pytest==5.3.1",
            "selenium==3.141.0",
            "splinter==0.10.0",
            ],



        )

