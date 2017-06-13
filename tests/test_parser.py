import pytest
from dowins import dowins

def test_parser():
    assert dowins.parse_args(['someaccount']).name == 'someaccount'
