from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import os

from config import settings
from test_runner import test_engine
from report_generator import generate_client_html_report

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Client-Focused QA Automation & Executive Reporting Platform"
)

static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def get_index():
    index_file = os.path.join(static_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return HTMLResponse("<h1>ClientPulse QA Dashboard Running</h1>")

@app.get("/api/summary")
async def get_summary():
    return {
        "status": "success",
        "client_name": settings.CLIENT_NAME,
        "target_system": settings.TARGET_SYSTEM_NAME,
        "metrics": test_engine.latest_summary
    }

@app.post("/api/run-tests")
async def run_test_suite():
    summary = test_engine.run_tests()
    return {
        "message": "Test suite executed successfully",
        "timestamp": test_engine.last_run_time,
        "summary": summary
    }

@app.get("/api/report/html", response_class=HTMLResponse)
async def get_html_report():
    html_content = generate_client_html_report(test_engine.latest_summary, settings.CLIENT_NAME)
    return HTMLResponse(content=html_content)

@app.get("/health")
async def health_check():
    return {"status": "HEALTHY", "app": settings.APP_NAME, "version": settings.VERSION}
