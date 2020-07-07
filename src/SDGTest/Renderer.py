from rest_framework import renderers
from rest_framework.decorators import parser_classes 


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        return data.encode(self.charset)

# class PlainTextParser(BaseParser):
#     """
#     Plain text parser.
#     """
#     media_type = 'text/plain'

#     def parse(self, stream, media_type=None, parser_context=None):
#         """
#         Simply return a string representing the body of the request.
#         """
#         return stream.read()