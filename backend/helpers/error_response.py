from rest_framework.renderers import JSONRenderer
from rest_framework.response import responses


def error_response(error_msg, status):
    response= responses({'error': error_msg}, status=status)
    response.accepted_renderer= JSONRenderer
    response.accepted_media_type = 'applicatiom/json'
    response.renderer_context = {}
    return response