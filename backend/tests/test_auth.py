from httpx import AsyncClient

async def test_login_sucesso(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_login = await client.post("/login", data={
        "username": "will@email.com",
        "password": "Will123"
    })

    data = response_login.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

async def test_login_senha_errada(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_login = await client.post("/login", data={
        "username": "will@email.com",
        "password": "Will12345"
    })

    assert response_login.status_code == 401

async def test_login_email_inexistente(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_login = await client.post("/login", data={
        "username": "willian@email.com",
        "password": "Will12345"
    })

    assert response_login.status_code == 401