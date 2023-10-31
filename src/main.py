import uvicorn
from fastapi import FastAPI
from controller import commentController
from database import SessionLocal, engine
from model import commentModel
from fastapi.middleware.cors import CORSMiddleware

commentModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
async def root():
    return {"message": "Hello from Video Service"}


app.include_router(prefix="/api", router=commentController.comment)

if __name__ == '__main__':
  uvicorn.run('main:app', reload=True)