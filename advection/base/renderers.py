from rest_framework.renderers import JSONRenderer


class AdvectionApiRenderer(JSONRenderer):
    media_type = 'application/vnd.advection+json'
