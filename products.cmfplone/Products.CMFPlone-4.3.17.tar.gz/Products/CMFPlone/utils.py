import re
import string
from types import ClassType
from os.path import join, abspath, split

import pkg_resources
from plone.i18n.normalizer.interfaces import IIDNormalizer
from webdav.interfaces import IWriteLock

import zope.interface
from zope.interface import implementedBy
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.component import queryUtility
from zope.deprecation import deprecated
from zope.i18n import translate
from zope.publisher.interfaces.browser import IBrowserRequest

import OFS
from AccessControl import getSecurityManager
from AccessControl import ModuleSecurityInfo
from AccessControl import Unauthorized
from AccessControl.ZopeGuards import guarded_getattr
from AccessControl.ZopeGuards import guarded_getitem
from Acquisition import aq_base
from Acquisition import aq_get
from Acquisition import aq_inner
from Acquisition import aq_parent
from App.Common import package_home
from App.ImageFile import ImageFile
from collections import Mapping
from DateTime import DateTime
from DateTime.interfaces import DateTimeError
from Products.CMFCore.permissions import ManageUsers
from Products.CMFCore.utils import ToolInit as CMFCoreToolInit
from Products.CMFCore.utils import getToolByName

import transaction

security = ModuleSecurityInfo()
security.declarePrivate('deprecated')
security.declarePrivate('abspath')
security.declarePrivate('re')
security.declarePrivate('OFS')
security.declarePrivate('aq_get')
security.declarePrivate('package_home')
security.declarePrivate('ImageFile')
security.declarePrivate('CMFCoreToolInit')
security.declarePrivate('transaction')
security.declarePrivate('zope')


# Canonical way to get at CMFPlone directory
PACKAGE_HOME = package_home(globals())
security.declarePrivate('PACKAGE_HOME')
WWW_DIR = join(PACKAGE_HOME, 'www')
security.declarePrivate('WWW_DIR')

# Log methods
from log import log
from log import log_exc
from log import log_deprecated

_marker = []


def parent(obj):
    return aq_parent(aq_inner(obj))


def createBreadCrumbs(context, request):
    view = getMultiAdapter((context, request), name='breadcrumbs_view')
    return view.breadcrumbs()


def createNavTree(context, request, sitemap=False):
    view = getMultiAdapter((context, request), name='navtree_builder_view')
    return view.navigationTree()


def createSiteMap(context, request, sitemap=False):
    view = getMultiAdapter((context, request), name='sitemap_builder_view')
    return view.siteMap()


def _getDefaultPageView(obj, request):
    """This is a nasty hack because the view lookup fails when it occurs too
       early in the publishing process because the request isn't marked with
       the default skin.  Explicitly marking the request appears to cause
       connection errors, so we just instantiate the view manually.
    """
    view = queryMultiAdapter((obj, request), name='default_page')
    if view is None:
        # XXX: import here to avoid a circular dependency
        from plone.app.layout.navigation.defaultpage import DefaultPage
        view = DefaultPage(obj, request)
    return view


def isDefaultPage(obj, request):
    container = parent(obj)
    if container is None:
        return False
    view = _getDefaultPageView(container, request)
    return view.isDefaultPage(obj)


def getDefaultPage(obj, request):
    # Short circuit if we are not looking at a Folder
    if not obj.isPrincipiaFolderish:
        return None
    view = _getDefaultPageView(obj, request)
    return view.getDefaultPage()


def isIDAutoGenerated(context, id):
    # In 2.1 non-autogenerated is the common case, caught exceptions are
    # expensive, so let's make a cheap check first
    if id.count('.') < 2:
        return False

    pt = getToolByName(context, 'portal_types')
    portaltypes = pt.listContentTypes()
    portaltypes.extend([pt.lower() for pt in portaltypes])

    try:
        parts = id.split('.')
        random_number = parts.pop()
        date_created = parts.pop()
        obj_type = '.'.join(parts)
        type = ' '.join(obj_type.split('_'))
        # New autogenerated ids may have a lower case portal type
        if ((type in portaltypes or obj_type in portaltypes) and
            DateTime(date_created) and
            float(random_number)):
            return True
    except (ValueError, AttributeError, IndexError, DateTimeError):
        pass

    return False


def isExpired(content):
    """ Find out if the object is expired (copied from skin script) """

    expiry = None

    # NOTE: We also accept catalog brains as 'content' so that the
    # catalog-based folder_contents will work. It's a little magic, but
    # it works.

    # ExpirationDate should have an ISO date string, which we need to
    # convert to a DateTime

    # Try DC accessor first
    if base_hasattr(content, 'ExpirationDate'):
        expiry = content.ExpirationDate

    # Try the direct way
    if not expiry and base_hasattr(content, 'expires'):
        expiry = content.expires

    # See if we have a callable
    if safe_callable(expiry):
        expiry = expiry()

    # Convert to DateTime if necessary, ExpirationDate may return 'None'
    if expiry and expiry != 'None' and isinstance(expiry, basestring):
        expiry = DateTime(expiry)

    if isinstance(expiry, DateTime) and expiry.isPast():
        return 1
    return 0


def pretty_title_or_id(context, obj, empty_value=_marker):
    """Return the best possible title or id of an item, regardless
       of whether obj is a catalog brain or an object, but returning an
       empty title marker if the id is not set (i.e. it's auto-generated).
    """
    #if safe_hasattr(obj, 'aq_explicit'):
    #    obj = obj.aq_explicit
    #title = getattr(obj, 'Title', None)
    title = None
    if base_hasattr(obj, 'Title'):
        title = getattr(obj, 'Title', None)
    if safe_callable(title):
        title = title()
    if title:
        return title
    item_id = getattr(obj, 'getId', None)
    if safe_callable(item_id):
        item_id = item_id()
    if item_id and not isIDAutoGenerated(context, item_id):
        return item_id
    if empty_value is _marker:
        empty_value = getEmptyTitle(context)
    return empty_value


def getSiteEncoding(context):
    return 'utf-8'
deprecated('getSiteEncoding',
           ('`getSiteEncoding` is deprecated. Plone only supports UTF-8 '
            'currently. This method always returns "utf-8"'))

# XXX portal_utf8 and utf8_portal probably can go away
def portal_utf8(context, str, errors='strict'):
    # Test
    unicode(str, 'utf-8', errors)
    return str


# XXX this is the same method as above
def utf8_portal(context, str, errors='strict'):
    # Test
    unicode(str, 'utf-8', errors)
    return str


def getEmptyTitle(context, translated=True):
    """Returns string to be used for objects with no title or id"""
    # The default is an extra fancy unicode elipsis
    empty = unicode('\x5b\xc2\xb7\xc2\xb7\xc2\xb7\x5d', 'utf-8')
    if translated:
        if context is not None:
            if not IBrowserRequest.providedBy(context):
                context = aq_get(context, 'REQUEST', None)
        empty = translate('title_unset', domain='plone',
                          context=context, default=empty)
    return empty


def typesToList(context):
    ntp = getToolByName(context, 'portal_properties').navtree_properties
    ttool = getToolByName(context, 'portal_types')
    bl = ntp.getProperty('metaTypesNotToList', ())
    bl_dict = {}
    for t in bl:
        bl_dict[t] = 1
    all_types = ttool.listContentTypes()
    wl = [t for t in all_types if not t in bl_dict]
    return wl


def normalizeString(text, context=None, encoding=None):
    # The relaxed mode was removed in Plone 4.0. You should use either the url
    # or file name normalizer from the plone.i18n package instead.
    return queryUtility(IIDNormalizer).normalize(text)


class RealIndexIterator(object):
    """The 'real' version of the IndexIterator class, that's actually
    used to generate unique indexes.
    """
    __allow_access_to_unprotected_subobjects__ = 1

    def __init__(self, pos=0):
        self.pos = pos

    def next(self):
        result = self.pos
        self.pos = self.pos + 1
        return result


security.declarePrivate('ToolInit')
class ToolInit(CMFCoreToolInit):

    def getProductContext(self, context):
        name = '_ProductContext__prod'
        return getattr(context, name, getattr(context, '__prod', None))

    def getPack(self, context):
        name = '_ProductContext__pack'
        return getattr(context, name, getattr(context, '__pack__', None))

    def getIcon(self, context, path):
        pack = self.getPack(context)
        icon = None
        # This variable is just used for the log message
        icon_path = path
        try:
            icon = ImageFile(path, pack.__dict__)
        except (IOError, OSError):
            # Fallback:
            # Assume path is relative to CMFPlone directory
            path = abspath(join(PACKAGE_HOME, path))
            try:
                icon = ImageFile(path, pack.__dict__)
            except (IOError, OSError):
                # if there is some problem loading the fancy image
                # from the tool then  tell someone about it
                log(('The icon for the product: %s which was set to: %s, '
                     'was not found. Using the default.' %
                     (self.product_name, icon_path)))
        return icon

    def initialize(self, context):
        # Wrap the CMFCore Tool Init method.
        CMFCoreToolInit.initialize(self, context)
        for tool in self.tools:
            # Get the icon path from the tool
            path = getattr(tool, 'toolicon', None)
            if path is not None:
                pc = self.getProductContext(context)
                if pc is not None:
                    pid = pc.id
                    name = split(path)[1]
                    icon = self.getIcon(context, path)
                    if icon is None:
                        # Icon was not found
                        return
                    icon.__roles__ = None
                    tool.icon = 'misc_/%s/%s' % (self.product_name, name)
                    misc = OFS.misc_.misc_
                    Misc = OFS.misc_.Misc_
                    if not hasattr(misc, pid):
                        setattr(misc, pid, Misc(pid, {}))
                    getattr(misc, pid)[name] = icon


def _createObjectByType(type_name, container, id, *args, **kw):
    """Create an object without performing security checks

    invokeFactory and fti.constructInstance perform some security checks
    before creating the object. Use this function instead if you need to
    skip these checks.

    This method uses
    CMFCore.TypesTool.FactoryTypeInformation._constructInstance
    to create the object without security checks.
    """
    id = str(id)
    typesTool = getToolByName(container, 'portal_types')
    fti = typesTool.getTypeInfo(type_name)
    if not fti:
        raise ValueError('Invalid type %s' % type_name)

    return fti._constructInstance(container, id, *args, **kw)


def safeToInt(value, default=0):
    """Convert value to integer or just return 0 if we can't

       >>> safeToInt(45)
       45

       >>> safeToInt("42")
       42

       >>> safeToInt("spam")
       0

       >>> safeToInt([])
       0

       >>> safeToInt(None)
       0

       >>> safeToInt(None, default=-1)
       -1
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

release_levels = ('alpha', 'beta', 'candidate', 'final')
rl_abbr = {'a': 'alpha', 'b': 'beta', 'rc': 'candidate'}


def versionTupleFromString(v_str):
    """Returns version tuple from passed in version string

        >>> versionTupleFromString('1.2.3')
        (1, 2, 3, 'final', 0)

        >>> versionTupleFromString('2.1-final1 (SVN)')
        (2, 1, 0, 'final', 1)

        >>> versionTupleFromString('3-beta')
        (3, 0, 0, 'beta', 0)

        >>> versionTupleFromString('2.0a3')
        (2, 0, 0, 'alpha', 3)

        >>> versionTupleFromString('foo') is None
        True
        """
    regex_str = "(^\d+)[.]?(\d*)[.]?(\d*)[- ]?(alpha|beta|candidate|final|a|b|rc)?(\d*)"
    v_regex = re.compile(regex_str)
    match = v_regex.match(v_str)
    if match is None:
        v_tpl = None
    else:
        groups = list(match.groups())
        for i in (0, 1, 2, 4):
            groups[i] = safeToInt(groups[i])
        if groups[3] is None:
            groups[3] = 'final'
        elif groups[3] in rl_abbr.keys():
            groups[3] = rl_abbr[groups[3]]
        v_tpl = tuple(groups)
    return v_tpl


def getFSVersionTuple():
    """Returns Products.CMFPlone version tuple"""
    version = pkg_resources.get_distribution('Products.CMFPlone').version
    return versionTupleFromString(version)


def transaction_note(note):
    """Write human legible note"""
    T = transaction.get()
    if isinstance(note, unicode):
        # Convert unicode to a regular string for the backend write IO.
        # UTF-8 is the only reasonable choice, as using unicode means
        # that Latin-1 is probably not enough.
        note = note.encode('utf-8', 'replace')

    if (len(T.description) + len(note)) >= 65533:
        log('Transaction note too large omitting %s' % str(note))
    else:
        T.note(str(note))


def base_hasattr(obj, name):
    """Like safe_hasattr, but also disables acquisition."""
    return safe_hasattr(aq_base(obj), name)


def safe_hasattr(obj, name, _marker=object()):
    """Make sure we don't mask exceptions like hasattr().

    We don't want exceptions other than AttributeError to be masked,
    since that too often masks other programming errors.
    Three-argument getattr() doesn't mask those, so we use that to
    implement our own hasattr() replacement.
    """
    return getattr(obj, name, _marker) is not _marker


def safe_callable(obj):
    """Make sure our callable checks are ConflictError safe."""
    if safe_hasattr(obj, '__class__'):
        if safe_hasattr(obj, '__call__'):
            return True
        else:
            return isinstance(obj, ClassType)
    else:
        return callable(obj)


def safe_unicode(value, encoding='utf-8'):
    """Converts a value to unicode, even it is already a unicode string.

        >>> from Products.CMFPlone.utils import safe_unicode

        >>> safe_unicode('spam')
        u'spam'
        >>> safe_unicode(u'spam')
        u'spam'
        >>> safe_unicode(u'spam'.encode('utf-8'))
        u'spam'
        >>> safe_unicode('\xc6\xb5')
        u'\u01b5'
        >>> safe_unicode(u'\xc6\xb5'.encode('iso-8859-1'))
        u'\u01b5'
        >>> safe_unicode('\xc6\xb5', encoding='ascii')
        u'\u01b5'
        >>> safe_unicode(1)
        1
        >>> print safe_unicode(None)
        None
    """
    if isinstance(value, unicode):
        return value
    elif isinstance(value, basestring):
        try:
            value = unicode(value, encoding)
        except (UnicodeDecodeError):
            value = value.decode('utf-8', 'replace')
    return value


def tuplize(value):
    if isinstance(value, tuple):
        return value
    if isinstance(value, list):
        return tuple(value)
    return (value,)


def _detuplize(interfaces, append):
    if isinstance(interfaces, (tuple, list)):
        for sub in interfaces:
            _detuplize(sub, append)
    else:
        append(interfaces)


def flatten(interfaces):
    flattened = []
    _detuplize(interfaces, flattened.append)
    return tuple(flattened)


def directlyProvides(obj, *interfaces):
    return zope.interface.directlyProvides(obj, *interfaces)


def classImplements(class_, *interfaces):
    return zope.interface.classImplements(class_, *interfaces)


def classDoesNotImplement(class_, *interfaces):
    # convert any Zope 2 interfaces to Zope 3 using fromZ2Interface
    interfaces = flatten(interfaces)
    implemented = implementedBy(class_)
    for iface in interfaces:
        implemented = implemented - iface
    return zope.interface.classImplementsOnly(class_, implemented)


def webdav_enabled(obj, container):
    """WebDAV check used in externalEditorEnabled.py"""

    # Object implements lock interface
    if IWriteLock.providedBy(obj):
        return True

    return False


# Copied 'unrestricted_rename' from ATCT migrations to avoid
# a dependency.

from App.Dialogs import MessageDialog
from OFS.CopySupport import CopyError
from OFS.CopySupport import eNotSupported
from cgi import escape
import sys

security.declarePrivate('sys')

def _unrestricted_rename(container, id, new_id):
    """Rename a particular sub-object

    Copied from OFS.CopySupport

    Less strict version of manage_renameObject:
        * no write lock check
        * no verify object check from PortalFolder so it's allowed to rename
          even unallowed portal types inside a folder
    """
    try:
        container._checkId(new_id)
    except:
        raise CopyError, MessageDialog(
              title='Invalid Id',
              message=sys.exc_info()[1],
              action='manage_main')
    ob = container._getOb(id)
    if not ob.cb_isMoveable():
        raise CopyError, eNotSupported % escape(id)
    try:
        ob._notifyOfCopyTo(container, op=1)
    except:
        raise CopyError, MessageDialog(
              title='Rename Error',
              message=sys.exc_info()[1],
              action='manage_main')
    container._delObject(id)
    ob = aq_base(ob)
    ob._setId(new_id)

    # Note - because a rename always keeps the same context, we
    # can just leave the ownership info unchanged.
    container._setObject(new_id, ob, set_owner=0)
    ob = container._getOb(new_id)
    ob._postCopy(container, op=1)

    return None


# Copied '_getSecurity' from Archetypes.utils to avoid a dependency.

from AccessControl import ClassSecurityInfo
security.declarePrivate('ClassSecurityInfo')


def _getSecurity(klass, create=True):
    # a Zope 2 class can contain some attribute that is an instance
    # of ClassSecurityInfo. Zope 2 scans through things looking for
    # an attribute that has the name __security_info__ first
    info = vars(klass)
    security = None
    for k, v in info.items():
        if hasattr(v, '__security_info__'):
            security = v
            break
    # Didn't found a ClassSecurityInfo object
    if security is None:
        if not create:
            return None
        # we stuff the name ourselves as __security__, not security, as this
        # could theoretically lead to name clashes, and doesn't matter for
        # zope 2 anyway.
        security = ClassSecurityInfo()
        setattr(klass, '__security__', security)
    return security


def isLinked(obj):
    """ check if the given content object is linked from another one

        WARNING: this function can be time consuming !!

            It deletes the object in a subtransaction that is rollbacked.
            In other words, the object is kept safe.

            Nevertheless, this implies that it also deletes recursively
            all object's subobjects and references, which can be very
            expensive.
    """
    # first check to see if link integrity handling has been enabled at all
    # and if so, if the removal of the object was already confirmed, i.e.
    # while replaying the request;  unfortunately this makes it necessary
    # to import from plone.app.linkintegrity here, hence the try block...
    try:
        from plone.app.linkintegrity.interfaces import ILinkIntegrityInfo
        info = ILinkIntegrityInfo(obj.REQUEST)
    except (ImportError, TypeError):
        # if p.a.li isn't installed the following check can be cut short...
        return False
    if not info.integrityCheckingEnabled():
        return False
    if info.isConfirmedItem(obj):
        return True
    # otherwise, when not replaying the request already, it is tried to
    # delete the object, making it possible to find out if it was referenced,
    # i.e. in case a link integrity exception was raised
    linked = False
    parent = obj.aq_inner.aq_parent
    try:
        savepoint = transaction.savepoint()
        parent.manage_delObjects(obj.getId())
    except OFS.ObjectManager.BeforeDeleteException:
        linked = True
    except:  # ignore other exceptions, not useful to us at this point
        pass
    finally:
        savepoint.rollback()
    return linked


def set_own_login_name(member, loginname):
    """Allow the user to set his/her own login name.

    If you have the Manage Users permission, you can update the login
    name of another member too, though the name of this function is a
    bit weird then.  Historical accident.
    """
    if member.getUserName() == loginname:
        # Bail out early as there is nothing to do.  Also this avoids
        # an Unauthorized error when this is a member that has just
        # been registered.
        return
    pas = getToolByName(member, 'acl_users')
    mt = getToolByName(member, 'portal_membership')
    if member.getId() == mt.getAuthenticatedMember().getId():
        pas.updateOwnLoginName(loginname)
        return
    secman = getSecurityManager()
    if not secman.checkPermission(ManageUsers, member):
        raise Unauthorized('You can only change your OWN login name.')
    pas.updateLoginName(member.getId(), loginname)


class _MagicFormatMapping(Mapping):
    """Pulled from Jinja2.

    This class implements a dummy wrapper to fix a bug in the Python
    standard library for string formatting.

    See http://bugs.python.org/issue13598 for information about why
    this is necessary.
    """

    def __init__(self, args, kwargs):
        self._args = args
        self._kwargs = kwargs
        self._last_index = 0

    def __getitem__(self, key):
        if key == '':
            idx = self._last_index
            self._last_index += 1
            try:
                return self._args[idx]
            except LookupError:
                pass
            key = str(idx)
        return self._kwargs[key]

    def __iter__(self):
        return iter(self._kwargs)

    def __len__(self):
        return len(self._kwargs)


class SafeFormatter(string.Formatter):
    """Formatter using guarded access."""

    def __init__(self, value):
        self.value = value
        super(SafeFormatter, self).__init__()

    def get_field(self, field_name, args, kwargs):
        """Get the field value using guarded methods."""
        first, rest = field_name._formatter_field_name_split()

        obj = self.get_value(first, args, kwargs)

        # loop through the rest of the field_name, doing
        #  getattr or getitem as needed
        for is_attr, i in rest:
            if is_attr:
                obj = guarded_getattr(obj, i)
            else:
                obj = guarded_getitem(obj, i)

        return obj, first

    def safe_format(self, *args, **kwargs):
        """Safe variant of `format` method."""
        kwargs = _MagicFormatMapping(args, kwargs)
        return self.vformat(self.value, args, kwargs)


def safe_format(inst, method):
    """Use our SafeFormatter that uses guarded_getattr and guarded_getitem."""
    return SafeFormatter(inst).safe_format
