from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.conexion import Base
from datetime import datetime

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    
    # relación con cliente
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="tickets")
    
    # relación con atracción
    atraccion_id = Column(Integer, ForeignKey('atracciones.id'))
    atraccion = relationship("Atraccion")
    
    # información del ticket
    fecha_emision = Column(Date, default=datetime.now)
    fecha_uso = Column(Date)
    
    # estado del ticket
    usado = Column(Boolean, default=False)
    valido = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Ticket(cliente={self.cliente.nombre}, atraccion={self.atraccion.nombre})>"