from django.urls import path, include
from rest_framework import routers
from app.views import EnderecoViewSet, CadastroViewSet, FilmeViewSet, LocacaoViewSet, AvaliacaoViewSet, DevolucaoViewSet

router = routers.DefaultRouter()
router.register(r'endereco', EnderecoViewSet)
router.register(r'cadastro', CadastroViewSet)
router.register(r'filme', FilmeViewSet)
router.register(r'locacao', LocacaoViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)
router.register(r'devolucao', DevolucaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
