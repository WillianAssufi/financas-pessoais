from httpx import AsyncClient

async def test_criar_transacao(client: AsyncClient):
    response = await client.post("/usuarios/", json={
        "nome": "Willian", 
        "email": "will@email.com",
        "senha": "Will123"
        })
    
    response_login = await client.post("/login", data={
        "username": "will@email.com",
        "password": "Will123"
    })

    token = response_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response_create_categoria = await client.post("/categorias/", json={
        "usuario_id": 1,
        "nome": "Compra",
        "cor": "#FFFFFF"
    }, headers=headers)

    response_create_transacao = await client.post("/transacoes/", json={
        "categoria_id": response_create_categoria.json()["id"],
        "descricao": "Mercado",
        "valor": "2500.00",
        "tipo": "despesa",
        "data": "2026-07-06"
    }, headers=headers)

    data = response_create_transacao.json()

    assert response_create_transacao.status_code == 201
    assert data["descricao"] == "Mercado"
    assert data["valor"] == "2500.00"
    assert data["tipo"] == "despesa"
    assert data["data"] == "2026-07-06"
    assert data["categoria_id"] == 1
    assert data["usuario_id"] == 1

async def test_criar_transacao_sem_token(client: AsyncClient):
    response = await client.post("/transacoes/", json={
        "categoria_id": 1,
        "descricao": "Mercado",
        "valor": "2500.00",
        "tipo": "despesa",
        "data": "2026-07-06"
    })

    assert response.status_code == 401

async def test_listar_transacoes_so_do_usuario_logado(client: AsyncClient):
    response_user_um = await client.post("/usuarios/", json={
        "nome": "Will",
        "email": "will@email.com",
        "senha": "Will123"
    })

    response_user_dois = await client.post("/usuarios/", json={
        "nome": "Willian",
        "email": "willian@email.com",
        "senha": "Will123"
    })

    response_login_user_um = await client.post("/login", data={
        "username": "will@email.com",
        "password": "Will123"
    })

    token_um = response_login_user_um.json()["access_token"]
    headers_um = {"Authorization": f"Bearer {token_um}"}
    
    response_create_categoria = await client.post("/categorias/", json={
        "usuario_id": 1,
        "nome": "Gastos",
        "cor": "#FFFFFF"
    }, headers=headers_um)

    response_create_transacao = await client.post("/transacoes/", json={
        "categoria_id": response_create_categoria.json()["id"],
        "descricao": "Mercado",
        "valor": "2500.00",
        "tipo": "despesa",
        "data": "2026-07-06"
    }, headers=headers_um)

    response_login_user_dois = await client.post("/login", data={
        "username": "willian@email.com",
        "password": "Will123"
    })

    token_dois = response_login_user_dois.json()["access_token"]
    headers_dois = {"Authorization": f"Bearer {token_dois}"}

    response_list_transacoes = await client.get("/transacoes/", headers=headers_dois)
    data = response_list_transacoes.json()

    assert len(data) == 0