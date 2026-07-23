import os
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "ClientPulse QA - Executive Testing Platform"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    CLIENT_NAME: str = "Acme Corp Enterprise Client"
    TARGET_SYSTEM_NAME: str = "E-Commerce & Payment API Suite"
    REPORT_OUTPUT_DIR: str = os.path.join(os.path.dirname(__file__), "reports")

settings = Settings()
os.makedirs(settings.REPORT_OUTPUT_DIR, exist_ok=True)
