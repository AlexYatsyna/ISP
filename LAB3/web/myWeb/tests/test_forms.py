import pytest
from main.forms import PostForm, UserRegistrationForm


@pytest.fixture
def user_data_signup():
    return {"username": "Alina", "password": "testpassword", "password2": "testpassword"}


@pytest.fixture
def post_data():
    return {"title": "PyTest", "text": "it's test"}


@pytest.mark.django_db
def test_signup(user_data_signup):
    assert UserRegistrationForm(data=user_data_signup).is_valid()


@pytest.mark.django_db
def test_post(post_data):
    assert PostForm(data=post_data).is_valid()
