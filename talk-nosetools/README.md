GIST, since checkout is used.
1. https://github.com/jmrnilsson/talknosetools

# talknosetools
__-A talk on testing with nosetools and mock__

## Outline

+ Discovery of tests (and how to ignore them)
+ Running (terminal and PyCharm)
+ Assign setup, teardown (different ways)
+ Using nosetools' asserts and built-in asserts
+ Checking PEP-8 (Flake8 included in CodeClimate)
+ Cyclomatic complexity (Radon included in CodeClimate)

Started out with 20 steps and now only 10. Approximately 1h but depends on many things. If one has
any questions, I'll do my best but only had 12M:s of experience working with this.

## Also briefly covered:
+ pip
+ requirements.txt
+ setup.cfg

## Step 1: Python with VirtualEnv
http://docs.python-guide.org/en/latest/dev/virtualenvs/

    virtualenv venv
    ls venv
    source venv/bin/activate
    deactivate
    . venv/bin/activate
    export PYTHONPATH=.

    pip install requests
    echo 'requests==2.9.1' > requirements.txt
    pip install -r requirements.txt
    pip list --outdated
    pip list

## Step 2: REPL, Assertions, Tests

### REPL
A read–eval–print loop (REPL), also known as an interactive toplevel or language shell. REPL is
commonly available at `python` or `ipython`.

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


A note on imports in python:

    >>> from re import *
    >>> findall('a', 'asdma')
    ['a', 'a']
    >>> findall('as', 'asdma')
    ['as']
    >>> import re
    >>> re.findall('as', 'asdma')
    import re as regexorz
    regexorz.findall('am', 'mammma')

### Assertions

    assert 2 > 1

+ Compare with DbC
+ C# Code Contracts [https://github.com/Microsoft/CodeContracts](https://github.com/Microsoft/CodeContracts)
+ [https://www.eiffel.org](https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20%28tm%29%2C%20Assertions%20and%20Exceptions)

"A few techniques can help shift the numbers in our favor, including:
+ good error logging,
+ good testing,
+ and internal self-checks (assertions).
"
[https://wiki.python.org](https://wiki.python.org/moin/UsingAssertionsEffectively)

test/01_builtin_assert_tests.py:

`C: 0`

    assert 2 < 1
    print 'yes, you did it!'

    #!/usr/bin/env python

    python tests/01_builtin_assert_tests.py
    python -O tests/01_builtin_assert_tests.py
    ./tests/01_builtin_assert_tests.py
    chmod +x ./tests/01_builtin_assert_tests.py
    ./tests/01_builtin_assert_tests.py

`C: 1`

## Step 3: Create tests

    from download import beers


    def test_beers_exists():
        actual = list(beers.find_all())

        assert len(actual) > 100
        print 'yes, you did it!'

    . venv/bin/activate; nosetests tests

`C: 1`

## Step 4

+ http://stackoverflow.com/questions/1457104/nose-unable-to-find-tests-in-ubuntu
+ option is to run `nosetests --exe`

    chmod -x tests/01_builtin_assert_tests.py
    . venv/bin/activate; nosetests tests


`download/beers.py`
## Step 5:
```
    import requests


    def find_all(predicate=lambda r: True):
        response = requests.get('http://www._.se/api/assortment/products/json')
        response.raise_for_status()
        json_response = response.json()
        rows = (dict(zip(json_response['columns'], row)) for row in json_response['rows'])
        return sorted(filter(predicate, rows), key=lambda r: r['price_per_litre'])


    def find_by_start(start):
        return find_all(predicate=lambda r: r['start'] >= start)
```

    . venv/bin/activate; nosetests tests


`tests\__init__.py`

```
import os
import json
from codecs import open

from mock import Mock
import requests

__get = requests.get


def setup_module():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb_.json', encoding='utf-8') as fp:
        rows = json.loads(fp.read().encode('utf-8'))
        requests.get = Mock(return_value=Mock(json=Mock(return_value=rows)))


def teardown_module():
    requests.get = __get

```

    . venv/bin/activate; nosetests tests

`C: 3`

## Step 7: Before we get carried away, flake8 radon

    echo '[flake8]' > setup.cfg
    echo 'max-line-length=100' >> setup.cfg
    echo 'ignore=E731' >> setup.cfg

    flake8 ./*.py download
    radon cc -a -nc -e "venv/*" ./

Some of these feature are included in i.e. CodeClimate which is free for OSS, I think. But's a piece
of cake to setup with Makefile.

`C: 4`

## Step 5 using nose.tools asserts and generators

    cp tests/02_ordering_tests.py._ tests/02_ordering_tests.py
    nosetests tests

Missing some info about the tests, very unfortunate

    echo '[nosetests]' >> setup.cfg
    echo 'verbosity=2' >> setup.cfg

    nosetests tests

Nicer output, also generators show metadata.

`C: 5`

## Step 6: Running tests
+ Show how to add a new Test Configuration. Press plus-sign and check all in folder and add
`--nocapture`

## Step 7: Create test to demonstrate patch
`tests/03_using_patch_tests.py`

    def test_retry_with_patch():
        with patch.object(requests, 'get', side_effect=KeyError('some')):
            assert_raises(KeyError, beers.find_all)

Alternatively `cp tests/03 ...`

show `assert_equal(requests.get.call_count, 2)`
show `with_setup`

`C: 6`

## Step 8: Side-effects - the good parts

Do `cp tests/04 ...` and add:

    b = beers.find_all()
    assert_equal(b, 0)


## Step 9:

Do `cp tests/05 ...` OR :


    def test_by_start_date():
        actual = beers.find_by_start('2015-05-01')[0]

        assert_greater_equal(actual['start'], '2015-04-29')

and add imports and then:

    def test_by_custom_predicate_name():
        actual = beers.find_all(predicate=lambda r: re.findall('^Swe', r['name']))

        print actual
        assert_is_not_none(actual)

and add more imports

    . venv/bin/activate; nosetests tests

``

## Step 10: Discover of tests

    Ignoring tests and the concept of hidden, very hidden.
    Rename `^02` to `tes$` and then `test$`
