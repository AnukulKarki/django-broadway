
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

class ListUpdateViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    pass

class ListCreateRetriveViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    pass