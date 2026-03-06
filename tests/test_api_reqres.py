import requests
import pytest

# Usamos un User-Agent de un navegador muy común y headers de aceptación
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}
@pytest.mark.skipif(reason="Skipping test")
def test_get_placeholder(url_base):
    # JSONPlaceholder no suele bloquear IPs
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    print(response.json()['name'])
@pytest.mark.skipif(reason="Skipping test")
def test_create_user(url_base):
    session = requests.Session()
    payload = {"name": "Antonella", "job": "Qa Tester"}
    response = session.post(url_base, json=payload, headers=HEADERS, timeout=10)
    assert response.status_code == 201
@pytest.mark.skipif(reason="Skipping test")
def test_delete_user(url_base):
    session = requests.Session()
    # JSONPlaceholder devuelve 200 en lugar de 204 para DELETE
    response = session.delete(f"{url_base}/2", headers=HEADERS, timeout=10)
    assert response.status_code == 200