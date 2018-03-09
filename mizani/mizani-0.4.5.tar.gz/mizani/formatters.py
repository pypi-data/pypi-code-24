"""
Scales have guides and these are what help users make sense of
the data mapped onto the scale. Common examples of guides include
the x-axis, the y-axis, the keyed legend and a colorbar legend.
The guides have demarcations(breaks), some of which must be labelled.

The `*_format` functions below create functions that convert data
values as understood by a specific scale and return string
representations of those values. Manipulating the string
representation of a value helps improve readability of the guide.
"""
from __future__ import division
import re
from warnings import warn

import numpy as np
from matplotlib.dates import DateFormatter, date2num
from matplotlib.ticker import ScalarFormatter

from .breaks import timedelta_helper
from .utils import round_any, precision, is_close_to_int
from .utils import same_log10_order_of_magnitude


__all__ = ['custom_format', 'currency_format', 'dollar_format',
           'percent_format', 'scientific_format', 'date_format',
           'mpl_format', 'log_format', 'timedelta_format']


class custom_format(object):
    """
    Custom format

    Parameters
    ----------
    fmt : str, optional
        Format string. Default is the generic new style
        format braces, `\{\}`.
    style : 'new' | 'old'
        Whether to use new style or old style formatting.
        New style uses the :meth:`str.format` while old
        style uses ``%``. The format string must be written
        accordingly.

    Examples
    --------
    >>> formatter = custom_format('{:.2f} USD')
    >>> formatter([3.987, 2, 42.42])
    ['3.99 USD', '2.00 USD', '42.42 USD']
    """
    def __init__(self, fmt='{}', style='new'):
        self.fmt = fmt
        self.style = style

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        if self.style == 'new':
            return [self.fmt.format(val) for val in x]
        elif self.style == 'old':
            return [self.fmt % val for val in x]
        else:
            raise ValueError(
                "style should be either 'new' or 'old'")


# formatting functions
class currency_format(object):
    """
    Currency formatter

    Parameters
    ----------
    prefix : str
        What to put before the value.
    suffix : str
        What to put after the value.
    digits : int
        Number of significant digits
    big_mark : str
        The thousands separator. This is usually
        a comma or a dot.

    Examples
    --------
    >>> x = [1.232, 99.2334, 4.6, 9, 4500]
    >>> currency_format()(x)
    ['$1.23', '$99.23', '$4.60', '$9.00', '$4500.00']
    >>> currency_format('C$', digits=0, big_mark=',')(x)
    ['C$1', 'C$99', 'C$5', 'C$9', 'C$4,500']
    """
    def __init__(self, prefix='$', suffix='', digits=2, big_mark=''):
        self.prefix = prefix
        self.suffix = suffix
        self.digits = digits
        self.big_mark = big_mark

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        # create {:.2f} or {:,.2f}
        big_mark = self.big_mark
        comma = ',' if big_mark else ''
        tpl = ''.join((self.prefix, '{:', comma, '.',
                       str(self.digits), 'f}', self.suffix))

        labels = [tpl.format(val) for val in x]
        if big_mark and big_mark != ',':
            labels = [val.replace(',', big_mark) for val in labels]
        return labels


dollar_format = currency_format
dollar = dollar_format()


class comma_format(object):
    """
    Format number with commas separating thousands

    Parameters
    ----------
    digits : int
        Number of digits after the decimal point.

    Examples
    --------
    >>> comma_format()([1000, 2, 33000, 400])
    ['1,000', '2', '33,000', '400']
    """
    def __init__(self, digits=0):
        self.formatter = currency_format(
            prefix='', digits=digits, big_mark=',')

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        return self.formatter(x)


class percent_format(object):
    """
    Percent formatter

    Multiply by one hundred and display percent sign

    Parameters
    ----------
    use_comma : bool
        If True, use a comma to separate the thousands.
        Default is False.

    Examples
    --------
    >>> formatter = percent_format()
    >>> formatter([.45, 9.515, .01])
    ['45%', '952%', '1%']
    >>> formatter([.654, .8963, .1])
    ['65.4%', '89.6%', '10.0%']
    """
    def __init__(self, use_comma=False):
        self.big_mark = ',' if use_comma else ''

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        if len(x) == 0:
            return []

        _precision = precision(x)
        x = round_any(x, _precision / 100) * 100

        # When the precision is less than 1, we show
        if _precision > 1:
            digits = 0
        else:
            digits = abs(int(np.log10(_precision)))

        formatter = currency_format(prefix='',
                                    suffix='%',
                                    digits=digits,
                                    big_mark=self.big_mark)
        labels = formatter(x)
        # Remove unnecessary zeros after the decimal
        pattern = re.compile(r'\.0+%$')
        if all(pattern.search(val) for val in labels):
            labels = [pattern.sub('%', val) for val in labels]
        return labels


percent = percent_format()


class scientific_format(object):
    """
    Scientific formatter

    Parameters
    ----------
    digits : int
        Significant digits.

    Examples
    --------
    >>> x = [.12, .23, .34, 45]
    >>> scientific_format()(x)
    ['1.2e-01', '2.3e-01', '3.4e-01', '4.5e+01']

    Notes
    -----
    Be careful when using many digits (15+ on a 64
    bit computer). Consider of the `machine epsilon`_.

    .. _machine epsilon: https://en.wikipedia.org/wiki/Machine_epsilon
    """
    def __init__(self, digits=3):
        tpl = ''.join(['{:.', str(digits), 'e}'])
        self.formatter = custom_format(tpl)

    def __call__(self, x):
        if len(x) == 0:
            return []

        zeros_re = re.compile(r'(0+)e')

        def count_zeros(s):
            match = zeros_re.search(s)
            if match:
                return len(match.group(1))
            else:
                return 0

        # format and then remove superfluous zeros
        labels = self.formatter(x)
        n = min([count_zeros(val) for val in labels])
        if n:
            labels = [val.replace('0'*n+'e', 'e') for val in labels]
        return labels


scientific = scientific_format()


def _format(formatter, x):
    """
    Helper to format and tidy up
    """
    # For MPL to play nice
    formatter.create_dummy_axis()
    # For sensible decimal places
    formatter.set_locs([val for val in x if ~np.isnan(val)])
    try:
        oom = int(formatter.orderOfMagnitude)
    except AttributeError:
        oom = 0
    labels = [formatter(tick) for tick in x]

    # Remove unnecessary decimals
    pattern = re.compile(r'\.0+$')
    for i, label in enumerate(labels):
        match = pattern.search(label)
        if match:
            labels[i] = pattern.sub('', label)

    # MPL does not add the exponential component
    if oom:
        labels = ['{}e{}'.format(s, oom) if s != '0' else s
                  for s in labels]
    return labels


class mpl_format(object):
    """
    Format using MPL formatter for scalars

    Examples
    --------
    >>> mpl_format()([.654, .8963, .1])
    ['0.6540', '0.8963', '0.1000']
    """
    def __init__(self):
        self.formatter = ScalarFormatter(useOffset=False)

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        return _format(self.formatter, x)


class log_format(object):
    """
    Log Formatter

    Parameters
    ----------
    base : int
        Base of the logarithm. Default is 10.
    exponent_threshold : int
        Difference between the minimum and maximum values
        of the data beyond which exponent notation will
        be used. Default is 5.

    Examples
    --------
    >>> log_format()([0.001, 0.1, 100])
    ['0.001', '0.1', '100']

    >>> log_format()([0.001, 0.1, 1000])
    ['1e-3', '1e-1', '1e3']
    """
    def __init__(self, base=10, exponent_threshold=5):
        self.base = base
        self.exponent_threshold = exponent_threshold

    def _num_to_string(self, x, use_exponent):
        """
        Parameters
        ----------
        x : float
            Number to represent as string
        use_exponent : bool
            Difference in exponents between max and min.
        """
        if use_exponent:
            fmt = '{:1.0e}'
        else:
            fmt = '{}'

        s = fmt.format(x)

        # Tidy up, remove unnecessary +ve signs
        # e.g 1e+00 -> 1
        #     1e+3 -> 1e3
        if use_exponent:
            tup = s.split('e')
            if len(tup) == 2:
                mantissa = tup[0].rstrip('0').rstrip('.')
                exponent = int(tup[1])
                if exponent:
                    s = '%se%d' % (mantissa, exponent)
                else:
                    s = mantissa
        return s

    def _format_num(self, x, use_exponent):
        """
        Return the format for tick val `x`.

        Parameters
        ----------
        x : float
            Number to format
        use_exponent : bool
            If True, used exponent notation.

        Returns
        -------
        out : str
            Formatted number.
        """
        if x == 0.0:  # Symlog
            return '0'

        x = abs(x)

        # only label the decades
        if self.base == 10 and use_exponent:
            fx = np.log(x) / np.log(self.base)
            is_x_decade = is_close_to_int(fx)

            if not is_x_decade:
                return ''

        s = self._num_to_string(x, use_exponent)
        return (s)

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        if len(x) == 0:
            return []

        # Decide on using exponents
        if self.base == 10:
            # Order of magnitude of the minimum and maximum
            dmin = np.log(np.min(x))/np.log(self.base)
            dmax = np.log(np.max(x))/np.log(self.base)
            if same_log10_order_of_magnitude((dmin, dmax)):
                return mpl_format()(x)

            has_small_number = dmin < -3
            has_large_number = dmax > 3
            has_large_range = (dmax - dmin) > self.exponent_threshold
            use_exponent = (has_small_number or
                            has_large_number or
                            has_large_range)
        else:
            use_exponent = False
        return [self._format_num(num, use_exponent) for num in x]


class date_format(object):
    """
    Datetime formatter

    Parameters
    ----------
    fmt : str
        Format string. See
        :ref:`strftime <strftime-strptime-behavior>`.
    tz : datetime.tzinfo, optional
        Time zone information. If none is specified, the
        time zone will be that of the first date. If the
        first date has no time information then a time zone
        is chosen by other means.

    Examples
    --------
    >>> import pytz
    >>> from datetime import datetime
    >>> x = [datetime(x, 1, 1) for x in [2010, 2014, 2018, 2022]]
    >>> date_format()(x)
    ['2010-01-01', '2014-01-01', '2018-01-01', '2022-01-01']
    >>> date_format('%Y')(x)
    ['2010', '2014', '2018', '2022']

    Can format time

    >>> x = [datetime(2017, 12, 1, 16, 5, 7)]
    >>> date_format("%Y-%m-%d %H:%M:%S")(x)
    ['2017-12-01 16:05:07']

    Time zones are respected

    >>> utc = pytz.timezone('UTC')
    >>> ug = pytz.timezone('Africa/Kampala')
    >>> x = [datetime(2010, 1, 1, i) for i in [8, 15]]
    >>> x_tz = [datetime(2010, 1, 1, i, tzinfo=ug) for i in [8, 15]]
    >>> date_format('%Y-%m-%d %H:%M')(x)
    ['2010-01-01 08:00', '2010-01-01 15:00']
    >>> date_format('%Y-%m-%d %H:%M')(x_tz)
    ['2010-01-01 08:33', '2010-01-01 15:33']

    Format with a specific time zone

    >>> date_format('%Y-%m-%d %H:%M', tz=utc)(x_tz)
    ['2010-01-01 05:33', '2010-01-01 12:33']
    """
    def __init__(self, fmt='%Y-%m-%d', tz=None):
        self.formatter = DateFormatter(fmt, tz=tz)
        self.tz = tz

    def __call__(self, x):
        """
        Format a sequence of inputs

        Parameters
        ----------
        x : array
            Input

        Returns
        -------
        out : list
            List of strings.
        """
        # Formatter timezone
        if self.tz is None and len(x):
            tz = self.formatter.tz = x[0].tzinfo

            if not all(value.tzinfo == tz for value in x):
                msg = ("Dates have different time zones. "
                       "Choosen `{}` the time zone of the first date. "
                       "To use a different time zone, create a "
                       "formatter and pass the time zone.")
                warn(msg.format(tz.zone))

        # The formatter is tied to axes and takes
        # breaks in ordinal format.
        x = [date2num(val) for val in x]
        return _format(self.formatter, x)


class timedelta_format(object):
    """
    Timedelta formatter

    Parameters
    ----------
    units : str, optional
        The units in which the breaks will be computed.
        If None, they are decided automatically. Otherwise,
        the value should be one of::

            'ns'    # nanoseconds
            'us'    # microseconds
            'ms'    # milliseconds
            's'     # secondss
            'm'     # minute
            'h'     # hour
            'd'     # day
            'w'     # week
            'M'     # month
            'y'     # year

    add_units : bool
        Whether to append the units identifier string
        to the values.
    usetext : bool
        If True, they microseconds identifier string is
        rendered with greek letter *mu*. Default is False.

    Examples
    --------
    >>> from datetime import timedelta
    >>> x = [timedelta(days=31*i) for i in range(5)]
    >>> timedelta_format()(x)
    ['0', '1 month', '2 months', '3 months', '4 months']
    >>> timedelta_format(units='d')(x)
    ['0', '31 days', '62 days', '93 days', '124 days']
    >>> timedelta_format(units='d', add_units=False)(x)
    ['0', '31', '62', '93', '124']
    """
    abbreviations = {
        'ns': 'ns',
        'us': 'us',
        'ms': 'ms',
        's': 's',
        'm': ' minute',
        'h': ' hour',
        'd': ' day',
        'w': ' week',
        'M': ' month',
        'y': ' year'}

    def __init__(self, units=None, add_units=True, usetex=False):
        self.units = units
        self.add_units = add_units
        self.usetex = usetex
        self._mpl_format = mpl_format()

    def __call__(self, x):
        if len(x) == 0:
            return []

        labels = []
        values, _units = timedelta_helper.format_info(x, self.units)
        plural = '' if _units.endswith('s') else 's'
        ulabel = self.abbreviations[_units]
        if ulabel == 'us' and self.usetex:
            ulabel = '$\mu s$'
        _labels = self._mpl_format(values)

        if not self.add_units:
            return _labels

        for num, num_label in zip(values, _labels):
            s = '' if num == 1 else plural
            # 0 has no units
            _ulabel = '' if num == 0 else ulabel+s
            labels.append(''.join([num_label, _ulabel]))

        return labels
