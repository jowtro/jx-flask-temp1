import os
from dotenv import load_dotenv

# load env vars from .env
load_dotenv()


TEST = os.getenv("test_var")
