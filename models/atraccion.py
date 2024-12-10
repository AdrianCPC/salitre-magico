from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from database.conexion import Base

class Atraccion(Base):
    __tablename__ = 'atracciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    
    # condiciones para usar atraccion
    altura_minima = Column(Float, nullable=False)
    altura_maxima = Column(Float)
    
    # clasificación
    clasificacion = Column(String, nullable=False)
    
    # estado de la atracción
    disponible = Column(Boolean, default=True)
    
    # metricas de uso
    total_visitantes = Column(Integer, default=0)
    
    def verificar_acceso(self, altura_cliente):
        """
        Verifica si un cliente puede acceder a la atraccion
        """
        if not self.disponible:
            return False
        
        if altura_cliente < self.altura_minima:
            return False
        
        if self.altura_maxima and altura_cliente > self.altura_maxima:
            return False
        
        return True
    
    def __repr__(self):
        return f"<Atraccion(nombre={self.nombre}, clasificacion={self.clasificacion})>"