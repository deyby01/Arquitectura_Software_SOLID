from dependency_injector import containers, providers
from src.tienda.application.services import OrdenService
from src.tienda.adapters.django_orm import DjangoOrdenRepository

class Container(containers.DeclarativeContainer):

    # El 'wiring' nos permite inyectar dependencias en funciones o vistas de Django
    wiring_config = containers.WiringConfiguration(modules=["api.views"])

    # ----- Adaptadores (Bajo Nivel) -----
    # El provider.Factory significa que se creara una nueva instancia cada vez que se pida
    orden_repository = providers.Factory(
        DjangoOrdenRepository
    )

    # ----- Servicios (Alto Nivel) -----
    # Fijate como le decimos que su 'orden_repository' sera el que definimos arriba.
    orden_service = providers.Factory(
        OrdenService,
        orden_repository=orden_repository
    )