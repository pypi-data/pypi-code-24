import logging
import json
import concurrent
from aioclustermanager.k8s.namespace import K8SNamespace
from aioclustermanager.k8s.delete import K8SDelete
from aioclustermanager.k8s.quota import K8SQuota
from aioclustermanager.k8s.job import K8SJob
from aioclustermanager.k8s.tf_job import K8STFJob
from aioclustermanager.k8s.tf_job_list import K8STFJobList
from aioclustermanager.k8s.job_list import K8SJobList
from aioclustermanager.k8s.executions_list import K8SExecutionList

logger = logging.getLogger(__name__)

WATCH_OPS = {
    'namespace': 'https://{endpoint}/api/v1/watch/namespaces/{namespace}',
    'job': 'https://{endpoint}/apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}',  # noqa
    'tfjob':
        'https://{endpoint}/apis/kubeflow.org/v1alpha1/watch/namespaces/{namespace}/tfjobs/{name}'  # noqa
}

GET_OPS = {
    'namespace':
        'https://{endpoint}/api/v1/namespaces/{namespace}',
    'list_jobs':
        'https://{endpoint}/apis/batch/v1/namespaces/{namespace}/jobs',
    'job':
        'https://{endpoint}/apis/batch/v1/namespaces/{namespace}/jobs/{name}/status',  # noqa
    'executions':
        'https://{endpoint}/api/v1/namespaces/{namespace}/pods/?labelSelector=job-name={name}',  # noqa
    'tfjob':
        'https://{endpoint}/apis/kubeflow.org/v1alpha1/namespaces/{namespace}/tfjobs/{name}',  # noqa
    'list_tfjobs':
        'https://{endpoint}/apis/kubeflow.org/v1alpha1/namespaces/{namespace}/tfjobs'  # noqa
}

POST_OPS = {
    'namespace':
        ('https://{endpoint}/api/v1/namespaces', 'v1'),
    'job':
        ('https://{endpoint}/apis/batch/v1/namespaces/{namespace}/jobs', 'batch/v1'),  # noqa
    'tfjob':
        ('https://{endpoint}/apis/kubeflow.org/v1alpha1/namespaces/{namespace}/tfjobs', 'kubeflow.org/v1alpha1'),  # noqa
    'quota':
        ('https://{endpoint}/api/v1/namespaces/{namespace}/resourcequotas', 'v1')  # noqa
}

DELETE_OPS = {
    'namespace':
        ('https://{endpoint}/api/v1/namespaces/{namespace}', 'v1'),
    'job':
        ('https://{endpoint}/apis/batch/v1/namespaces/{namespace}/jobs/{name}', 'batch/v1'),  # noqa
    'tfjob':
        ('https://{endpoint}/apis/kubeflow.org/v1alpha1/namespaces/{namespace}/tfjobs/{name}', 'v1')  # noqa
}


class K8SCaller(object):
    def __init__(self, ssl_context, endpoint, session, verify=True):
        self.ssl_context = ssl_context
        self.endpoint = endpoint
        self.session = session
        self.verify = verify
        self._type = 'k8s'

    @property
    def type(self):
        return self._type

    async def get_namespace(self, namespace):
        url = GET_OPS['namespace']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8SNamespace(data=result)

    async def create_namespace(self, namespace):
        url, version = POST_OPS['namespace']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        obj = K8SNamespace(namespace)
        return await self.post(url, version, obj.payload())

    async def delete_namespace(self, namespace):
        url, version = DELETE_OPS['namespace']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        obj = K8SDelete()
        return await self.delete(url, version, obj.payload())

    async def wait_added(self, kind, namespace, name=None):
        url = WATCH_OPS[kind]
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        return await self.watch(url, value='ADDED')

    async def wait_deleted(self, kind, namespace, name=None):
        url = WATCH_OPS[kind]
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        return await self.watch(url, value='DELETED')

    async def define_quota(self, namespace, cpu_limit=None, mem_limit=None):
        url, version = POST_OPS['quota']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        obj = K8SQuota(
            namespace=namespace,
            max_cpu=cpu_limit,
            max_memory=mem_limit)
        return await self.post(url, version, obj.payload())

    async def get_job(self, namespace, name):
        url = GET_OPS['job']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8SJob(data=result)

    async def get_tfjob(self, namespace, name):
        url = GET_OPS['tfjob']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8STFJob(data=result)

    async def get_job_executions(self, namespace, name):
        url = GET_OPS['executions']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8SExecutionList(data=result)

    async def delete_job(self, namespace, name, wait=False):
        url, version = DELETE_OPS['job']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        obj = K8SDelete()
        await self.delete(url, version, obj.payload())
        if wait:
            return await self.wait_deleted('job', namespace, name)
        return True

    async def delete_tfjob(self, namespace, name, wait=False):
        url, version = DELETE_OPS['tfjob']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        obj = K8SDelete()
        await self.delete(url, version, obj.payload())
        if wait:
            return await self.wait_deleted('tfjob', namespace, name)
        return True

    async def list_jobs(self, namespace):
        url = GET_OPS['list_jobs']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8SJobList(data=result)

    async def list_tfjobs(self, namespace):
        url = GET_OPS['list_tfjobs']
        url = url.format(
            namespace=namespace,
            endpoint=self.endpoint)
        result = await self.get(url)
        if result is None:
            return None
        else:
            return K8STFJobList(data=result)

    async def create_job(
            self, namespace, name, image,
            command=None, args=None,
            cpu_limit=None, mem_limit=None,
            envvars={}):
        url, version = POST_OPS['job']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        obj = K8SJob(
            namespace=namespace,
            name=name,
            image=image,
            command=command, args=args,
            cpu_limit=cpu_limit, mem_limit=mem_limit,
            envvars=envvars)
        return await self.post(url, version, obj.payload())

    async def create_tfjob(
            self, namespace, name, image,
            command=None, args=None,
            cpu_limit=None, mem_limit=None,
            envvars={}, workers=1, ps=1,
            masters=1, tb_gs=None):
        url, version = POST_OPS['tfjob']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        obj = K8STFJob(
            namespace=namespace,
            name=name,
            image=image,
            command=command, args=args,
            cpu_limit=cpu_limit, mem_limit=mem_limit,
            envvars=envvars, workers=workers,
            ps=ps, masters=masters, tb_gs=tb_gs)
        return await self.post(url, version, obj.payload())

    async def wait_for_job(self, namespace, name):
        url = WATCH_OPS['job']
        url = url.format(
            namespace=namespace,
            name=name,
            endpoint=self.endpoint)
        try:
            # We only wait 1 hour
            async for data in self._watch(url, 3660):
                json_data = json.loads(data)
                if 'conditions' not in json_data['object']['status']:
                    continue
                for condition in json_data['object']['status']['conditions']:
                    if condition['type'] == 'Complete':
                        return json_data['object']['status']['succeeded']
        except concurrent.futures._base.TimeoutError:
            return None

    # BASIC OPS

    async def _watch(self, url, timeout=20):
        async with self.session.get(
                url + '?watch=true',
                ssl_context=self.ssl_context,
                verify_ssl=self.verify,
                timeout=timeout) as resp:
            assert resp.status == 200
            while True:
                data, end_of_http = await resp.content.readchunk()
                # print(b'Data: ' + data)
                yield data

    async def watch(self, url, value=None, timeout=20):
        try:
            async for data in self._watch(url, timeout):
                json_data = json.loads(data)
                if json_data['type'] == value:
                    break
        except concurrent.futures._base.TimeoutError:
            pass

    async def get(self, url):
        async with self.session.get(
                url,
                headers={
                    'Accept': 'application/json'
                },
                ssl_context=self.ssl_context,
                verify_ssl=self.verify) as resp:
            if resp.status == 404:
                return None
            if resp.status != 200:
                text = await resp.text()
                print('Error: %d - %s' % (resp.status, text))
            assert resp.status == 200
            return await resp.json()

    async def post(self, url, version, payload):
        payload['apiVersion'] = version
        async with self.session.post(
                url,
                json=payload,
                headers={
                    'Accept': 'application/json'
                },
                ssl_context=self.ssl_context,
                verify_ssl=self.verify) as resp:
            if resp.status in [201, 200]:
                return await resp.json()
            else:
                text = await resp.text()
                logger.error('Error calling k8s: %d - %s' % (resp.status, text))  # noqa
                raise Exception('Error calling k8s')

    async def delete(self, url, version, payload):
        payload['apiVersion'] = version
        async with self.session.delete(
                url,
                headers={
                    'Accept': 'application/json'
                },
                json=payload,
                ssl_context=self.ssl_context,
                verify_ssl=self.verify) as resp:
            if resp.status == 200:
                return await resp.json()
            elif resp.status == 404:
                return None
            elif resp.status == 409:
                return None
            else:
                text = await resp.text()
                logger.error('Error calling k8s: %d - %s' % (resp.status, text))  # noqa
                raise Exception('Error calling k8s')
