# api-progect



- [Postman.com](https://www.postman.com/)
- [Postman API testing](https://www.postman.com/automated-testing/)
- [FastAPI туториал](https://fastapi.tiangolo.com/tutorial/)


#### 1. Устанвока и запуск проекта 

###Сначала склонируйте репозиторий на вашу локальную машину:
git clone git@github.com:rakhatt/TechOrda.git
#### Создание виртуального окружения

```bash
python3 -m venv .venv
```

### Активируйте виртуальное окружение:
```bash
source .venv/bin/activate
```

### Установка зависимостей:
```bash
pip install -r requirements.txt
```
###  Запуск приложения:
```bash
uvicorn main:app --reload
```
## Устанвоите зависимости бля теста 
```bash
apt install snapd
snap install postman
pip install pytest
pip install httpx
```

### Запуск теста 
```bash
pytest
```

### Результат долженбыть 
==================================================================== test session starts =====================================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/rakhat/TechOrda/TechOrda/python/api/api-project
plugins: anyio-4.6.2.post1
collected 7 items

test_main.py .......                                                                                                                                   [100%]

===================================================================== 7 passed in 0.64s ======================================================================

### 
```bash
newman run test.json
```

