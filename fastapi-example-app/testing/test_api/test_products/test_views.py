from fastapi import status


def test_get_products_status_code(client):
    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK


def test_get_product_by_id(client):
    response = client.get('/api/products/1/')
    assert response.status_code == status.HTTP_200_OK
