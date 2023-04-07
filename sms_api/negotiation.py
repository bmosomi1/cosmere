from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.parsers import BaseParser


class IgnoreClientContentNegotiation(BaseContentNegotiation):
    def select_parser(self, request, parsers):
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix=None):
        return renderers[0], renderers[0].media_type


class XMLParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/xml'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()