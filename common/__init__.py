from werkzeug.routing import BaseConverter

from .schemas import *
from .validations import *


class BooleanConverter(BaseConverter):
    regex = r"(?:yes|no)"

    def __init__(self, url_map):
        super(BooleanConverter, self).__init__(url_map)

    def to_python(self, value):
        return value == 'yes'

    def to_url(self, value):
        return "yes" if value else "no"
