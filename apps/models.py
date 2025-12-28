# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Vendedor(db.Model):

    __tablename__ = 'Vendedor'

    id = db.Column(db.Integer, primary_key=True)

    #__Vendedor_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    nombre = db.Column(db.String(255),  nullable=True)
    apellido = db.Column(db.String(255),  nullable=True)
    celular = db.Column(db.String(255),  nullable=True)

    #__Vendedor_FIELDS__END

    def __init__(self, **kwargs):
        super(Vendedor, self).__init__(**kwargs)


class Provincia(db.Model):

    __tablename__ = 'Provincia'

    id = db.Column(db.Integer, primary_key=True)

    #__Provincia_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    nombre = db.Column(db.String(255),  nullable=True)

    #__Provincia_FIELDS__END

    def __init__(self, **kwargs):
        super(Provincia, self).__init__(**kwargs)


class Localidad(db.Model):

    __tablename__ = 'Localidad'

    id = db.Column(db.Integer, primary_key=True)

    #__Localidad_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    id_provincia = db.Column(db.Integer, nullable=True)

    #__Localidad_FIELDS__END

    def __init__(self, **kwargs):
        super(Localidad, self).__init__(**kwargs)


class Domicilio(db.Model):

    __tablename__ = 'Domicilio'

    id = db.Column(db.Integer, primary_key=True)

    #__Domicilio_FIELDS__
    calle = db.Column(db.String(255),  nullable=True)
    id = db.Column(db.Integer, nullable=True)
    numero = db.Column(db.String(255),  nullable=True)
    id_localidad = db.Column(db.Integer, nullable=True)
    coord_gps = db.Column(db.String(255),  nullable=True)

    #__Domicilio_FIELDS__END

    def __init__(self, **kwargs):
        super(Domicilio, self).__init__(**kwargs)


class Tipocliente(db.Model):

    __tablename__ = 'Tipocliente'

    id = db.Column(db.Integer, primary_key=True)

    #__Tipocliente_FIELDS__
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Tipocliente_FIELDS__END

    def __init__(self, **kwargs):
        super(Tipocliente, self).__init__(**kwargs)


class Cliente(db.Model):

    __tablename__ = 'Cliente'

    id = db.Column(db.Integer, primary_key=True)

    #__Cliente_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    id_tipo = db.Column(db.Integer, nullable=True)
    celular = db.Column(db.String(255),  nullable=True)
    id_domicilio = db.Column(db.Integer, nullable=True)

    #__Cliente_FIELDS__END

    def __init__(self, **kwargs):
        super(Cliente, self).__init__(**kwargs)


class Chofer(db.Model):

    __tablename__ = 'Chofer'

    id = db.Column(db.Integer, primary_key=True)

    #__Chofer_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    apellido = db.Column(db.String(255),  nullable=True)
    celular = db.Column(db.String(255),  nullable=True)

    #__Chofer_FIELDS__END

    def __init__(self, **kwargs):
        super(Chofer, self).__init__(**kwargs)


class Vehiculo(db.Model):

    __tablename__ = 'Vehiculo'

    id = db.Column(db.Integer, primary_key=True)

    #__Vehiculo_FIELDS__
    modelo = db.Column(db.String(255),  nullable=True)

    #__Vehiculo_FIELDS__END

    def __init__(self, **kwargs):
        super(Vehiculo, self).__init__(**kwargs)


class Producto(db.Model):

    __tablename__ = 'Producto'

    id = db.Column(db.Integer, primary_key=True)

    #__Producto_FIELDS__
    descripcion = db.Column(db.String(255),  nullable=True)

    #__Producto_FIELDS__END

    def __init__(self, **kwargs):
        super(Producto, self).__init__(**kwargs)


class Estado(db.Model):

    __tablename__ = 'Estado'

    id = db.Column(db.Integer, primary_key=True)

    #__Estado_FIELDS__
    ambito = db.Column(db.String(255),  nullable=True)
    color = db.Column(db.String(255),  nullable=True)
    is_final = db.Column(db.Boolean, nullable=True)

    #__Estado_FIELDS__END

    def __init__(self, **kwargs):
        super(Estado, self).__init__(**kwargs)


class Viaje(db.Model):

    __tablename__ = 'Viaje'

    id = db.Column(db.Integer, primary_key=True)

    #__Viaje_FIELDS__
    fecha_viaje = db.Column(db.String(255),  nullable=True)
    notas = db.Column(db.String(255),  nullable=True)
    id_chofer = db.Column(db.Integer, nullable=True)
    id_vehiculo = db.Column(db.Integer, nullable=True)
    id_estado = db.Column(db.Integer, nullable=True)

    #__Viaje_FIELDS__END

    def __init__(self, **kwargs):
        super(Viaje, self).__init__(**kwargs)


class Pedido(db.Model):

    __tablename__ = 'Pedido'

    id = db.Column(db.Integer, primary_key=True)

    #__Pedido_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    comentarios = db.Column(db.Text, nullable=True)
    lugar_entrega = db.Column(db.String(255),  nullable=True)
    id_cliente = db.Column(db.Integer, nullable=True)
    id_vendedor = db.Column(db.Integer, nullable=True)
    id_viaje = db.Column(db.Integer, nullable=True)
    id_estado = db.Column(db.Integer, nullable=True)

    #__Pedido_FIELDS__END

    def __init__(self, **kwargs):
        super(Pedido, self).__init__(**kwargs)


class Itemspedido(db.Model):

    __tablename__ = 'Itemspedido'

    id = db.Column(db.Integer, primary_key=True)

    #__Itemspedido_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    cantidad = db.Column(db.Integer, nullable=True)
    unidad = db.Column(db.String(255),  nullable=True)
    id_pedido = db.Column(db.Integer, nullable=True)
    id_producto = db.Column(db.Integer, nullable=True)

    #__Itemspedido_FIELDS__END

    def __init__(self, **kwargs):
        super(Itemspedido, self).__init__(**kwargs)



#__MODELS__END
