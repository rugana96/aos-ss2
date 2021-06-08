import connexion
import six
import datetime

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.vehiculo import Vehiculo  # noqa: E501
from swagger_server import util
from flask import make_response

example = [
    {
        'id': 1743,
        'clientId': 28,
        'matricula': '6452-ABC',
        'marca': 'Audi',
        'modelo': 'a7',
        'color': 'Gris',
        'año': 2012,
        'VIN': '3C8FY68B72T322831'
    },
    {
        'id': 5623,
        'clientId': 21,
        'matricula': '1234-JPG',
        'marca': 'Ford',
        'modelo': 'focus',
        'color': 'rojo',
        'año': 2020,
        'VIN': '6J8FY68B72T322831'
    }
]

def taller_clientid_get(client_id):  # noqa: E501
    """Obtener los vehículos de un cliente concreto.

    Permite obtener un vehículo perteneciente a la lista de todos los vehículos de un cliente del taller. # noqa: E501

    :param client_id: ID del cliente.
    :type client_id: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def taller_matricula_get(matricula):  # noqa: E501
    """Obtener un vehículo concreto a partir de su matrícula

    Permite obtener un vehículo perteneciente a la lista de todos los vehículos del taller indicando la matrícula del vehículo. # noqa: E501

    :param matricula: Matrícula del vehículo
    :type matricula: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def taller_vehiculo_cget():  # noqa: E501
    """Obtener la lista de vehículos.

    Permite obtener la lista de todos los vehículos del taller. # noqa: E501


    :rtype: InlineResponse200
    """
    return example


def taller_vehiculo_options():  # noqa: E501
    """Proporcionar los métodos HTTP soportados para la lista de vehículos.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def taller_vehiculo_post(body):  # noqa: E501
    """Registrar un nuevo vehículo en el taller.

    Genera un nuevo vehículo para añadir a la lista de vehículos gestionados por el taller. # noqa: E501

    :param body: &#x60;Vehiculo&#x60; data
    :type body: dict | bytes

    :rtype: Vehiculo
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def taller_vehiculoid_delete(vehiculo_id):  # noqa: E501
    """Eliminar un vehículo de la lista.

    Perimite eliminar un vehículo de la lista de los vehículos gestionados por el taller, utilizando su ID. # noqa: E501

    :param vehiculo_id: ID del vehículo.
    :type vehiculo_id: int

    :rtype: None
    """
    return 'do some magic!'


def taller_vehiculoid_get(vehiculo_id):  # noqa: E501
    """Obtener un vehículo concreto.

    Permite obtener un vehículo perteneciente a la lista de todos los vehículos del taller. # noqa: E501

    :param vehiculo_id: ID del vehículo.
    :type vehiculo_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def taller_vehiculoid_options(vehiculo_id):  # noqa: E501
    """Proporcionar los métodos HTTP soportados para un único vehículo.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados (separados por comas). # noqa: E501

    :param vehiculo_id: ID del vehículo.
    :type vehiculo_id: int

    :rtype: None
    """
    return 'do some magic!'


def taller_vehiculoid_put(body, vehiculo_id):  # noqa: E501
    """Modificar un vehículo de la lista.

    Permite realizar la modificación de los atributos uno de los vehículos gestionados por el taller, seleccionado mediante su ID. # noqa: E501

    :param body: &#x60;Vehiculo&#x60; data
    :type body: dict | bytes
    :param vehiculo_id: ID del vehículo.
    :type vehiculo_id: int

    :rtype: Vehiculo
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def taller_vin_get(vin):  # noqa: E501
    """Obtener el vehículo con un VIN concreto.

    Permite obtener un vehículo según su identificador único. # noqa: E501

    :param vin: Número de identificación del vehículo (Vehicle Identification Number).
    :type vin: str

    :rtype: InlineResponse2002
    """
    return 'do some magic!'
