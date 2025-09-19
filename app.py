from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import calculator  # your calculator.py

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API is running"}

@app.get("/calc")
def run_calc(ticker: str):
    try:
        result = calculator.main(ticker)  # if you have calculator.main()
        return {"success": True, "ticker": ticker, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/recommend/{symbol}")
def recommend(symbol: str):
    try:
        result = calculator.compute_recommendation(symbol)  # no await
        return JSONResponse(content=result)
    except Exception as e:
        return {"error": str(e)}

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
