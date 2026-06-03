from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    AWS_REGION: str = "eu-central-1"
    BEDROCK_MODEL: str = "eu.anthropic.claude-sonnet-4-5-20250929-v1:0"
    ALLOWED_DOMAINS: str = "mhb.de,thesoc.de,mpauli.de"
    SMTP_SERVER: str = "mail.thesoc.de"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    RANSOMWARE_API: str = "https://api.ransomware.live/v1"
    
    class Config:
        env_file = ".env"

settings = Settings()
