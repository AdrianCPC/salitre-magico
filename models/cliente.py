from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.conexion import Base
from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    telefono = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False)
    estatura = Column(Float, nullable=False)
    edad = Column(Integer, nullable=False)
    
    # contacto para menores
    contacto_familiar_nombre = Column(String)
    contacto_familiar_telefono = Column(String)
    
    # zona de seguimiento
    fecha_registro = Column(Date, default=datetime.now)
    frecuencia_visitas = Column(Integer, default=0)
    
    # zona de marketing
    permite_publicidad = Column(Boolean, default=False)
    
    # relaciones
    tickets = relationship("Ticket", back_populates="cliente")
    
    def __repr__(self):
        return f"<Cliente(nombre={self.nombre}, edad={self.edad})>"