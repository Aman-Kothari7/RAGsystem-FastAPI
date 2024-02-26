
from main import agent  
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Ensure you have a 'templates' directory

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form_page.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, query: str = Form(...)):
    response = agent.query(query)
    return templates.TemplateResponse("form_page.html", {"request": request, "response": response.response})

