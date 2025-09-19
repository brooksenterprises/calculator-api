from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import calculator

app = FastAPI()

# CORS fix
origins = [
    "https://earnings-c38b45.webflow.io",  # Webflow staging domain
    "https://earnings.blueoceantrading.org",
    "http://earnings.blueoceantrading.org"# Your custom domain
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Calculator API is running"}

@app.get("/calc")
def run_calc(ticker: str):
    try:
        result = calculator.main(ticker)
        return {"ticker": ticker, "result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/recommend/{symbol}")
async def recommend(symbol: str):
    try:
        result = calculator.main(symbol)
        return JSONResponse(content=result)
    except Exception as e:
        return {"error": str(e)}


