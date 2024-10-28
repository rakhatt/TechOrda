from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест для роута GET /
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# Тест для роута GET /sum1n/{n}
def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

    response = client.get("/sum1n/0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

# Тест для роута GET /fibo
def test_fibo():
    response = client.get("/fibo?n=7")
    assert response.status_code == 200
    assert response.json() == {"result": 13}

    response = client.get("/fibo?n=-1")
    assert response.status_code == 400

# Тест для роута POST /reverse
def test_reverse_string():
    response = client.post("/reverse", headers={"string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

# Тест для роута PUT /list
def test_add_to_list():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"message": "Element added"}

# Тест для роута GET /list
def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

# Тест для роута POST /calculator
def test_calculator():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

    response = client.post("/calculator", json={"expr": "1,/,-1"})
    assert response.status_code == 200
    assert response.json() == {"result": -1.0}

    response = client.post("/calculator", json={"expr": "1,/,-0"})
    assert response.status_code == 403
    assert response.json() == {"detail": {"error": "zerodiv"}}

    response = client.post("/calculator", json={"expr": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": {"error": "invalid"}}

