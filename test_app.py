#importing add function from app.py file
from app import add

#testing add function
def test_add():
    assert add(2, 3) == 5