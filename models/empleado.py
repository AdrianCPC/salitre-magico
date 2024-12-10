from sqlalchemy import Column, Integer, String, Enum
from database.conexion import Base
import enum

class TipoEmpleado(enum.Enum):
    ADMINISTRATIVO = "Administrativo"
    LOGISTICA = "Logistica"
    PUBLICIDAD = "Publicidad"
    OPERADOR = "Operador"
    MANTENIMIENTO = "Mantenimiento"

class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    tipo_empleado = Column(Enum(TipoEmpleado), nullable=False)
    horario_laboral = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Empleado(nombre={self.nombre}, tipo={self.tipo_empleado.value})>"