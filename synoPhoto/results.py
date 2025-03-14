"""


"""

class ResultsReports:

    def __init__(self):

        self._FILE_MOVED = False
        self._IS_ERROR = False

    def _set_value(self, file_moved: bool, is_error: bool):
        self._FILE_MOVED = file_moved
        self._IS_ERROR = is_error

    def log_file_move(self):
        self._FILE_MOVED = True

    @property
    def has_moved(self) -> bool:
        return self._FILE_MOVED

    def log_error(self):
        self._IS_ERROR = True

    @property
    def has_error(self) -> bool:
        return self._IS_ERROR


    def __add__(self, other):
        is_error = self.has_error or other.has_error
        file_moved = self.has_moved or other.has_moved
        new_report = ResultsReports()

        new_report._set_value(file_moved=file_moved,
                              is_error=is_error
                              )
        return new_report

    def __repr__(self):
        return f"Error: {self.has_error} Moved: {self.has_moved}"