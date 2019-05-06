from openapi_server.services import storage_service

class DatasourceService(object):
    def sample(self, sample_request):
        result = storage_service.get_file_content(sample_request.file, 10240)
        print("Service: {}".format(result))
        return 1
