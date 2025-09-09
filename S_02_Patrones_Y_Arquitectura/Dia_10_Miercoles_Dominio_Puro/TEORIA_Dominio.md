# 🧠 Día 10: El Corazón del Hexágono (El Dominio)

Hoy nos enfocamos en la parte más importante de la **Arquitectura Hexagonal**: el núcleo de la aplicación, también conocido como la **capa de Dominio**.

## 🚗 Analogía del Motor

> Piensa en el Dominio como el **motor de un coche**. 

Es la pieza de ingeniería compleja que contiene toda la lógica de cómo funciona el coche. No sabe nada de la carrocería, el color de la pintura, el tipo de ruedas o la marca de la radio. Es **completamente independiente**.

## 📁 Estructura en el Código

En nuestro código, el Dominio es una carpeta que contiene toda nuestra lógica de negocio en su forma más pura.

### 🔑 La Regla de Oro

> Los archivos dentro de esta carpeta **no pueden importar nada de frameworks externos**.

* Nada de Django
* Nada de FastAPI
* Nada de SQLAlchemy
* Solo **Python puro**

## ❓ ¿Qué Vive Dentro del Dominio?

### 1️⃣ Modelos de Dominio (Entidades)

* Son las clases que representan los **conceptos clave del negocio**
* En nuestro caso: `Orden`, `Libro`, `CursoOnline`
* No son solo contenedores de datos; también contienen **lógica que les pertenece intrínsecamente**
  * Ejemplo: el método `agregar_item` pertenece a la `Orden`

### 2️⃣ Puertos

* Las definiciones de los puertos (nuestras `ABCs`) que diseñamos ayer también viven aquí
* El núcleo define los "enchufes" que necesita
* **Ejemplos**: `MetodoPago`, `INotificacion`, `IOrdenRepository`

## ⚡️ Flash Recordatorio: SRP y DIP

Esta estricta separación es una aplicación a gran escala del **SRP** y el **DIP**:

* Cada parte (modelos, puertos) tiene una **responsabilidad única** (SRP)
* Todo dependerá de las **abstracciones** (puertos) que definamos aquí, en el corazón de todo (DIP)
* El dominio es el centro de la arquitectura y no depende de nada externo