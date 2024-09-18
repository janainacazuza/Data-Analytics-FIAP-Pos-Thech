class CustomException(Exception):
    def __init__(self, message, errors=None):
        """
        Custom exception class to capture more detailed error information.
        Args:
            message (str): Custom error message.
            errors (Exception, optional): Additional exception details.
        """
        super().__init__(message)
        self.errors = errors
        self.message = message

    def __str__(self):
        """
        Return the string representation of the exception, which includes the custom message and any additional errors.
        """
        if self.errors:
            return f"{self.message} - {self.errors}"
        else:
            return self.message

