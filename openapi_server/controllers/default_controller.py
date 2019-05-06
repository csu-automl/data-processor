import connexion
import six

from openapi_server.models.sample_body import SampleBody  # noqa: E501
from openapi_server.models.sample_response import SampleResponse  # noqa: E501
from openapi_server.services import datasource_service
from openapi_server import util

def sample_datasource(sample_body=None):  # noqa: E501
    """Выполняет предварительный анализ данных на куске файла

     # noqa: E501

    :param sample_body:
    :type sample_body: dict | bytes

    :rtype: SampleResponse
    """
    if connexion.request.is_json:
        sample_body = SampleBody.from_dict(connexion.request.get_json())  # noqa: E501
        print("Controller: {}".format(sample_body))
        datasource_service.sample(sample_body)
    return 'do some magic!'
