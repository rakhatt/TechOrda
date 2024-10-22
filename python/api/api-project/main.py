from fastapi import FastAPI, HTTPException, Header
from typing import Dict, List
from pydantic import BaseModel
import operator

app = FastAPI()
items: List[str] = []
class Item(BaseModel):
    element: str
class Expression(BaseModel):
    expr: str

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/sum1n/{n}")
def sum1n(n: int) -> Dict[str, int]:
    if n < 1:
        return {"result": 0}
    result = sum(range(1, n + 1))
    return {"result": result}
@app.get("/fibo")
def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n должно быть положительным")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        result = b
    return {"result": result}
@app.post("/reverse")
async def reverse_string(string: str = Header(...)):
    reversed_string = string[::-1]  
    return {"result": reversed_string}

@app.put("/list")
async def add_to_list(item: Item):
    items.append(item.element)
    return {"message": "Element added"}
@app.get("/list")
async def get_list():
    return {"result": items}

@app.post("/calculator")
async def calculate(expression: Expression):
    try:
        num1_str, op, num2_str = expression.expr.split(',')
        num1 = float(num1_str)
        num2 = float(num2_str)
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        if op not in ops:
            raise HTTPException(status_code=400, detail={"error": "invalid"})
        result = ops[op](num1, num2)
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": "invalid"})
    except ZeroDivisionError:
        raise HTTPException(status_code=403, detail={"error": "zerodiv"})
