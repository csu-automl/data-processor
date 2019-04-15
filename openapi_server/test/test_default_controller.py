# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sample_body import SampleBody  # noqa: E501
from openapi_server.models.sample_response import SampleResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_sample_datasource(self):
        """Test case for sample_datasource

        Выполняет предварительный анализ данных на куске файла
        """
        sample_body = {
  "file" : "file",
  "delimiter" : "delimiter"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/sample',
            method='POST',
            headers=headers,
            data=json.dumps(sample_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
