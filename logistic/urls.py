from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, ProductStockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('positions', ProductStockViewSet)

urlpatterns = router.urls