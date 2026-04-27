# Plataforma de Tienda en Línea

Sistema modular de comercio electrónico compuesto por un panel de administración, una tienda pública y una API REST para integraciones externas.

---

## Visión General

Este proyecto es una tienda en línea diseñada para la gestión y visualización de productos de una empresa comercial.

La plataforma está dividida en tres componentes principales:

- Panel de administración (Intranet)
- Tienda pública (Portal Web)
- API REST (Integración externa)

Todos los módulos comparten una base de datos centralizada para garantizar consistencia de la información.

---

## Panel de Administración

Sistema interno utilizado para gestionar el contenido de la tienda.

### Gestión de Productos
- Crear, editar y eliminar productos
- Subida de imágenes
- Asociación de productos a proveedores

### Gestión de Proveedores
- Registro y mantenimiento de proveedores
- Información básica de contacto

### Gestión de Usuarios
- Control de usuarios del sistema
- Roles y permisos basados en perfiles
- Bloqueo y activación de cuentas

---

## Tienda Web (Frontend Público)

Interfaz pública donde los clientes pueden explorar productos.

### Registro e Inicio de Sesión
- Registro de usuarios nuevos
- Creación automática de cuenta de cliente
- Autenticación estándar (login/logout)

### Catálogo de Productos
- Visualización tipo tienda moderna (grid o lista)
- Información mostrada:
  - Imagen del producto
  - Nombre
  - Descripción
  - Precio

Este módulo es solo de visualización. No incluye carrito ni proceso de pago.

---

## API REST

Interfaz para consumo de datos desde sistemas externos.

### Seguridad
- Autenticación basada en tokens (JWT o similar)

### Funcionalidades
- Acceso de solo lectura:
  - Listado de productos
  - Detalle de productos

---

## Arquitectura del Proyecto

El sistema está estructurado de forma modular para facilitar escalabilidad y mantenimiento:

- users: autenticación y gestión de cuentas
- products: lógica de catálogo
- store: lógica del frontend público
- api: servicios REST

---

## Lógica de Negocio

- Los productos son el núcleo del sistema
- La administración controla su disponibilidad y contenido
- La tienda solo consume y muestra la información
- La lógica se mantiene en el backend para asegurar consistencia

---

## Reglas del Sistema

- Los precios se almacenan en formato decimal
- No se utilizan tipos de punto flotante para valores monetarios
- El sistema prioriza precisión y consistencia en datos de negocio

---

## Futuras Mejoras

- Carrito de compras
- Sistema de pagos en línea
- Historial de pedidos
- Panel de analítica de ventas
- Recomendaciones de productos
