from fastapi import FastAPI
import uvicorn
import calculator  # this is your calculator.py file

app = FastAPI()

@app.get("/calc")
def run_calc(ticker: str):
    try:
        # IMPORTANT: you need a function inside calculator.py
        # Example: def main(ticker): return {...}
        result = calculator.main(ticker)
        return {"success": True, "ticker": ticker, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI
from fastapi.responses import JSONResponse
import calculator  # your calculator.py

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API is running"}

@app.get("/recommend/{symbol}")
async def recommend(symbol: str):
    try:
        result = await calculator.compute_recommendation(symbol)
        return JSONResponse(content=result)
    except Exception as e:
        return {"error": str(e)}


