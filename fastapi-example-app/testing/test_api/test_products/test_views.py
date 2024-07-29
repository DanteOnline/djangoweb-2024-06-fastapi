from fastapi import status


def test_get_products_status_code(client):
    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK


def test_get_products_empty_db(client):
    response = client.get('/api/products/')
    assert response.json() == []


def test_create_product_status_code(client):
    data = {
        'name': 'New product',
        'price': 100,
    }
    response = client.post('/api/products/', json=data)
    assert response.status_code == status.HTTP_201_CREATED


def test_create_product_response(client):
    data = {
        'name': 'New product',
        'price': 100,
    }
    response = client.post('/api/products/', json=data)
    response_data = {
        'name': 'New product',
        'price': 100,
        'id': 1,
    }

    assert response.json() == response_data


def test_get_product_by_id(client):
    response = client.get('/api/products/1/')
    assert response.status_code == status.HTTP_200_OK
