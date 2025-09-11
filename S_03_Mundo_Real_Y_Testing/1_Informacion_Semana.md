Esta semana consiste en aprender lo que hemos estado viendo y como aplicarlo en un entorno real, o mas realista, trabajaremos con Django y Django Rest Framework, pero nos seguiremos basando en nuestra arquitectura Hexagonal, para eso tener en cuenta lo siguiente: 
- Todo el proyecto de la semana sera `django_tienda/`
- Iniciaremos un proyecto nuevo en la carpeta con django: django-admin startproject config .
- crearemos una app llamada `api` con django: python manage.py startapp api
- Copiar todo el contenido de la carpeta `src/` de la semana 2 del proyecto `tienda_hexagonal/`
- registraremos nuestra app en settings.py en INSTALLED_APPS que seriam: 'api' y 'rest_framework'
