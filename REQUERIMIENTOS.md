# Documento de Análisis de Requerimientos y Diseño

**Proyecto:** Sistema Integrado de Inventario, Portal Web y API Externa

## 1.  Visión General del Proyecto

El sistema está diseñado para manejar la operativa básica de una empresa comercializadora. Se divide en tres  ecosistemas bien diferenciados que comparten una misma base de datos centralizada, asegurando la consistencia de la información.

##  Especificación de Requerimientos (Módulos)

### 2.1. Módulo A: Intranet (Backoffice / Administración) 

Este módulo está reservado para el personal interno de la empresa y se enfoca en la gestión operativa. 

* **Gestión de Proveedores (CRUD):**
  * Permite registrar, consultar, modificar y eliminar proveedores.
  * Datos mínimos requeridos: Nombre, correo electrónico y teléfono.
* **Gestión de Catálogo de Productos (CRUD):**
  * Permite la administración de los artículos a comercializar.
  * Soporta la carga de imágenes representativas del producto.
  * Requiere vincular obligatoriamente cada producto a un proveedor registrado.
* **Proceso de Recepción de Mercancía:**
  * Módulo transaccional para ingresar nuevo stock al almacén.
  * **Regla de negocio:** Al registrar una recepción, la existencia (stock) del producto asociado debe incrementarse automáticamente.
  * **Auditoria:** Debe registrarse la fecha, la cantidad recibida y el usuario interno que ejecutó la acción.
* **Administración de Usuarios (Internos y Externos):**
  * Se gestionan identidades centralizadas. Una persona puede ser asignada a diferentes perfiles.
  * Solo los usuarios con un Perfil catalogado como "Interno" (ej. Administrador, Almacenista) tienen acceso a esta Intranet.
  *  Los administradores pueden bloquear el acceso (is_active=False) a cualquier usuario, sea interno o 
cliente.

### 2.2. Módulo B: Portal Web (Catálogo Público) 
Plataforma orientada al cliente final para la visualización de la oferta comercial. 
* **Autenticación de Clientes (Usuarios Externos):**
  * Permite al usuarios públicos registrarse de forma autónoma.
  *  Al registrarse, el sistema crea un registro en PERSON, un USER y le asigna automáticamente el PERFIL por defecto de "Cliente" (Externo).
    * Sistema de login y logout estándar.
* **Vitrina de Productos (Estilo Amazon):**
    * Visualización de los productos en formato  cuadriculado o lista.
    * Muestra informacion esencial: Fotografia, Nombre, descripcion y precio.
    * Restricciones: Estrictamente informativo. Sin carrito ni ventas.
###  Módulo C: API REST (Interoperabilidad)
Interfaz de programación de aplicaciones para interactuar con sistemas de terceros. 
- **Autenticación Segura:** Acceso mediante validación de Tokens (ej. JWT).
- **Endpoints de Lectura (Read-Only):** Listado y detalle de productos disponibles.

## 3. Arquitectura de Datos (Diseño Conceptual)

Para soportar las operativas descritas, se define el siguiente modelo Entidad-Relación:

### 3.1. Entidades Principales (Basado en la separación de Identidad Física, Digital y Control de Acceso).

* PERSON (Identidad Física): Almacena datos como nombres, correos y contacto de cualquier ser humano en el sistema.
* **PERFIL (Roles y Permisos):** Define los tipos de usuarios que existen (ej. "Cliente Web", "Admin de 
Catálogo"). Contiene una bandera is_internal para separar radicalmente quién entra a la Intranet y 
quién se queda en el Portal Web.
* **USER (Identidad Digital):** Nodo central. Une a la Persona con su Perfil y almacena sus credenciales de acceso (usuario y contraseña).

 * **SUPPLIER (Proveedor) & PRODUCT (Producto):** Catálogo maestro y abastecimiento. PRODUCT guarda el stock consolidado.

 * **STOCK_RECEPTION (Recepción de Inventario):** Histórico transaccional de auditoría de inventario. 

## Notas de Implementación

* Framework: Django (Python). Se utilizará la arquitectura MVT.
* Separación de Aplicaciones: El proyecto se dividirá en apps lógicas (users, inventory, portal, api) para asegurar un bajo acoplamiento.
* Cálculo de Stock: La actualización del campo stock en la tabla PRODUCT se gestionará preferiblemente a través de
* Django Signals o sobrescribiendo el método save() de STOCK_RECEPTION, asegurando que la lógica de negocio se mantenga a nivel de modelo (Fat Models, Thin Views).
* Autenticación Personalizada: En Django, deberemos crear un modelo de usuario personalizado que
* apunte a estas relaciones (AUTH_USER_MODEL). La tabla USER será nuestro AbstractBaseUser.
* Relaciones Django: * PERSON a USER: OneToOneField.
* PERFIL a USER: ForeignKey (Un perfil puede ser usado por muchos usuarios).
* Dinero: Todos los campos relacionados con precios utilizarán tipos de datos Decimal, nunca tipos de punto flotante (Float), para evitar errores de precisión.


