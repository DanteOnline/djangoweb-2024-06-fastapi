import pytest
from fastapi import status
from core.models import Base, db_helper


@pytest.mark.asyncio
async def test_crud(client):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
    data = {
            'name': 'New product',
            'price': 100,
        }
    response = client.post('/api/products/', json=data)
    assert response.status_code == status.HTTP_201_CREATED
    response_data = {
            'name': 'New product',
            'price': 100,
            'id': 1,
        }
    assert response.json() == response_data

    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [response_data]
