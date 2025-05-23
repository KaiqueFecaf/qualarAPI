from pydantic import BaseSettings

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str = "mysql"
    MYSQL_PORT: str = "3306"
    MYSQL_DB: str = "cetesb"
    
    class Config:
        env_file = ".env"

settings = Settings()