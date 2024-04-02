"""Hotel Management Exception Class"""


class HotelManagementException(Exception):
    """Exception for errors in hotel manager"""

    def __init__(self, message):
        self.errorMessage = message
        super().__init__(self.message)

    @property
    def message(self):
        """Returns error message"""
        return self.errorMessage

    @message.setter
    def message(self, value):
        self.errorMessage = value
