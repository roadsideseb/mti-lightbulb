import os
import logging

from requests.exceptions import HTTPError

from firebase import firebase
from parse_rest import connection, datatypes

logger = logging.getLogger('benchy.storage')
logging.basicConfig(level=logging.INFO)


class BaseStorageBackend(object):
    test_name = None

    def initialise_storage(self, test_name, **kwargs):
        self.test_name = test_name

    def save_result(self, result, **kwargs):
        pass

    def close_storage(self, **kwargs):
        pass


class FirebaseBackend(BaseStorageBackend):

    def __init__(self, **kwargs):
        self.firebase_url = os.getenv('FIREBASE_URL')
        self.endpoint = 'benchmarks'
        logger.info(
            'using firebase storage backend at {}'.format(self.firebase_url))
        self.firebase = firebase.FirebaseApplication(self.firebase_url, None)

    def save_result(self, result, **kwargs):
        url = '/{}'.format(self.endpoint)
        name = result.test_id.replace('.', '-')
        data = dict(result.serializer(result).data)
        try:
            self.firebase.put(url, name, data=data)
        except HTTPError:
            logger.error(
                'error sending result {} to firebase: {}'.format(
                    name, data))


class FileBackend(BaseStorageBackend):

    def __init__(self, base_dir=None, **kwargs):
        logger.info('using file storage backend')
        self.filename = None
        self.json_handle = None
        self.base_dir = base_dir or os.getcwd()

    def initialise_storage(self, test_name, **kwargs):
        super(FileBackend, self).initialise_storage(test_name)
        self.filename = "{}.json".format(test_name)
        self.json_handle = open(
            os.path.join(self.base_dir, self.filename), 'w')
        self.json_handle.write("[\n")

    def save_result(self, result, **kwargs):
        self.json_handle.write("{}\n".format(result.to_json()))

    def close_storage(self, **kwargs):
        self.json_handle.write(']')
        self.json_handle.close()
        self.json_handle = None

    def __del__(self):
        if self.json_handle:
            self.json_handle.close()
            self.json_handle = None


class Benchmark(datatypes.Object):
    pass


class ParseComBackend(BaseStorageBackend):

    def __init__(self, base_dir=None, **kwargs):
        logger.info('using the parse.com backend')
        connection.register(app_id=os.getenv('PARSECOM_APP_ID'),
                            rest_key=os.getenv('PARSECOM_REST_API_KEY'))

    def save_result(self, result, **kwargs):
        bm = Benchmark(**result.serializer(result).data)
        bm.save()
