import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Fast api"
    PROJECT_VERSION: str = "1.0.0"
    username: str = os.getenv('MONGO_INITDB_ROOT_USERNAME', default='user')
    password: str = os.getenv('MONGO_INITDB_ROOT_PASSWORD', default='699699')

    SECRET_AUTH: str = os.getenv("SECRET_AUTH")
    DATABASE_URL: str = f"mongodb://{username}:{password}@localhost:27017"


settings = Settings()
