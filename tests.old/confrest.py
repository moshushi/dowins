import pytest

pytest_plugins = ['json_fixtures']

@pytest.fixture
def fixture_a():
    return 'value'
