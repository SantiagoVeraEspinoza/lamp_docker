import pytest
import requests

# Define la URL base de tu servidor Apache
BASE_URL = 'http://localhost'

@pytest.fixture(scope='module')
def apache_url():
    # Puedes modificar la URL base si es necesario
    return BASE_URL

def test_apache_homepage(apache_url):
    # Realiza una solicitud GET a la URL base
    response = requests.get(apache_url)

    # Verifica que la solicitud fue exitosa
    assert response.status_code == 200, f"Status code expected 200, but got {response.status_code}"

    # Verifica que el contenido de la respuesta no está vacío
    assert response.text, "Response body is empty"

    # Verifica que el encabezado Content-Type sea de tipo texto/html
    assert response.headers['Content-Type'].startswith('text/html'), "Content-Type is not text/html"

    # Verifica algún contenido esperado en la página (por ejemplo, un título específico)
    expected_content = '<h1>Welcome to My Website</h1>'
    assert expected_content in response.text, f"Expected content '{expected_content}' not found in response body"

    # Puedes agregar más verificaciones según sea necesario

