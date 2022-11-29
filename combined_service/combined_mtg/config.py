import os

from dotenv import load_dotenv

load_dotenv()

# Configuration Variables
MONGO_HOST: str = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT: int = int(os.environ.get("MONGO_PORT", 27017))
MONGO_TIMEOUT: int = int(os.environ.get("MONGO_TIMEOUT", 3000))
MONGO_USERNAME: str = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD: str = os.environ.get("MONGO_PASSWORD", "pass")
