"""JSON implementations of relationship sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from bson.objectid import ObjectId


from . import objects
from . import queries
from .. import utilities
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import DateTime
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from ..utilities import overlap
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.relationship import sessions as abc_relationship_sessions
from dlkit.abstract_osid.relationship.objects import FamilyForm as ABCFamilyForm
from dlkit.abstract_osid.relationship.objects import RelationshipForm as ABCRelationshipForm
from dlkit.abstract_osid.type.primitives import Type as ABCType


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1


class RelationshipLookupSession(abc_relationship_sessions.RelationshipLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving relationships.

    A ``Relationship`` is mapped to two OSID ``Ids``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * federated family view: includes relationships in families which
        are children of this family in the family hierarchy
      * isolated family view: restricts lookups to this family only
      * effective relationship view: Relationship methods return only
        relationships currently in effect.
      * any effective relationship view: Relationship methods return
        both effective and ineffective relationships.


    Relationships may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Relationship``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Family
        self._catalog_name = 'Family'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='relationship',
            cat_name='Family',
            cat_class=objects.Family)
        self._kwargs = kwargs

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    family = property(fget=get_family)

    def can_lookup_relationships(self):
        """Tests if this user can perform ``Relationship`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_relationship_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_relationship_view(self):
        """A complete view of the ``Relationship`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_effective_relationship_view(self):
        """Only relationships whose effective dates are current are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_effective_relationship_view
        self._use_effective_view()

    def use_any_effective_relationship_view(self):
        """All relationships of any effective dates are returned by all methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_any_effective_relationship_view
        self._use_any_effective_view()

    @utilities.arguments_not_none
    def get_relationship(self, relationship_id):
        """Gets the ``Relationship`` specified by its ``Id``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to retrieve
        return: (osid.relationship.Relationship) - the returned
                ``Relationship``
        raise:  NotFound - no ``Relationship`` found with the given
                ``Id``
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(relationship_id, 'relationship').get_identifier())},
                 **self._view_filter()))
        return objects.Relationship(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_relationships_by_ids(self, relationship_ids):
        """Gets a ``RelationshipList`` corresponding to the given ``IdList``.

        arg:    relationship_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``relationship_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        object_id_list = []
        for i in relationship_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'relationship').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.RelationshipList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type(self, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` which does not include relationships of types derived from the specified ``Type``.

        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(relationship_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.RelationshipList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_relationships_by_parent_genus_type(self, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` and include any additional relationships with genus types derived from the specified ``Type``.

        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        raise:  NullArgument - ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.RelationshipList([])

    @utilities.arguments_not_none
    def get_relationships_by_record_type(self, relationship_record_type):
        """Gets a ``RelationshipList`` containing the given relationship record ``Type``.

        arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.RelationshipList([])

    @utilities.arguments_not_none
    def get_relationships_on_date(self, from_, to):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive but not confined to the date range.

        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_on_date
        relationship_list = []
        for relationship in self.get_relationships():
            if overlap(from_, to, relationship.start_date, relationship.end_date):
                relationship_list.append(relationship)
        return objects.RelationshipList(relationship_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_for_source(self, source_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        arg:    source_id (osid.id.Id): a peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(source_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_for_source_on_date(self, source_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, from`` ,or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date
        relationship_list = []
        for relationship in self.get_relationships_for_source(source_id):
            if overlap(from_, to, relationship.start_date, relationship.end_date):
                relationship_list.append(relationship)
        return objects.RelationshipList(relationship_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_source(self, source_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(source_id),
                  'genusTypeId': str(relationship_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_source_on_date(self, source_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type`` and effective during the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, relationship_genus_type,
                from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date
        relationship_list = []
        for relationship in self.get_relationships_by_genus_type_for_source():
            if overlap(from_, to, relationship.start_date, relationship.end_date):
                relationship_list.append(relationship)
        return objects.RelationshipList(relationship_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_for_destination(self, destination_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``destination_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_destination
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'destinationId': str(destination_id)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_for_destination_on_date(self, destination_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` with a starting effective date in the given range inclusive.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``destination_id, from`` ,or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_destination_on_date
        relationship_list = []
        for relationship in self.get_relationships_for_destination():
            if overlap(from_, to, relationship.start_date, relationship.end_date):
                relationship_list.append(relationship)
        return objects.RelationshipList(relationship_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_destination(self, destination_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``destination_id`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_destination
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'destinationId': str(destination_id),
                  'genusTypeId': str(relationship_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_destination_on_date(self, destination_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type`` and effective during the entire given date range inclusive but not confined to the date range.

        arg:    destination_id (osid.id.Id): a peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_relationships_for_peers(self, source_id, destination_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids``.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(source_id),
                  'destinationId': str(destination_id)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_for_peers_on_date(self, source_id, destination_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids`` and effective during the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``source_id, destination_id, from`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_peers(self, source_id, destination_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding between the given peer ``Ids`` and relationship genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer or an error
        results if a relationship is inaccessible. Otherwise,
        inaccessible ``Relationships`` may be omitted from the list.

        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  NullArgument - ``source_id, destination_id,`` or
                ``relationship_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(source_id),
                  'destinationId': str(destination_id),
                  'genusTypeId': str(relationship_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.RelationshipList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_relationships_by_genus_type_for_peers_on_date(self, source_id, destination_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive but not confined to the date range.

        arg:    source_id (osid.id.Id): a peer ``Id``
        arg:    destination_id (osid.id.Id): a related peer ``Id``
        arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.relationship.RelationshipList) - the relationships
        raise:  InvalidArgument - ``from is greater than to``
        raise:  NullArgument - ``source_id, destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_relationships(self):
        """Gets all ``Relationships``.

        return: (osid.relationship.RelationshipList) - a list of
                ``Relationships``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.RelationshipList(result, runtime=self._runtime, proxy=self._proxy)

    relationships = property(fget=get_relationships)


class RelationshipQuerySession(abc_relationship_sessions.RelationshipQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Relationship`` objects.

    The search query is constructed using the ``Relationship``.

    Relationships may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelationshipQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Family
        self._catalog_name = 'Family'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='relationship',
            cat_name='Family',
            cat_class=objects.Family)
        self._kwargs = kwargs

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    family = property(fget=get_family)

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def can_search_relationships(self):
        """Tests if this user can perform ``Relationship`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def get_relationship_query(self):
        """Gets a relationship query.

        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.RelationshipQuery(runtime=self._runtime)

    relationship_query = property(fget=get_relationship_query)

    @utilities.arguments_not_none
    def get_relationships_by_query(self, relationship_query):
        """Gets a list of ``Relationships`` matching the given relationship query.

        arg:    relationship_query
                (osid.relationship.RelationshipQuery): the relationship
                query
        return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        raise:  NullArgument - ``relationship_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in relationship_query._query_terms:
            if '$in' in relationship_query._query_terms[term] and '$nin' in relationship_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': relationship_query._query_terms[term]['$in']}},
                             {term: {'$nin': relationship_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: relationship_query._query_terms[term]})
        for term in relationship_query._keyword_terms:
            or_list.append({term: relationship_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('relationship',
                                             collection='Relationship',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.RelationshipList(result, runtime=self._runtime, proxy=self._proxy)


class RelationshipAdminSession(abc_relationship_sessions.RelationshipAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Relationships``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Relationship,`` a ``RelationshipForm`` is requested using
    ``get_relationship_form_for_create()`` specifying the desired peers
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``RelationshipForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``RelationshipForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``RelationshipForm`` corresponds to an attempted transaction.

    For updates, ``RelationshipForms`` are requested to the
    ``Relationship``  ``Id`` that is to be updated using
    ``getRelationshipFormForUpdate()``. Similarly, the
    ``RelationshipForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``RelationshipForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``Relationships``. To unmap a
    ``Relationship`` from the current ``Family,`` the
    ``RelationshipFamilyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Relationship`` itself thus
    removing it from all known ``Family`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Family
        self._catalog_name = 'Family'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='relationship',
            cat_name='Family',
            cat_class=objects.Family)
        self._forms = dict()
        self._kwargs = kwargs

    def get_family_id(self):
        """Gets the ``Familt``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        return: (osid.relationship.Family) - the family
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    family = property(fget=get_family)

    def can_create_relationships(self):
        """Tests if this user can create ``Relationships`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known creating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_relationship_with_record_types(self, relationship_record_types):
        """Tests if this user can create a single ``Relationship`` using the desired record types.

        While ``RelationshipManager.getRelationshipRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Relationship``. Providing an empty array tests if a
        ``Relationship`` can be created with no records.

        arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        return: (boolean) - ``true`` if ``Relationship`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``relationship_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_relationship_form_for_create(self, source_id, destination_id, relationship_record_types):
        """Gets the relationship form for creating new relationships.

        A new form should be requested for each create transaction.

        arg:    source_id (osid.id.Id): ``Id`` of a peer
        arg:    destination_id (osid.id.Id): ``Id`` of the related peer
        arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        return: (osid.relationship.RelationshipForm) - the relationship
                form
        raise:  NotFound - ``source_id`` or ``destination_id`` is not
                found
        raise:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested recod
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create
        # These really need to be in module imports:
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from dlkit.abstract_osid.type.primitives import Type as ABCType
        if not isinstance(source_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(destination_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in relationship_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if relationship_record_types == []:
            # WHY are we passing family_id = self._catalog_id below, seems redundant:
            obj_form = objects.RelationshipForm(
                family_id=self._catalog_id,
                source_id=source_id,
                destination_id=destination_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.RelationshipForm(
                family_id=self._catalog_id,
                record_types=relationship_record_types,
                source_id=source_id,
                destination_id=destination_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_relationship(self, relationship_form):
        """Creates a new ``Relationship``.

        arg:    relationship_form (osid.relationship.RelationshipForm):
                the form for this ``Relationship``
        return: (osid.relationship.Relationship) - the new
                ``Relationship``
        raise:  IllegalState - ``relationship_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``relationship_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        if not isinstance(relationship_form, ABCRelationshipForm):
            raise errors.InvalidArgument('argument type is not an RelationshipForm')
        if relationship_form.is_for_update():
            raise errors.InvalidArgument('the RelationshipForm is for update only, not create')
        try:
            if self._forms[relationship_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('relationship_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('relationship_form did not originate from this session')
        if not relationship_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(relationship_form._my_map)

        self._forms[relationship_form.get_id().get_identifier()] = CREATED
        result = objects.Relationship(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_relationships(self):
        """Tests if this user can update ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_relationship_form_for_update(self, relationship_id):
        """Gets the relationship form for updating an existing relationship.

        A new relationship form should be requested for each update
        transaction.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        return: (osid.relationship.RelationshipForm) - the relationship
                form
        raise:  NotFound - ``relationship_id`` is not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        if not isinstance(relationship_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (relationship_id.get_identifier_namespace() != 'relationship.Relationship' or
                relationship_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(relationship_id.get_identifier())})

        obj_form = objects.RelationshipForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_relationship(self, relationship_form):
        """Updates an existing relationship.

        arg:    relationship_form (osid.relationship.RelationshipForm):
                the form containing the elements to be updated
        raise:  IllegalState - ``relationship_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``relationship_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        if not isinstance(relationship_form, ABCRelationshipForm):
            raise errors.InvalidArgument('argument type is not an RelationshipForm')
        if not relationship_form.is_for_update():
            raise errors.InvalidArgument('the RelationshipForm is for update only, not create')
        try:
            if self._forms[relationship_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('relationship_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('relationship_form did not originate from this session')
        if not relationship_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(relationship_form._my_map)

        self._forms[relationship_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Relationship(
            osid_object_map=relationship_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_relationships(self):
        """Tests if this user can delete ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_relationship(self, relationship_id):
        """Deletes a ``Relationship``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to remove
        raise:  NotFound - ``relationship_id`` not found
        raise:  NullArgument - ``relationship_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('relationship',
                                         collection='Relationship',
                                         runtime=self._runtime)
        if not isinstance(relationship_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        relationship_map = collection.find_one(
            dict({'_id': ObjectId(relationship_id.get_identifier())},
                 **self._view_filter()))

        objects.Relationship(osid_object_map=relationship_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(relationship_id.get_identifier())})

    def can_manage_relationship_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Relationship`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_relationship(self, relationship_id, alias_id):
        """Adds an ``Id`` to a ``Relationship`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Relationship`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another relationship, it is
        reassigned to the given relationship ``Id``.

        arg:    relationship_id (osid.id.Id): the ``Id`` of a
                ``Relationship``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``relationship`` not found
        raise:  NullArgument - ``relationship_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=relationship_id, equivalent_id=alias_id)


class FamilyLookupSession(abc_relationship_sessions.FamilyLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Family`` objects.

    The ``Family`` represents a collection of relationships.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Families`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Families``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

    """
    _session_namespace = 'relationship.FamilyLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_families(self):
        """Tests if this user can perform ``Family`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.can_lookup_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_lookup_catalogs()
        return True

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_family(self, family_id):
        """Gets the ``Family`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Family`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Family`` and retained for compatibil

        arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        return: (osid.relationship.Family) - the family
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=family_id)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if family_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Family, cat_name='Family')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(family_id, 'relationship').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Family.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(family_id, 'relationship', 'Family')

        return objects.Family(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_families_by_ids(self, family_ids):
        """Gets a ``FamilyList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the families
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible families may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    family_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``family_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Family() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=family_ids)
        catalog_id_list = []
        for i in family_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.FamilyList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_families_by_genus_type(self, family_genus_type):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` which does not include families of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_genus_type (osid.type.Type): a family genus type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=family_genus_type)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(family_genus_type)}).sort('_id', DESCENDING)

        return objects.FamilyList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_families_by_parent_genus_type(self, family_genus_type):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` and include any additional families with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_genus_type (osid.type.Type): a family genus type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_families_by_record_type(self, family_record_type):
        """Gets a ``FamilyList`` containing the given family record ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    family_record_type (osid.type.Type): a family record
                type
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_families_by_provider(self, resource_id):
        """Gets a ``FamilyList`` from the given provider.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_families(self):
        """Gets all families.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        return: (osid.relationship.FamilyList) - a list of families
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.FamilyList(result, runtime=self._runtime, proxy=self._proxy)

    families = property(fget=get_families)


class FamilyAdminSession(abc_relationship_sessions.FamilyAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Families``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Family,`` a ``FamilyForm`` is requested using
    ``get_family_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``FamilyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``FamilyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``FamilyForm``
    corresponds to an attempted transaction.

    For updates, ``FamilyForms`` are requested to the ``Family``  ``Id``
    that is to be updated using ``getFamilyFormForUpdate()``. Similarly,
    the ``FamilyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``FamilyForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Families``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'relationship.FamilyAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_families(self):
        """Tests if this user can create families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs()
        return True

    @utilities.arguments_not_none
    def can_create_family_with_record_types(self, family_record_types):
        """Tests if this user can create a single ``Family`` using the desired record types.

        While ``RelationshipManager.getFamilyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Family``.
        Providing an empty array tests if a ``Family`` can be created
        with no records.

        arg:    family_record_types (osid.type.Type[]): array of family
                record types
        return: (boolean) - ``true`` if ``Family`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``family_record_types is null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=family_record_types)
        return True

    @utilities.arguments_not_none
    def get_family_form_for_create(self, family_record_types):
        """Gets the family form for creating new families.

        A new form should be requested for each create transaction.

        arg:    family_record_types (osid.type.Type[]): array of family
                record types
        return: (osid.relationship.FamilyForm) - the family form
        raise:  NullArgument - ``family_record_types is null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=family_record_types)
        for arg in family_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if family_record_types == []:
            result = objects.FamilyForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.FamilyForm(
                record_types=family_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_family(self, family_form):
        """Creates a new ``Family``.

        arg:    family_form (osid.relationship.FamilyForm): the form for
                this ``Family``.
        return: (osid.relationship.Family) - the new ``Family``
        raise:  IllegalState - ``family_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``family_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=family_form)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        if not isinstance(family_form, ABCFamilyForm):
            raise errors.InvalidArgument('argument type is not an FamilyForm')
        if family_form.is_for_update():
            raise errors.InvalidArgument('the FamilyForm is for update only, not create')
        try:
            if self._forms[family_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('family_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('family_form did not originate from this session')
        if not family_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(family_form._my_map)

        self._forms[family_form.get_id().get_identifier()] = CREATED
        result = objects.Family(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_families(self):
        """Tests if this user can update families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_update_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_update_catalogs()
        return True

    @utilities.arguments_not_none
    def get_family_form_for_update(self, family_id):
        """Gets the family form for updating an existing family.

        A new family form should be requested for each update
        transaction.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        return: (osid.relationship.FamilyForm) - the family form
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=family_id)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        if not isinstance(family_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(family_id.get_identifier())})

        cat_form = objects.FamilyForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_family(self, family_form):
        """Updates an existing family.

        arg:    family_form (osid.relationship.FamilyForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``family_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``family_id`` or ``family_form`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=family_form)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        if not isinstance(family_form, ABCFamilyForm):
            raise errors.InvalidArgument('argument type is not an FamilyForm')
        if not family_form.is_for_update():
            raise errors.InvalidArgument('the FamilyForm is for update only, not create')
        try:
            if self._forms[family_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('family_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('family_form did not originate from this session')
        if not family_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(family_form._my_map)  # save is deprecated - change to replace_one

        self._forms[family_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Family(osid_object_map=family_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_families(self):
        """Tests if this user can delete families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Family`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_delete_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_delete_catalogs()
        return True

    @utilities.arguments_not_none
    def delete_family(self, family_id):
        """Deletes a ``Family``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                remove
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=family_id)
        collection = JSONClientValidated('relationship',
                                         collection='Family',
                                         runtime=self._runtime)
        if not isinstance(family_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['Relationship', 'Family']:
            obj_collection = JSONClientValidated('relationship',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedFamilyIds': {'$in': [str(family_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(family_id.get_identifier())})

    def can_manage_family_aliases(self):
        """Tests if this user can manage ``Id`` aliases for families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Family`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_family(self, family_id, alias_id):
        """Adds an ``Id`` to a ``Family`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Family`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another family, it is
        reassigned to the given family ``Id``.

        arg:    family_id (osid.id.Id): the ``Id`` of a ``Family``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=family_id, alias_id=alias_id)
        self._alias_id(primary_id=family_id, equivalent_id=alias_id)


class FamilyHierarchySession(abc_relationship_sessions.FamilyHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Family`` objects.

    Each node in the hierarchy is a unique ``Family``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_families()`` and ``getChildFamilies()``. To relate
    these ``Ids`` to another OSID, ``get_family_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Family`` available in the Relationship OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_families()`` or ``get_child_families()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: family elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    _session_namespace = 'relationship.FamilyHierarchySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchySession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
                Id(authority='RELATIONSHIP',
                   namespace='CATALOG',
                   identifier='FAMILY'),
                proxy=self._proxy)

    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_access_family_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_access_catalog_hierarchy()
        return True

    def use_comparative_family_view(self):
        """The returns from the family methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    def get_root_family_ids(self):
        """Gets the root family ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root family ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_family_ids = property(fget=get_root_family_ids)

    def get_root_families(self):
        """Gets the root families in the family hierarchy.

        A node with no parents is an orphan. While all family ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        return: (osid.relationship.FamilyList) - the root families
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return FamilyLookupSession(
            self._proxy,
            self._runtime).get_families_by_ids(list(self.get_root_family_ids()))

    root_families = property(fget=get_root_families)

    @utilities.arguments_not_none
    def has_parent_families(self, family_id):
        """Tests if the ``Family`` has any parents.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the family has parents,
                ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=family_id)
        return self._hierarchy_session.has_parents(id_=family_id)

    @utilities.arguments_not_none
    def is_parent_of_family(self, id_, family_id):
        """Tests if an ``Id`` is a direct parent of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=family_id)
        return self._hierarchy_session.is_parent(id_=family_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_family_ids(self, family_id):
        """Gets the parent ``Ids`` of the given family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (osid.id.IdList) - the parent ``Ids`` of the family
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=family_id)
        return self._hierarchy_session.get_parents(id_=family_id)

    @utilities.arguments_not_none
    def get_parent_families(self, family_id):
        """Gets the parent families of the given ``id``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        return: (osid.relationship.FamilyList) - the parent families of
                the ``id``
        raise:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=family_id)
        return FamilyLookupSession(
            self._proxy,
            self._runtime).get_families_by_ids(
                list(self.get_parent_family_ids(family_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_family(self, id_, family_id):
        """Tests if an ``Id`` is an ancestor of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=family_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=family_id)

    @utilities.arguments_not_none
    def has_child_families(self, family_id):
        """Tests if a family has any children.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``family_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=family_id)
        return self._hierarchy_session.has_children(id_=family_id)

    @utilities.arguments_not_none
    def is_child_of_family(self, id_, family_id):
        """Tests if a family is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=family_id)
        return self._hierarchy_session.is_child(id_=family_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_family_ids(self, family_id):
        """Gets the child ``Ids`` of the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the family
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=family_id)
        return self._hierarchy_session.get_children(id_=family_id)

    @utilities.arguments_not_none
    def get_child_families(self, family_id):
        """Gets the child families of the given ``id``.

        arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        return: (osid.relationship.FamilyList) - the child families of
                the ``id``
        raise:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=family_id)
        return FamilyLookupSession(
            self._proxy,
            self._runtime).get_families_by_ids(
                list(self.get_child_family_ids(family_id)))

    @utilities.arguments_not_none
    def is_descendant_of_family(self, id_, family_id):
        """Tests if an ``Id`` is a descendant of a family.

        arg:    id (osid.id.Id): an ``Id``
        arg:    family_id (osid.id.Id): the ``Id`` of a family
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``family_id,``  ``false`` otherwise
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``id`` or ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=family_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=family_id)

    @utilities.arguments_not_none
    def get_family_node_ids(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a family node
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=family_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=family_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_family_nodes(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given family.

        arg:    family_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.relationship.FamilyNode) - a family node
        raise:  NotFound - ``family_id`` is not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.FamilyNode(self.get_family_node_ids(
            family_id=family_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class FamilyHierarchyDesignSession(abc_relationship_sessions.FamilyHierarchyDesignSession, osid_sessions.OsidSession):
    """This session manages a hierarchy of families may be organized into a hierarchy for organizing or federating.

    A parent ``Family`` includes all of the relationships of its
    children such that a single root node contains all of the
    relationships of the federation.

    """
    _session_namespace = 'relationship.FamilyHierarchyDesignSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_design_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_design_session_for_hierarchy(
                Id(authority='RELATIONSHIP',
                   namespace='CATALOG',
                   identifier='FAMILY'),
                proxy=self._proxy)

    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_modify_family_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_modify_catalog_hierarchy()
        return True

    @utilities.arguments_not_none
    def add_root_family(self, family_id):
        """Adds a root family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  AlreadyExists - ``family_id`` is already in hierarchy
        raise:  NotFound - ``family_id`` not found
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=family_id)
        return self._hierarchy_session.add_root(id_=family_id)

    @utilities.arguments_not_none
    def remove_root_family(self, family_id):
        """Removes a root family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  NotFound - ``family_id`` not a root
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=family_id)
        return self._hierarchy_session.remove_root(id_=family_id)

    @utilities.arguments_not_none
    def add_child_family(self, family_id, child_id):
        """Adds a child to a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``family_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``family_id`` or ``child_id`` not found
        raise:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=family_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=family_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_family(self, family_id, child_id):
        """Removes a child from a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``family_id`` not a parent of ``child_id``
        raise:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=family_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=family_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_families(self, family_id):
        """Removes all children from a family.

        arg:    family_id (osid.id.Id): the ``Id`` of a family
        raise:  NotFound - ``family_id`` not in hierarchy
        raise:  NullArgument - ``family_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=family_id)
        return self._hierarchy_session.remove_children(id_=family_id)
