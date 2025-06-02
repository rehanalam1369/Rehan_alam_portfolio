from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(
    title="Rehan Alam Portfolio",
    description="Portfolio website for Rehan Alam, Data Scientist",
    version="1.0"
)

# Since all files are in the same directory, we'll use that as our templates directory
templates = Jinja2Templates(directory=".")

# Route for homepage
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route for vehicle crash project
@app.get("/vehicle-crash", response_class=HTMLResponse)
async def vehicle_crash(request: Request):
    return templates.TemplateResponse("vehicle-crash.html", {"request": request})

# Route for loan risk project
@app.get("/loan-risk", response_class=HTMLResponse)
async def loan_risk(request: Request):
    return templates.TemplateResponse("loan-risk.html", {"request": request})

# Route for insurance project
@app.get("/insurance", response_class=HTMLResponse)
async def insurance(request: Request):
    return templates.TemplateResponse("insurance.html", {"request": request})

# Route to serve resume
@app.get("/resume")
async def get_resume():
    return FileResponse("RehanAlam_resume.pdf", filename="RehanAlam_Resume.pdf")