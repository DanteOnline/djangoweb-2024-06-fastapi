import pytest
from fastapi import status
from core.models import Base, db_helper


@pytest.mark.asyncio
async def test_crud(client):
    # Create new database
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Get all products
    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK
    # Empty now
    assert response.json() == []
    data = {
            'name': 'New product',
            'price': 100,
        }

    # Create new product
    response = client.post('/api/products/', json=data)
    assert response.status_code == status.HTTP_201_CREATED
    response_data = {
            'name': 'New product',
            'price': 100,
            'id': 1,
        }
    # Return new product
    assert response.json() == response_data

    # Get all products
    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK

    # Get one new product in list
    assert response.json() == [response_data]

    updated_data = {
        'name': 'Very new product',
        'price': 200,
    }
    # Update (PUT) product
    response = client.put('/api/products/1/', json=updated_data)

    assert response.status_code == status.HTTP_200_OK

    partial_update_data = {
        'price': 300,
    }

    # Update (Patch) product
    response = client.patch('/api/products/1/', json=partial_update_data)

    assert response.status_code == status.HTTP_200_OK

    # Get one product by id and check

    response = client.get('/api/products/1/')

    assert response.status_code == status.HTTP_200_OK

    expected_data = {
        'id': 1,
        'name': 'Very new product',
        'price': 300,
    }

    assert response.json() == expected_data

    # Delete product

    response = client.delete('/api/products/1')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get all products is empty

    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK
    # Empty now
    assert response.json() == []
