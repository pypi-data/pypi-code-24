import inspect


__all__ = ["get_signal", "on_signal", "off_signal", "fire_signal", "add_signal"]


def get_signal(obj, signal_type):
    """Return a list of callback functions that are connected to the signal."""
    try:
        sig = obj.event_signals[signal_type]
        return [func for func in sig]
    except (KeyError, AttributeError) as error:
        raise ValueError("Invalid 'signal_type' given ({:s}). Cannot connect a function to this "
                         "signal.".format(repr(signal_type))) from error


def on_signal(obj, signal_type, func):
    """Connect a callback function to a signal."""
    try:
        sig = obj.event_signals[signal_type]
        if func not in sig:
            sig.append(func)
    except (KeyError, AttributeError):
        if not hasattr(obj, "event_signals"):
            obj.event_signals = {}
        obj.event_signals[signal_type] = [func]


def off_signal(obj, signal_type, func):
    """Disconnect a callback function from a signal."""
    try:
        sig = obj.event_signals[signal_type]
        existed = func in sig
        if func is None:
            sig.clear()
        else:
            try:
                sig.remove(func)
            except:
                pass
        return existed
    except (KeyError, AttributeError):
        return False


def fire_signal(obj, signal_type, *args, **kwargs):
    """Call all fo the callback functions for a signal."""
    try:
        sig = obj.event_signals[signal_type]
    except (KeyError, AttributeError) as error:
        sig = []
        raise ValueError("Invalid 'signal_type' given ({:s}). Cannot connect a function to this "
                         "signal.".format(repr(signal_type))) from error

    for func in sig:
        func(*args, **kwargs)


def add_signal(obj, signal_type, assign_signal_functions=True):
    """Add a 'signal_type' to an object.

    Warning:
        If a class is given the signal will be added as a class variable. All instances will share the signals.

    Example:

        ..code-block:: python

            >>> # Decorator example
            >>> item = MyClass()
            >>> add_signal(item, "custom_notifier")
            >>> item.on("custom_notifier", lambda *args: print(*args))
            >>> item.fire("custom_notifier", "Hello World!")

    Args:
        signal_type(str): String signal name.
        obj (object)[None]: Object that will have the signal items added to it.
            If an object is not given this function works as a decorator.
        assign_signal_functions (bool)[True]: Add methods 'get_signal', 'on', 'off', and 'fire'.
    """
    # Add normal signal methods
    if assign_signal_functions:
        if not hasattr(obj, "get_signal"):
            obj.get_signal = get_signal.__get__(obj, obj.__class__)
        if not hasattr(obj, "on"):
            obj.on = on_signal.__get__(obj, obj.__class__)
        if not hasattr(obj, "off"):
            obj.off = off_signal.__get__(obj, obj.__class__)
        if not hasattr(obj, "fire"):
            obj.fire = fire_signal.__get__(obj, obj.__class__)

    # Add signal dictionary
    if not hasattr(obj, "event_signals"):
        obj.event_signals = {}
    if signal_type not in obj.event_signals:
        obj.event_signals[signal_type] = []

    return obj
