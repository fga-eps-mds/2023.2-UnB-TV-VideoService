import uvicorn
from fastapi import FastAPI
from controller import scheduleController

app = FastAPI()


app.include_router(prefix="/api", router=scheduleController.schedule)

@app.get("/")
async def root():
    return {"message": "Hello from Video Service"}


if __name__ == '__main__':
  uvicorn.run('main:app', reload=True)