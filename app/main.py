from fastapi import FastAPI

app = FastAPI(title="Secure Cloud App")

@app.get("/")
def root():
    return {"message": "Secure Cloud App API is running"}