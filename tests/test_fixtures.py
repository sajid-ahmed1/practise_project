import pytest

# We can also enable start logging function that indicates when a test is running.
# Autouse is used to run everytime regardless if log_start is called or not.
@pytest.fixture(autouse=True)
def log_start():
    print('Starting to test')


# scope enables us to control 
@pytest.fixture(scope='function')
def sample_list():
    '''
    sample_list is a fixture that we can add to parameters.
    With pytest.fixture we set a dataset and then run tests on that dataset.
    '''
    print('sample_list has been called and ready to serve!')
    return [1, 2, 3]

def test_sum(sample_list):
    assert sum(sample_list) == 6

def test_count(sample_list):
    assert len(sample_list) == 3

@pytest.fixture(autouse=True)
def log_end():
    print('Ending to test')

# The alternative is the below with the copy-pasting the same sample_list.
# The sample_list is within the definition function, but better to be stated outside.
'''
def test_sum():
    sample_list = [1, 2, 3]
    assert sum(sample_list) == 6

def test_count():
    sample_list = [1, 2, 3]
    assert len(sample_list) == 3
'''