from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://test.com",
    "http://test.com:80",
    "http://test.com:3000",
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/calculator")
async def get_multiplication_table(number: int = Query(..., description="구구단을 위한 숫자를 입력하세요")):
    result = [f"{number} x {i} = {number * i}" for i in range(1, 10)]
    
    return {"result": result}


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True, log_level="debug")
