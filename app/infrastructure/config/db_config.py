from pydantic_settings import BaseSettings

class DBSettings(BaseSettings):
    DB_TYPE: str
    USERDB: str
    PASSWORDDB: str
    NAME_SERVICEDB: str
    PORTDB: str
    NAMEDB: str

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DB_TYPE}://{self.USERDB}:{self.PASSWORDDB}@{self.NAME_SERVICEDB}:{self.PORTDB}/{self.NAMEDB}"

    class Config:
        env_file = ".env"
