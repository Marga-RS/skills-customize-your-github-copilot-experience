from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Task API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add a Pydantic model and in-memory task collection.
# TODO: Implement the task routes described in the assignment.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
