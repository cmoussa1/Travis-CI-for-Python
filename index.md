# Setting Up Travis CI For Python Projects

In this tutorial I am going to be showing you how to set up Travis Continuous Integration (or CI for short) for a Python project. 

## *What is Travis CI?*

[Travis CI](https://docs.travis-ci.com/user/getting-started) is a continuous integration tool that allows developers to test small code changes very frequently, rather than making big changes few and far between. When smaller changes are made, code is easier to debug and problems seem far less daunting. Travis CI achieves this feature by allowing us to test our code in smaller increments. 

Travis CI can work with a GitHub repo, so all you really need to do is link your two accounts together (what makes it even easier is that you can sign in to Travis using your GitHub account) and allow access to the repo's contents. After that, every time you make a commit to GitHub with some changes, Travis will test those changes to make sure that your program is still working. 

## *Setting up Travis CI*

For this tutorial I am going to be testing just one file, **stats.py**, a simple Python script that can compute some basic statistics from a list of numbers. In our first version, **stats.py** contains three methods: *compute\_avg*, *compute\_min*, and *compute\_max*. I want to test my methods to make sure that they return the right answer, so I have a test file, **unittest_stats.py**, that tests these three methods. 

Our GitHub repo now contains these two files, maybe with a README to describe the functionality further. It's time to link this repo with Travis CI.

###### Note

*Make sure that you have admin privileges on the repo you are trying to integrate Travis CI with. If your repo is in an organization on GitHub, make sure that you are a member of that org before setting Travis up!*

1. Go to [Travis CI's website](https://travis-ci.com) and click the "Sign in with GitHub" button on the top right corner of the screen.
2. You may need to authorize Travis Ci to have permission to access your GitHub repos before you see them show up on Travis' side. To do this, go to GitHub --> Settings --> Personal settings --> Applications --> Authorizes OAuth Apps and configure the settings there.
3. Add a **.travis.yml** file to your repository. This is what instructs Travis CI what to do with your code. For a Python project, and for this specific repo, the following contents should work fine:

```
language: python
python:
    - "2.7"
    - "3.3"
    - "3.4"
    - "3.5" 
    - "3.5-dev"  # 3.5 development branch 
    - "3.6"
    - "3.6-dev"  # 3.6 development branch  
    - "3.7-dev"  # 3.7 development branch
install:
    - pip install codecov 
# command to run tests
script:
    - python unittest_stats.py 
```

* `language` specifies the language that your code is written in.
* `python` tells Travis all of the versions of Python that you want to test your code against.
* `install` specifies any dependencies that may be required when running your project. In this file we have `pip install codecov` in case we may want to also use Code Coverage to analyze how much of our program is actually being tested (but this is a separate topic).
* `script` tells Travis what command to run. In our case, we want to run our test script **unittest_stats.py**, so we use the command that we would in a terminal.

4. Watch Travis work! On the website you will see it automatically update once you push your **.travis.yml** file to your GitHub repo. It tests your scripts against all of the Python versions you specified, and can even output detailed logs of each run. All you have to do is click on each Build Job to see details of its success (or perhaps even more importanly, a failure!).

## An Example of a Failed Build

More often than not, the first time we build with Travis will show us some errors it encountered while building. This is okay, because all we have to do is look at the raw log of the failed build and see what went wrong. 

For example, let's say in our *compute_avg* method in **stats.py** I added a print statement that looked like the following:

`print "The average is " + str(avg)`

This is incorrect syntax according to the official documentation for Python version 3.x. We will see this error in Travis' Build Log: 

`The command "python unittest_stats.py" exited with 1.`

And just above that, we can see what actually caused the error. In this case, it was a syntax error that triggered while testing against Python 3.3:

```
File "/home/travis/build/cmoussa1/Travis-CI-for-Python/stats.py", line 7
	print "The average is " + str(avg)
                          ^
SyntaxError: invalid syntax
```

This is an easy fix! All we need to do is add a set of parentheses around our print statement and everything will get back to working normally. 

## Adding a Travis CI Build Badge to your GitHub Repo's Home Page

If you want to see your Travis CI's build status straight from your GitHub Repo's home page, all you need to do is add the following line to your README:

```
[![Build Status](https://travis-ci.com/cmoussa1/Travis-CI-for-Python.svg?branch=master)](https://travis-ci.com/cmoussa1/Travis-CI-for-Python)
```

Before you first integrate Travis, the badge should look like this: [![Build Status](https://travis-ci.com/cmoussa1/Cthulu-Resume.svg?branch=master)](https://travis-ci.com/cmoussa1/Cthulu-Resume)

But after your succesfully build your project, your badge will look like this: [![Build Status](https://travis-ci.org/LLNL/py-hostlist.svg?branch=master)](https://travis-ci.org/LLNL/py-hostlist)


## Summary

I hope this tutorial helped with setting up and integrating Travis CI with your Python project! This tool is great for seeing how changes in your code affect build success, as well as ensuring that your code is version agnostic. 