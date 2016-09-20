from mock import patch
import requests
from nose.tools import assert_raises

from download import beers


def test_retry_with_patch():
    with patch.object(requests, 'get', side_effect=KeyError('some')):
        assert_raises(KeyError, beers.find_all)
