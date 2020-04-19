# Third Party Stuff
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    title="advection API",
    description="django based web backend for AFrOST website",
    public=True,
    permission_classes=[AllowAny],
)

swagger_schema_view = get_swagger_view(title="advection API Playground")
