import json
from collections import abc


def load_profiles(strings):
    """Load profiles from a list of strings

    Parameters
    ----------
    strings : [str]
        A list of strings that are file names or json, and represent either a
        single profile or a list of profiles.

    Returns
    -------
    prof_gen : (prof)
        A generator of json profiles.
    """
    for prof_type in strings:
        # Try to load file else read as string
        try:
            with open(prof_type) as f:
                prof = json.load(f)
        except FileNotFoundError:
            prof = json.loads(prof_type)
        # Yield different amounts if it's a list
        if isinstance(prof, abc.Mapping):
            yield prof
        else:
            for p in prof:
                yield p
