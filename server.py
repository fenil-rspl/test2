from fastapi import FastAPI
from routes import index, auth, users, api, files

app = FastAPI()

app.include_router(index.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(api.router)
app.include_router(files.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)