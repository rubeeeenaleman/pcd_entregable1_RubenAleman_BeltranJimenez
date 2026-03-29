# 🌌 Gestor Logístico del Imperio Galáctico

Sistema de gestión de inventario y logística naval desarrollado en Python. Este proyecto simula la red de suministros del Imperio Galáctico, gestionando almacenes, operarios, comandantes y el stock de piezas para diferentes naves y estaciones espaciales (como la Estrella de la Muerte o los Cazas TIE).

---

## 🚀 Características Principales

* **Arquitectura Orientada a Objetos (POO):** Uso de herencia, clases abstractas y polimorfismo para modelar la jerarquía de la flota imperial (`NaveEstelar`, `CazaEstelar`, `EstacionEspacial`).
* **Algoritmo Voraz (Greedy):** Implementación de un algoritmo de optimización en las compras del Alto Mando. El sistema siempre busca y adquiere primero los repuestos más baratos disponibles en toda la galaxia antes de recurrir a los caros.
* **Gestión de Excepciones:** Control de errores robusto con excepciones personalizadas (`ErrorRepuestoNoEncontrado`, `ErrorStockInsuficiente`) para evitar caídas del sistema ante peticiones de material críticas.
* **Testing Automatizado:** Batería de pruebas unitarias implementada con `pytest` para asegurar la fiabilidad de las operaciones en los almacenes y la lógica de negocio.

---

## 🏗️ Estructura del Sistema

El proyecto se divide en las siguientes entidades principales:

1. **Usuarios del Sistema:**
   * **Comandante:** Encargado de su nave. Puede consultar disponibilidad, precios y comprar repuestos a nivel galáctico.
   * **Operario:** Encargado de un almacén físico. Gestiona el alta, baja, modificación y transferencia interplanetaria de stock.
2. **Flota Imperial:** Jerarquía de naves y unidades de combate basadas en clases abstractas.
3. **Infraestructura:** Clases `Almacen` y `Repuesto` que gestionan el catálogo físico mediante listas de objetos.

---
