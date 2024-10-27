import fastapi
from routes.routes_schools import router as router_schools
from routes.routes_classes import router as router_classes
from routes.routes_teachers import router as router_teachers
from routes.routes_students import router as router_students

main_router = fastapi.APIRouter()

main_router.include_router(router_schools)
main_router.include_router(router_classes)
main_router.include_router(router_teachers)
main_router.include_router(router_students)