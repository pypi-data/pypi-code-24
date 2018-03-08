"""Search expired users extended API method."""
from ibsng.handler.handler import Handler


class searchExpiredUsersExtended(Handler):
    """Search expired users extended method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.conds, dict)
        self.is_valid(self.from_, int)
        self.is_valid(self.to_, int)
        self.is_valid(self.order_by, str)
        self.is_valid(self.desc, bool)

    def setup(self, conds, from_, to_, order_by, desc):
        """Setup required parameters.

        :param dict conds: conditions
        :param int from: start index, for pagination
        :param int to: start index, for pagination
        :param choice order_by: order by specific field
        :param bool desc: descending

        :return: None
        :rtype: None
        """
        self.conds = conds
        self.from_ = from_
        self.to_ = to_
        self.order_by = order_by
        self.desc = desc
