import uvicorn, sys
from fastapi import FastAPI
from controller import scheduleController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(prefix="/api", router=scheduleController.schedule)

@app.get("/")
async def root():
    return {"message": "Hello from Video Service"}

if __name__ == '__main__':
  port = 8081
  if (len(sys.argv) == 2):
    port = sys.argv[1]

  uvicorn.run('main:app', reload=True, port=int(port), host="0.0.0.0")