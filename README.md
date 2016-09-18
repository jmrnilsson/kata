# talknosetools
> A talk on testing with nosetools

## Outline
### Setting up tests and linter with nosetools, flake8 and radon.

+ Discovery of tests (and how to ignore them)
+ Running (terminal and pycharm, maybe vscode)
+ Assign setup, teardown (different ways)
+ Using nosetools' asserts and using built-in
+ Checking PEP-8 (Flake8 included in CodeClimate)
+ Cyclomatic complexity (Radon included in CodeClimate)

### Also briefly covered:
+ pip
+ requirements.txt
+ setup.cfg

---

## Step 1: Python with VirtualEnv
http://docs.python-guide.org/en/latest/dev/virtualenvs/

    virtualenv venv
    ls venv
    source venv/bin/activate
    deactivate
    . venv/bin/activate
    pip install requests
    echo 'requests==2.9.1' > requirements.txt
    pip install -r requirements.txt
    pip list --outdated
    pip list

---

## Step 2: REPL, Assertions, Tests

### REPL
A read–eval–print loop (REPL), also known as an interactive toplevel or language shell.

    >>> list([1, 2])
    [1, 2]
    >>> list([1, 2, 4])
    [1, 2, 4]
    >>> set([1, 2, 4])
    set([1, 2, 4])
    >>> set([1, 2, 4, 4])
    set([1, 2, 4])
    >>> set([1, 2, 4, 4])
    >>> dict({'k': 'andy', 'k': 2})
    {'k': 2}
    >>> dict({'k': 'andy', 'k2': 2})
    {'k2': 2, 'k': 'andy'}
    >>> dict({'k': 'andy', 'k2': 2})

### Assertions
+ Compare with DbC
+ C# Code Contracts [https://github.com/Microsoft/CodeContracts](https://github.com/Microsoft/CodeContracts)
+ [https://www.eiffel.org](https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20%28tm%29%2C%20Assertions%20and%20Exceptions)

"A few techniques can help shift the numbers in our favor, including good error logging, good testing, and internal self-checks (assertions). I wanted to write briefly about how assertions can help with Python code."
[https://wiki.python.org](https://wiki.python.org/moin/UsingAssertionsEffectively)

    #!/usr/bin/env python
    python -O

## Step 3: Create tests
    api.get_beers()
    . venv/bin/activate; nosetests tests


## 4

    mv to tests
    mv to *-test.py
    mv to *-test
    export PYTHONPATH=.


## 5 using nose.tools asserts *


## 6 create generator

    nosetests tests
