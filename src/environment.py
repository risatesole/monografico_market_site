import os
from dotenv import load_dotenv

# Load .env file (from project root)
load_dotenv()

class environment:
    PLATFORM_NAME = os.environ.get('PLATFORM_NAME', 'Default Value')

env = environment()