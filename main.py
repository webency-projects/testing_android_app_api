from app.factory import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=5000)
