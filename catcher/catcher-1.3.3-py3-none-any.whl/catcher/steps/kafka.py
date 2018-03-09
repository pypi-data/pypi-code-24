from pykafka import KafkaClient, SimpleConsumer
from pykafka.common import OffsetType

from catcher.steps.check import Operator
from catcher.steps.step import Step
from catcher.utils.file_utils import read_file
from catcher.utils.time_utils import to_seconds
from catcher.utils.misc import try_get_object, fill_template_str


class Kafka(Step):
    def __init__(self, body: dict) -> None:
        super().__init__(body)
        [method] = [k for k in body.keys() if k != 'register']  # produce/consume
        self._method = method.lower()
        conf = body[method]
        self._group_id = conf.get('group_id', 'catcher')
        self._server = conf['server']
        self._topic = conf['topic']
        timeout = conf.get('timeout', {'seconds': 1})
        self._timeout = to_seconds(timeout)
        self._where = conf.get('where', None)
        self._data = None
        if self.method != 'consume':
            self._data = conf.get('data', None)
            if self.data is None:
                self._file = conf['data_from_file']

    @property
    def group_id(self):
        return self._group_id

    @property
    def server(self):
        return self._server

    @property
    def method(self):
        return self._method

    @property
    def topic(self):
        return self._topic

    @property
    def file(self) -> str:
        return self._file

    @property
    def data(self) -> bytes or dict:
        if isinstance(self._data, bytes) or isinstance(self._data, dict):
            return self._data
        return str(self._data).encode('utf-8')

    @property
    def where(self) -> dict or None:
        return self._where

    @property
    def timeout(self) -> int:
        return self._timeout

    def action(self, includes: dict, variables: dict) -> dict:
        client = KafkaClient(hosts=self.server)
        topic = client.topics[fill_template_str(self.topic, variables).encode('utf-8')]
        out = {}
        if self.method == 'consume':
            out = self.consume(topic, variables)
            if out is None:
                raise RuntimeError('No kafka messages were consumed')
        elif self.method == 'produce':
            self.produce(topic, variables)
        else:
            raise AttributeError('unknown method: ' + self.method)
        return self.process_register(variables, out)

    def consume(self, topic, variables: dict) -> dict:
        consumer = topic.get_simple_consumer(consumer_group=self.group_id.encode('utf-8'),
                                             auto_offset_reset=OffsetType.EARLIEST,
                                             reset_offset_on_start=False,
                                             consumer_timeout_ms=self.timeout * 1000)
        if self.where is not None:
            operator = Operator.find_operator(self.where)
        else:
            operator = None
        return Kafka.get_messages(consumer, operator, variables)

    def produce(self, topic, variables):
        message = self.__form_body(variables)
        if not isinstance(message, bytes):
            message = fill_template_str(message, variables).encode('utf-8')
        with topic.get_sync_producer() as producer:
            producer.produce(message)

    def __form_body(self, variables):
        if self.method == 'get':
            return None
        data = None
        if self.data is None:
            data = read_file(fill_template_str(self.file, variables))
        return fill_template_str(data, variables)

    @staticmethod
    def get_messages(consumer: SimpleConsumer, where: Operator or None, variables) -> dict or None:
        message = consumer.consume(True)
        if message is None:
            return None
        variables = dict(variables)
        value = try_get_object(message.value.decode('utf-8'))
        variables['MESSAGE'] = value
        if where is not None:
            if where.operation(variables) is True:
                return value
            else:
                return Kafka.get_messages(consumer, where, variables)
        return value
