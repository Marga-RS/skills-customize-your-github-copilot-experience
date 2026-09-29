from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import uvicorn


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


app = FastAPI(title="Task API")
tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks(completed: bool | None = None):
    if completed is None:
        return list(tasks.values())
    return [task for task in tasks.values() if task.completed == completed]


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskInput):
    global next_task_id
    task = Task(
        id=next_task_id,
        title=task_input.title,
        completed=task_input.completed,
    )
    tasks[next_task_id] = task
    next_task_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    task = Task(
        id=task_id,
        title=task_input.title,
        completed=task_input.completed,
    )
    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return Response(status_code=204)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
