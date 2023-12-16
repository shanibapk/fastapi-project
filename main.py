from fastapi import fastapi


app= FastAPI()

@app.get('/')
def index():
    return 'heyy'

  
