import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    # Base de datos SQLite en el archivo pos.db dentro de la carpeta my_pos_system/backend
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '..', 'pos.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
