from __future__ import unicode_literals
from nose.tools import assert_raises

import itertools

import boto
import boto3
from boto.exception import EC2ResponseError
from boto.ec2.instance import Reservation
import sure  # noqa

from moto import mock_ec2_deprecated, mock_ec2
from nose.tools import assert_raises


@mock_ec2_deprecated
def test_add_tag():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]

    with assert_raises(EC2ResponseError) as ex:
        instance.add_tag("a key", "some value", dry_run=True)
    ex.exception.error_code.should.equal('DryRunOperation')
    ex.exception.status.should.equal(400)
    ex.exception.message.should.equal(
        'An error occurred (DryRunOperation) when calling the CreateTags operation: Request would have succeeded, but DryRun flag is set')

    instance.add_tag("a key", "some value")
    chain = itertools.chain.from_iterable
    existing_instances = list(
        chain([res.instances for res in conn.get_all_instances()]))
    existing_instances.should.have.length_of(1)
    existing_instance = existing_instances[0]
    existing_instance.tags["a key"].should.equal("some value")


@mock_ec2_deprecated
def test_remove_tag():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]

    instance.add_tag("a key", "some value")

    tags = conn.get_all_tags()
    tag = tags[0]
    tag.name.should.equal("a key")
    tag.value.should.equal("some value")

    with assert_raises(EC2ResponseError) as ex:
        instance.remove_tag("a key", dry_run=True)
    ex.exception.error_code.should.equal('DryRunOperation')
    ex.exception.status.should.equal(400)
    ex.exception.message.should.equal(
        'An error occurred (DryRunOperation) when calling the DeleteTags operation: Request would have succeeded, but DryRun flag is set')

    instance.remove_tag("a key")
    conn.get_all_tags().should.have.length_of(0)

    instance.add_tag("a key", "some value")
    conn.get_all_tags().should.have.length_of(1)
    instance.remove_tag("a key", "some value")


@mock_ec2_deprecated
def test_get_all_tags():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]

    instance.add_tag("a key", "some value")

    tags = conn.get_all_tags()
    tag = tags[0]
    tag.name.should.equal("a key")
    tag.value.should.equal("some value")


@mock_ec2_deprecated
def test_get_all_tags_with_special_characters():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]

    instance.add_tag("a key", "some<> value")

    tags = conn.get_all_tags()
    tag = tags[0]
    tag.name.should.equal("a key")
    tag.value.should.equal("some<> value")


@mock_ec2_deprecated
def test_create_tags():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    tag_dict = {'a key': 'some value',
                'another key': 'some other value',
                'blank key': ''}

    with assert_raises(EC2ResponseError) as ex:
        conn.create_tags(instance.id, tag_dict, dry_run=True)
    ex.exception.error_code.should.equal('DryRunOperation')
    ex.exception.status.should.equal(400)
    ex.exception.message.should.equal(
        'An error occurred (DryRunOperation) when calling the CreateTags operation: Request would have succeeded, but DryRun flag is set')

    conn.create_tags(instance.id, tag_dict)
    tags = conn.get_all_tags()
    set([key for key in tag_dict]).should.equal(
        set([tag.name for tag in tags]))
    set([tag_dict[key] for key in tag_dict]).should.equal(
        set([tag.value for tag in tags]))


@mock_ec2_deprecated
def test_tag_limit_exceeded():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    tag_dict = {}
    for i in range(51):
        tag_dict['{0:02d}'.format(i + 1)] = ''

    with assert_raises(EC2ResponseError) as cm:
        conn.create_tags(instance.id, tag_dict)
    cm.exception.code.should.equal('TagLimitExceeded')
    cm.exception.status.should.equal(400)
    cm.exception.request_id.should_not.be.none

    instance.add_tag("a key", "a value")
    with assert_raises(EC2ResponseError) as cm:
        conn.create_tags(instance.id, tag_dict)
    cm.exception.code.should.equal('TagLimitExceeded')
    cm.exception.status.should.equal(400)
    cm.exception.request_id.should_not.be.none

    tags = conn.get_all_tags()
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.name.should.equal("a key")
    tag.value.should.equal("a value")


@mock_ec2_deprecated
def test_invalid_parameter_tag_null():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]

    with assert_raises(EC2ResponseError) as cm:
        instance.add_tag("a key", None)
    cm.exception.code.should.equal('InvalidParameterValue')
    cm.exception.status.should.equal(400)
    cm.exception.request_id.should_not.be.none


@mock_ec2_deprecated
def test_invalid_id():
    conn = boto.connect_ec2('the_key', 'the_secret')
    with assert_raises(EC2ResponseError) as cm:
        conn.create_tags('ami-blah', {'key': 'tag'})
    cm.exception.code.should.equal('InvalidID')
    cm.exception.status.should.equal(400)
    cm.exception.request_id.should_not.be.none

    with assert_raises(EC2ResponseError) as cm:
        conn.create_tags('blah-blah', {'key': 'tag'})
    cm.exception.code.should.equal('InvalidID')
    cm.exception.status.should.equal(400)
    cm.exception.request_id.should_not.be.none


@mock_ec2_deprecated
def test_get_all_tags_resource_id_filter():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    instance.add_tag("an instance key", "some value")
    image_id = conn.create_image(instance.id, "test-ami", "this is a test ami")
    image = conn.get_image(image_id)
    image.add_tag("an image key", "some value")

    tags = conn.get_all_tags(filters={'resource-id': instance.id})
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.res_id.should.equal(instance.id)
    tag.res_type.should.equal('instance')
    tag.name.should.equal("an instance key")
    tag.value.should.equal("some value")

    tags = conn.get_all_tags(filters={'resource-id': image_id})
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.res_id.should.equal(image_id)
    tag.res_type.should.equal('image')
    tag.name.should.equal("an image key")
    tag.value.should.equal("some value")


@mock_ec2_deprecated
def test_get_all_tags_resource_type_filter():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    instance.add_tag("an instance key", "some value")
    image_id = conn.create_image(instance.id, "test-ami", "this is a test ami")
    image = conn.get_image(image_id)
    image.add_tag("an image key", "some value")

    tags = conn.get_all_tags(filters={'resource-type': 'instance'})
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.res_id.should.equal(instance.id)
    tag.res_type.should.equal('instance')
    tag.name.should.equal("an instance key")
    tag.value.should.equal("some value")

    tags = conn.get_all_tags(filters={'resource-type': 'image'})
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.res_id.should.equal(image_id)
    tag.res_type.should.equal('image')
    tag.name.should.equal("an image key")
    tag.value.should.equal("some value")


@mock_ec2_deprecated
def test_get_all_tags_key_filter():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    instance.add_tag("an instance key", "some value")
    image_id = conn.create_image(instance.id, "test-ami", "this is a test ami")
    image = conn.get_image(image_id)
    image.add_tag("an image key", "some value")

    tags = conn.get_all_tags(filters={'key': 'an instance key'})
    tag = tags[0]
    tags.should.have.length_of(1)
    tag.res_id.should.equal(instance.id)
    tag.res_type.should.equal('instance')
    tag.name.should.equal("an instance key")
    tag.value.should.equal("some value")


@mock_ec2_deprecated
def test_get_all_tags_value_filter():
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance = reservation.instances[0]
    instance.add_tag("an instance key", "some value")
    reservation_b = conn.run_instances('ami-1234abcd')
    instance_b = reservation_b.instances[0]
    instance_b.add_tag("an instance key", "some other value")
    reservation_c = conn.run_instances('ami-1234abcd')
    instance_c = reservation_c.instances[0]
    instance_c.add_tag("an instance key", "other value*")
    reservation_d = conn.run_instances('ami-1234abcd')
    instance_d = reservation_d.instances[0]
    instance_d.add_tag("an instance key", "other value**")
    reservation_e = conn.run_instances('ami-1234abcd')
    instance_e = reservation_e.instances[0]
    instance_e.add_tag("an instance key", "other value*?")
    image_id = conn.create_image(instance.id, "test-ami", "this is a test ami")
    image = conn.get_image(image_id)
    image.add_tag("an image key", "some value")

    tags = conn.get_all_tags(filters={'value': 'some value'})
    tags.should.have.length_of(2)

    tags = conn.get_all_tags(filters={'value': 'some*value'})
    tags.should.have.length_of(3)

    tags = conn.get_all_tags(filters={'value': '*some*value'})
    tags.should.have.length_of(3)

    tags = conn.get_all_tags(filters={'value': '*some*value*'})
    tags.should.have.length_of(3)

    tags = conn.get_all_tags(filters={'value': '*value\*'})
    tags.should.have.length_of(1)

    tags = conn.get_all_tags(filters={'value': '*value\*\*'})
    tags.should.have.length_of(1)

    tags = conn.get_all_tags(filters={'value': '*value\*\?'})
    tags.should.have.length_of(1)


@mock_ec2_deprecated
def test_retrieved_instances_must_contain_their_tags():
    tag_key = 'Tag name'
    tag_value = 'Tag value'
    tags_to_be_set = {tag_key: tag_value}

    conn = boto.connect_ec2('the_key', 'the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    reservation.should.be.a(Reservation)
    reservation.instances.should.have.length_of(1)
    instance = reservation.instances[0]

    reservations = conn.get_all_instances()
    reservations.should.have.length_of(1)
    reservations[0].id.should.equal(reservation.id)
    instances = reservations[0].instances
    instances.should.have.length_of(1)
    instances[0].id.should.equal(instance.id)

    conn.create_tags([instance.id], tags_to_be_set)
    reservations = conn.get_all_instances()
    instance = reservations[0].instances[0]
    retrieved_tags = instance.tags

    # Cleanup of instance
    conn.terminate_instances([instances[0].id])

    # Check whether tag is present with correct value
    retrieved_tags[tag_key].should.equal(tag_value)


@mock_ec2_deprecated
def test_retrieved_volumes_must_contain_their_tags():
    tag_key = 'Tag name'
    tag_value = 'Tag value'
    tags_to_be_set = {tag_key: tag_value}
    conn = boto.connect_ec2('the_key', 'the_secret')
    volume = conn.create_volume(80, "us-east-1a")

    all_volumes = conn.get_all_volumes()
    volume = all_volumes[0]
    conn.create_tags([volume.id], tags_to_be_set)

    # Fetch the volume again
    all_volumes = conn.get_all_volumes()
    volume = all_volumes[0]
    retrieved_tags = volume.tags

    volume.delete()

    # Check whether tag is present with correct value
    retrieved_tags[tag_key].should.equal(tag_value)


@mock_ec2_deprecated
def test_retrieved_snapshots_must_contain_their_tags():
    tag_key = 'Tag name'
    tag_value = 'Tag value'
    tags_to_be_set = {tag_key: tag_value}
    conn = boto.connect_ec2(aws_access_key_id='the_key',
                            aws_secret_access_key='the_secret')
    volume = conn.create_volume(80, "eu-west-1a")
    snapshot = conn.create_snapshot(volume.id)
    conn.create_tags([snapshot.id], tags_to_be_set)

    # Fetch the snapshot again
    all_snapshots = conn.get_all_snapshots()
    snapshot = [item for item in all_snapshots if item.id == snapshot.id][0]
    retrieved_tags = snapshot.tags

    conn.delete_snapshot(snapshot.id)
    volume.delete()

    # Check whether tag is present with correct value
    retrieved_tags[tag_key].should.equal(tag_value)


@mock_ec2_deprecated
def test_filter_instances_by_wildcard_tags():
    conn = boto.connect_ec2(aws_access_key_id='the_key',
                            aws_secret_access_key='the_secret')
    reservation = conn.run_instances('ami-1234abcd')
    instance_a = reservation.instances[0]
    instance_a.add_tag("Key1", "Value1")
    reservation_b = conn.run_instances('ami-1234abcd')
    instance_b = reservation_b.instances[0]
    instance_b.add_tag("Key1", "Value2")

    reservations = conn.get_all_instances(filters={'tag:Key1': 'Value*'})
    reservations.should.have.length_of(2)

    reservations = conn.get_all_instances(filters={'tag-key': 'Key*'})
    reservations.should.have.length_of(2)

    reservations = conn.get_all_instances(filters={'tag-value': 'Value*'})
    reservations.should.have.length_of(2)


@mock_ec2
def test_create_volume_with_tags():
    client = boto3.client('ec2', 'us-west-2')
    response = client.create_volume(
            AvailabilityZone='us-west-2',
            Encrypted=False,
            Size=40,
            TagSpecifications=[
                {
                    'ResourceType': 'volume',
                    'Tags': [
                        {
                            'Key': 'TEST_TAG',
                            'Value': 'TEST_VALUE'
                        }
                    ],
                }
            ]
        )
    
    assert response['Tags'][0]['Key'] == 'TEST_TAG'
