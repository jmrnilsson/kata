import requests
from mock import Mock

requests.get = Mock(side_effect=Exception('BOOM!'))
