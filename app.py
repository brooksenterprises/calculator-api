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
        # Prefer calculator.main() if it returns structured JSON
        result = calculator.main(ticker)
        return JSONResponse(content={"ticker": ticker, "result": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
