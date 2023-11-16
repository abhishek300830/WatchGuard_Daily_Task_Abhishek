from fastapi import FastAPI
from src.routes import customer, auth_operations, account
from src.helpers.logger_config import initialize_main_logger

logger = initialize_main_logger(__name__)
logger.info("Starting Application")

app = FastAPI()

app.include_router(account.router)
app.include_router(auth_operations.router)
app.include_router(customer.router)
