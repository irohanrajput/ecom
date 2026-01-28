from fastapi import FastAPI

app = FastAPI(title="ecom")

@app.get("/health")
def health_check():
    return {"status: ok"}