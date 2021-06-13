import pytest
from django.contrib.auth import get_user_model
from main.models import Post
from main.forms import PostForm, UserRegistrationForm
from django.urls import reverse

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(username="Dima", password="zxcvb")


@pytest.fixture
def post(user):
    return Post.objects.create(title="This is test", text="car", author=user)


@pytest.mark.django_db
def test_sign_up(client):
    data = {"username": "Kostya", "password": "asdfg", "password2": "asdfg"}
    assert UserRegistrationForm(data=data).is_valid()
    client.post("/signup", data)
    assert User.objects.filter(username=data["username"])


@pytest.mark.django_db
def test_sign_in(client, user):
    data = {"username": user.username, "password": "zxcvb"}
    client.post("/signin", data)
    assert client.post("/signin", username=user.username, password="zxcvb")
    assert client.login(username=user.username, password="zxcvb")


@pytest.mark.django_db
def test_profile(client, user):
    temp_url = reverse("user_profile", args=(user.id,))
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_new_ad(client, user):
    client.login(username=user.username, password="zxcvb")
    resp_get = client.get("/ad/new")
    assert resp_get.status_code == 200
    data = {"title": "asdasd", "text": "sdefghhgj"}
    assert PostForm(data=data).is_valid()
    resp_post = client.post("/ad/new", data)
    assert resp_post.status_code == 302


@pytest.mark.django_db
def test_main_page(client, user):
    temp_url = reverse("home")
    resp = client.get(temp_url)
    assert resp.status_code == 200
    client.login(username=user.username, password="zxcvb")
    resp_get = client.get("/")
    assert resp_get.status_code == 200


@pytest.mark.django_db
def test_faq(client, user):
    temp_url = reverse("faq")
    resp = client.get(temp_url)
    assert resp.status_code == 200
    client.login(username=user.username, password="zxcvb")
    resp_get = client.get("/faq")
    assert resp_get.status_code == 200







