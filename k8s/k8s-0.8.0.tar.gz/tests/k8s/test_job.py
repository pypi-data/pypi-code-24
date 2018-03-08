#!/usr/bin/env python
# -*- coding: utf-8

import pytest
import mock

from k8s.client import NotFound
from k8s.models.common import ObjectMeta
from k8s.models.job import Job, JobSpec
from k8s.models.pod import Container, LocalObjectReference, PodTemplateSpec, PodSpec

NAME = "my-name"
NAMESPACE = "my-namespace"


@pytest.mark.usefixtures("k8s_config")
class TestJobs(object):
    def test_create_blank_job(self):
        object_meta = ObjectMeta(name=NAME, namespace=NAMESPACE)
        job = Job(metadata=object_meta)
        assert job.as_dict()[u"metadata"][u"name"] == NAME

    def test_created_if_not_exists(self, post, api_get):
        api_get.side_effect = NotFound()
        job = _create_default_job()
        call_params = job.as_dict()

        assert job._new
        job.save()
        assert not job._new

        pytest.helpers.assert_any_call(post, _uri(NAMESPACE), call_params)


def _create_default_job():
    labels = {"test": "true"}
    object_meta = ObjectMeta(name=NAME, namespace=NAMESPACE, labels=labels)
    container = Container(
        name="container",
        image="dummy_image"
    )
    image_pull_secret = LocalObjectReference(name="image_pull_secret")
    pod_spec = PodSpec(containers=[container], imagePullSecrets=[image_pull_secret], serviceAccountName="default",
                       restartPolicy="Never")
    pod_template_spec = PodTemplateSpec(metadata=object_meta, spec=pod_spec)
    job_spec = JobSpec(template=pod_template_spec)
    job = Job(metadata=object_meta, spec=job_spec)

    return job


def _create_mock_response():
    mock_response = mock.Mock()
    mock_response.json.return_value = {
        u"metadata": {
            u"labels": {
                u"test": u"true"
            },
            u"namespace": u"my-namespace",
            u"name": u"my-name"
        },
        u"spec": {
            u"template": {
                u"spec": {
                    u"serviceAccountName": u"default",
                    u"restartPolicy": u"Never",
                    u"volumes": [],
                    u"imagePullSecrets": [
                        {
                            u"name": u"image_pull_secret"
                        }
                    ],
                    u"containers": [
                        {
                            u"name": u"container",
                            u"image": u"dummy_image",
                            u"volumeMounts": [],
                            u"env": [],
                            u"imagePullPolicy": u"IfNotPresent",
                        }
                    ]
                },
                u"metadata": {
                    u"labels": {
                        u"test": u"true"
                    },
                    u"namespace": u"my-namespace",
                    u"name": u"my-name"
                }
            }
        }
    }
    return mock_response


def _uri(namespace, name=""):
    return "/apis/batch/v1/namespaces/{namespace}/jobs".format(name=name, namespace=namespace)
