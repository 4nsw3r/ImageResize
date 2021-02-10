import pytest
from django import urls



@pytest.mark.parametrize('param', [
    ('index'),
    ('new'),
])
@pytest.mark.django_db
def test_urls(client, param):
    url = urls.reverse(param)
    resp = client.get(url)
    assert resp.status_code == 200