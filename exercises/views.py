from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets
from rest_framework.mixins import Response
from rest_framework.pagination import PageNumberPagination

from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer


class ExercisePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "prev": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "result": data,
            }
        )


@extend_schema(tags=["Exercise"])
class ExerciseViewSet(viewsets.ModelViewSet):
    """Представлениe для реализации CRUD для модели Exercise"""

    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    pagination_class = ExercisePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type_exercise", "difficulty"]
    permission_classes = [permissions.IsAuthenticated]
