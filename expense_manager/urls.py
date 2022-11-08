from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from categories.views import CategoryViewSet
from transactions.views import TransactionViewSet
from users.views import UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, "users")
router.register("categories", CategoryViewSet, "categories")
router.register("transactions", TransactionViewSet, "transactions")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
]
