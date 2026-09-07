from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Python Tutor API"}


@app.get("/api/health")
def health():
    return {"status": "ok"}
