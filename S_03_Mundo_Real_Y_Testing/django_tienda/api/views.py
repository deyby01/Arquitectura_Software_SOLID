from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from src.tienda.application.services import OrdenService

# Creamos una vista basada en clase con DRF
class OrdenView(APIView):
    
    # El decorador @inject dice al contenedor que debe inyectar las dependencias que declaremos
    @inject
    def post(self,
            request,
            orden_service: OrdenService = Provide[Container.orden_service]):
        """
        Crea una nueva orden.
        """

        # El 'orden_service' que recibimos ya esta completamente configurado con el DjangoOrdenRepository, listo para usar
        nueva_orden = orden_service.crear_nueva_orden()

        print(f"VISTA: Servicio creó la orden con ID #{nueva_orden.id}")

        # Devolvemos una respuesta HTTP exitosa
        return Response(
            {"id": nueva_orden.id, "mensaje": "Orden creada exitosamente."},
            status=status.HTTP_201_CREATED
        )