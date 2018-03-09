import warnings

import requests
import six

from pyHIBP import pwnedpasswords as pw

HIBP_API_BASE_URI = "https://haveibeenpwned.com/api/v2/"
HIBP_API_ENDPOINT_BREACH_SINGLE = "breach/"
HIBP_API_ENDPOINT_BREACHES = "breaches"
HIBP_API_ENDPOINT_BREACHED_ACCT = "breachedaccount/"
HIBP_API_ENDPOINT_DATA_CLASSES = "dataclasses"
HIBP_API_ENDPOINT_PASTES = "pasteaccount/"

# The HIBP API requires that a useragent be set.
pyHIBP_USERAGENT = "pyHIBP: A Python Interface to the Public HIBP API"


def _process_response(response):
    """
    Process the `requests` response from the call to the HIBP API endpoints.

    :param response: The response object from a call to `requests`
    :return: True if HTTP Status 200, False if 404. Raises RuntimeError on API-defined status codes of
    400, 403, 429; NotImplementedError if the API returns an unexpected HTTP status code.
    """
    if response.status_code == 200:
        # The request was successful (a password/breach/paste was found)
        return True
    elif response.status_code == 404:
        # The request was successful, though the item wasn't found
        return False
    elif response.status_code == 400:
        # Bad request - The account does not comply with an acceptable format (i.e., it's an empty string)
        raise RuntimeError(
            "HTTP 400 - Bad request - The account does not comply with an acceptable format (i.e., it's an empty string)")
    elif response.status_code == 403:
        # Forbidden - no user agent has been specified in the request
        raise RuntimeError("HTTP 403 - User agent required for HIBP API requests, but no user agent was sent to the API endpoint")
    elif response.status_code == 429:
        # Too many requests - the rate limit has been exceeded
        raise RuntimeError(
            "HTTP 429 - Rate limit exceeded: API rate limit is 1500ms. Retry-After header was: " + response.headers['Retry-After']
        )
    else:
        # We /should/ get one of the above error codes. If not, raise an error.
        raise NotImplementedError("Returned HTTP status code of " + str(response.status_code) + " was not expected.")


def get_account_breaches(account=None, domain=None, truncate_response=False, include_unverified=False):
    """
    Gets breaches for a specified account from the HIBP system, optionally restricting the returned results
    to a specified domain.

    :param account: The user's account name (such as an email address or a user-name). Default None.
    :param domain: The domain to check for breaches. Default None.
    :param truncate_response: If ``account`` is specified, truncates the response down to the breach names.
    Default False.
    :param include_unverified: If set to True, unverified breaches are included in the result. Default False.
    :return: A list object containing one or more dict objects, based on the information being requested,
    provided there was matching information. Boolean False returned if no information was found according to
    the HIBP API.
    """
    # Account/Domain don't need to be specified, but they must be text if so.
    if account is None or not isinstance(account, six.string_types):
        raise AttributeError("The account parameter must be specified, and must be a string")
    if domain is not None and not isinstance(domain, six.string_types):
        raise AttributeError("The domain parameter, if specified, must be a string")

    # Build the URI
    uri = HIBP_API_BASE_URI + HIBP_API_ENDPOINT_BREACHED_ACCT + account
    headers = {'user-agent': pyHIBP_USERAGENT}

    # Build the query string payload (requests drops params when None)
    # (and the HIBP backend ignores those that don't apply)
    query_string_payload = {
        "domain": domain,
        "truncateResponse": truncate_response,
        "includeUnverified": include_unverified,
    }
    resp = requests.get(url=uri, params=query_string_payload, headers=headers)
    if _process_response(response=resp):
        return resp.json()
    else:
        return False


def get_all_breaches(domain=None):
    """
    Returns a listing of all sites breached in the HIBP database.

    :param domain: Optional, default None. If specified, get all breaches for the domain with the specified name.
    :return: A list object containing one or more dict objects if breaches are present. Returns Boolean False
    if ``domain`` is specified, but the resultant list would be length zero.
    """
    if domain is not None and not isinstance(domain, six.string_types):
        raise AttributeError("The domain parameter, if specified, must be a string")
    uri = HIBP_API_BASE_URI + HIBP_API_ENDPOINT_BREACHES
    headers = {'user-agent': pyHIBP_USERAGENT}
    query_string_payload = {'domain': domain}
    resp = requests.get(url=uri, params=query_string_payload, headers=headers)
    # The API will return HTTP200 even if resp.json is length zero.
    if _process_response(response=resp) and len(resp.json()) > 0:
        return resp.json()
    else:
        return False


def get_single_breach(breach_name=None):
    """
    Returns a single breach's information from the HIBP's database.

    :param breach_name: The breach to retrieve. Required.
    :return: A dict object containing the information for the specified breach name, if it exists in the HIBP
    database. Boolean False is returned if the specified breach was not found.
    """
    if not isinstance(breach_name, six.string_types):
        raise AttributeError("The breach_name must be specified, and be a string")
    uri = HIBP_API_BASE_URI + HIBP_API_ENDPOINT_BREACH_SINGLE + breach_name
    headers = {'user-agent': pyHIBP_USERAGENT}
    resp = requests.get(url=uri, headers=headers)
    if _process_response(response=resp):
        return resp.json()
    else:
        return False


def get_pastes(email_address=None):
    """
    Retrieve all pastes for a specified email address.

    :param email_address: The email address to search. Required.
    :return: A list object containing one or more dict objects corresponding to the pastes the specified email
    address was found in. Boolean False returned if no pastes are detected for the given account.
    """
    if not isinstance(email_address, six.string_types):
        raise AttributeError("The email address supplied must be provided, and be a string")
    uri = HIBP_API_BASE_URI + HIBP_API_ENDPOINT_PASTES + email_address
    headers = {'user-agent': pyHIBP_USERAGENT}
    resp = requests.get(url=uri, headers=headers)
    if _process_response(response=resp):
        return resp.json()
    else:
        return False


def get_data_classes():
    """
    Retrieves all available data classes from the HIBP API.

    :return: A list object containing available data classes, corresponding to attributes found in breaches.
    A given breach will have one or more of the data classes in the list.
    """
    uri = HIBP_API_BASE_URI + HIBP_API_ENDPOINT_DATA_CLASSES
    headers = {'user-agent': pyHIBP_USERAGENT}
    resp = requests.get(url=uri, headers=headers)
    if _process_response(response=resp):
        return resp.json()
    else:
        # This path really shouldn't return false
        raise RuntimeError("HIBP API returned HTTP404 on a request for data classes.")


def is_password_breached(password=None, sha1_hash=None):
    """
    __DEPRECATED__: Use ``pwnedpasswords.is_password_breached`` instead, which contains additional functionality.

    Checks the HIBP breached password corpus for a breached password. Only the password or sha1_hash
    parameter is required to be set.

    Note that while the HIBP endpoint does have a originalPasswordIsAHash parameter, passwords submitted
    to this function will successfully process a supplied SHA1 hash password, since we pre-hash on our end.

    :param password: The raw password to check. Will be converted to a SHA1 hash prior to submission.
    :param sha1_hash: The SHA1 hash of the password to check.
    :return: True if the password was in the HIBP password corpus, otherwise False.
    """
    warnings.warn("Deprecation Warning: is_password_breached has moved to the pwnedpasswords module.")

    # Partially re-implement parameter checks to handle this deprecated function wrapper.
    if not password and not sha1_hash:
        raise AttributeError("You must provide either a password or sha1_hash.")

    # Pass the variables through to the new function...
    resp = pw.is_password_breached(password=password, sha1_hash=sha1_hash)

    if resp:
        # If the response is greater than zero
        return True
    else:
        return False
