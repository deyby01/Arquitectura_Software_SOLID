# 🧠 Día 9: Introducción a la Arquitectura Hexagonal

Ayer aislamos nuestra lógica de negocio en una "Capa de Servicios". La **Arquitectura Hexagonal**, también conocida como **Puertos y Adaptadores**, lleva esa idea al siguiente nivel.

## 🎯 El objetivo

Crear un "**núcleo**" de aplicación que sea completamente independiente y agnóstico de la tecnología externa. A tu lógica de negocio no le debe importar si la usa una aplicación web, una app móvil, si los datos se guardan en PostgreSQL o en un archivo de texto.

## 🔑 Los Tres Componentes Clave

> 💡 Imagina tu aplicación como un sistema de cine en casa.

### 1️⃣ El Hexágono (El Núcleo / El Amplificador 앰프)

* Es el **corazón** de tu aplicación. Contiene toda la lógica de negocio pura (tus servicios, tus modelos de dominio como `Orden`)
* No sabe nada del mundo exterior. No contiene código de Django, ni de SQLAlchemy, ni de APIs. Es solo **Python puro**

### 2️⃣ Los Puertos (Los Enchufes HDMI, USB, etc. 포트)

* Son las "**puertas**" de entrada y salida de tu núcleo, definidas por el propio núcleo
* Son los **contratos** entre el núcleo y el exterior
* En Python, nuestros puertos son las **Clases Base Abstractas** (`ABCs`) que ya hemos estado usando

#### Tipos de Puertos

1. **Puertos Primarios** (o de Conducción):
   * Son la API de nuestro núcleo
   * Definen lo que el mundo exterior puede hacer con nuestra aplicación
   * Ejemplo: los métodos en `UserService`

2. **Puertos Secundarios** (o Conducidos):
   * Definen lo que nuestra aplicación necesita del mundo exterior
   * Ejemplo: `MetodoPago`, `INotificacion`, `IProductoRepository`

### 3️⃣ Los Adaptadores (El Chromecast, la PlayStation, etc. 어댑터)

* Son el "**cableado**" que traduce la tecnología del mundo exterior al lenguaje simple de los puertos

#### Tipos de Adaptadores

1. **Adaptadores Primarios**:
   * Inician la comunicación
   * Ejemplo: Una vista de Django es un adaptador primario
   * Traduce una petición HTTP en una llamada a un puerto primario (un método de un servicio)

2. **Adaptadores Secundarios**:
   * Implementan los requisitos del núcleo
   * Ejemplo: La clase `PagoConTarjeta` es un adaptador secundario
   * Implementa la interfaz requerida por el puerto `MetodoPago`
   * La clase que guarda una orden en PostgreSQL es otro adaptador secundario

## ⚡️ Flash Recordatorio: Principio de Inversión de Dependencias (DIP)

> La Arquitectura Hexagonal es la **manifestación definitiva del DIP**. 

Las flechas de dependencia **siempre apuntan hacia el centro**, hacia el hexágono:
* Los detalles de **bajo nivel** (la base de datos) dependen de las abstracciones (los Puertos) definidas por el núcleo
* Los detalles de **alto nivel** (la interfaz de usuario) dependen de las abstracciones (los Puertos) definidas por el núcleo