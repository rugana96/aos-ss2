# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.vehiculo import Vehiculo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVehculoController(BaseTestCase):
    """VehculoController integration test stubs"""

    def test_taller_clientid_get(self):
        """Test case for taller_clientid_get

        Obtener los vehículos de un cliente concreto.
        """
        response = self.client.open(
            '/api/v1/vehiculo/clientId/{clientId}'.format(client_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_matricula_get(self):
        """Test case for taller_matricula_get

        Obtener un vehículo concreto a partir de su matrícula
        """
        response = self.client.open(
            '/api/v1/vehiculo/matricula/{matricula}'.format(matricula='matricula_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculo_cget(self):
        """Test case for taller_vehiculo_cget

        Obtener la lista de vehículos.
        """
        response = self.client.open(
            '/api/v1/vehiculo',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculo_options(self):
        """Test case for taller_vehiculo_options

        Proporcionar los métodos HTTP soportados para la lista de vehículos.
        """
        response = self.client.open(
            '/api/v1/vehiculo',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculo_post(self):
        """Test case for taller_vehiculo_post

        Registrar un nuevo vehículo en el taller.
        """
        body = None
        response = self.client.open(
            '/api/v1/vehiculo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculoid_delete(self):
        """Test case for taller_vehiculoid_delete

        Eliminar un vehículo de la lista.
        """
        response = self.client.open(
            '/api/v1/vehiculo/{vehiculoId}'.format(vehiculo_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculoid_get(self):
        """Test case for taller_vehiculoid_get

        Obtener un vehículo concreto.
        """
        response = self.client.open(
            '/api/v1/vehiculo/{vehiculoId}'.format(vehiculo_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculoid_options(self):
        """Test case for taller_vehiculoid_options

        Proporcionar los métodos HTTP soportados para un único vehículo.
        """
        response = self.client.open(
            '/api/v1/vehiculo/{vehiculoId}'.format(vehiculo_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vehiculoid_put(self):
        """Test case for taller_vehiculoid_put

        Modificar un vehículo de la lista.
        """
        body = None
        response = self.client.open(
            '/api/v1/vehiculo/{vehiculoId}'.format(vehiculo_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_taller_vin_get(self):
        """Test case for taller_vin_get

        Obtener el vehículo con un VIN concreto.
        """
        response = self.client.open(
            '/api/v1/vehiculo/VIN/{VIN}'.format(vin='vin_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
