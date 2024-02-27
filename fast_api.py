#Necessary imports to serve the RAG system using Fast API
from main import agent  
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

#Defining the simple template to show response
templates = Jinja2Templates(directory="templates")  

#Get request to show input page to user 
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form_page.html", {"request": request, "response": ""})

#Post request to show response to the user and update page 
@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, query: str = Form(...)):
    response = agent.query(query)
    return templates.TemplateResponse("form_page.html", {"request": request, "response": response.response})

