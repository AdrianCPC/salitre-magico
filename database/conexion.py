"""
Este modulo configura la conexion a base de datos PostgreSQL usando SQLAlchemy.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# conexión
DATABASE_URL = "postgresql://salitre_admin:root@localhost:5432/salitre_magico"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#