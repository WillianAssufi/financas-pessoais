from httpx import AsyncClient

async def test_criar_usuario(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })

    data = response.json()

    assert response.status_code == 201
    assert data["nome"] == "Willian" 
    assert data["email"] == "will@email.com"
    assert "senha" not in data
    assert "id" in data

async def test_criar_usuario_email_duplicado(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_duplicate = await client.post("/usuarios/", json={
        "nome": "Willian Assufi", 
        "email": "will@email.com",
        "senha": "Will123456"
        })

    assert response_duplicate.status_code == 409
    assert response_duplicate.json()["detail"] == "Email já cadastrado"

async def test_listar_usuarios(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_list = await client.get("/usuarios/")
    data = response_list.json()

    assert response_list.status_code == 200
    assert len(data) == 1
    assert data[0]["email"] == "will@email.com"