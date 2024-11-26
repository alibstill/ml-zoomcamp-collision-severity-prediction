from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    ml_model_filename: str = "collision_severity_model_eta=0.3_md=4_mcw=5_nboost=43.bin"
