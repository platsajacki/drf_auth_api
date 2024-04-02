from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view

id_parameter = OpenApiParameter('id', OpenApiTypes.INT, OpenApiParameter.PATH)

extend_schema_user_view_set = extend_schema_view(
    list=extend_schema(operation_id='user_list', description='Get list of users.'),
    retrieve=extend_schema(parameters=[id_parameter], description='Get details of a user.'),
    partial_update=extend_schema(parameters=[id_parameter], description='Update a user.'),
    destroy=extend_schema(parameters=[id_parameter], description='Delete a user.'),
)
