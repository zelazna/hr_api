import json

from tests import factories


def post(client, path, data):
    return client.post(
        path,
        data=json.dumps(data),
        content_type='application/json'
    )


def login(client, email, password):
    return post(
        client,
        '/auth/login',
        {'email': email, 'password': password}
    )


def register(client, email, password):
    return post(
        client,
        '/auth/register',
        {'email': email, 'password': password}
    )


def test_login(client, session):
    factories.UserFactory.create(email='test', password='test')
    json_data = login(client, 'test', 'test').data
    dict_data = json.loads(json_data)
    assert 'auth_token' in dict_data
    assert dict_data['status'] == 'success'


def test_register(client, session):
    json_data = register(client, 'test', 'test').data
    dict_data = json.loads(json_data)
    assert 'auth_token' in dict_data
    assert dict_data['status'] == 'success'
