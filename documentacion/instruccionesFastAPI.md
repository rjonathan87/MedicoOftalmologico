**Prompt para IA: Construcción de Backend RESTful con FastAPI para Clínica Oftalmológica**

**Objetivo General:**
Desarrollar un backend RESTful robusto, escalable y siguiendo las mejores prácticas de arquitectura y código, utilizando FastAPI en Python. Este backend interactuará con una base de datos MySQL existente para una clínica oftalmológica y será el punto central para la automatización de procesos a través de n8n y otros scripts Python.

**Contexto de la Aplicación:**
La aplicación gestionará todas las operaciones de una clínica oftalmológica (pacientes, citas, expedientes, facturación, inventario, personal, etc.). La base de datos MySQL (`dump-ophthalmological_clinic-202505261551.sql`) y su esquema (`explicacionBaseDatos.md`) ya están definidos y son el modelo de verdad para los datos.

**Requisitos Clave:**

1.  **Framework Principal:** FastAPI (Python).
2.  **Base de Datos:** MySQL (interacción con el esquema existente).
3.  **ORM/Herramienta de BBDD:** SQLAlchemy 2.0 (con el paradigma Core y ORM) para la interacción con MySQL, asegurando una gestión eficiente y segura de las conexiones y transacciones.
4.  **Validación de Datos y Serialización:** Pydantic para la definición de esquemas de datos (modelos request/response) y validación.
5.  **Autenticación y Autorización:**
    * Implementar un sistema de autenticación basado en JWT (JSON Web Tokens).
    * Gestionar roles de usuario (`roles` tabla) y permisos (`user_permissions`, `role_permissions` tablas) para control de acceso basado en roles (RBAC - Role-Based Access Control) en los endpoints.
    * Ejemplo: un médico solo puede ver los expedientes de sus propios pacientes, un administrador puede ver todos.
6.  **Estructura del Proyecto (Arquitectura):**
    * Adoptar una arquitectura modular y limpia (Clean Architecture o similar) para separar responsabilidades.
    * **Capas propuestas:**
        * `main.py` (o `app.py`): Configuración de FastAPI, rutas principales, manejo de eventos de startup/shutdown.
        * `routers/`: Contiene los archivos de router de FastAPI para cada módulo principal (ej. `users.py`, `patients.py`, `appointments.py`, `invoices.py`, `medical_records.py`).
        * `schemas/`: Modelos Pydantic para solicitudes (Request Body), respuestas (Response Model) y validación de datos.
        * `models/` (o `database/models/`): Definiciones de modelos SQLAlchemy (SQLAlchemy ORM Declarative Base).
        * `crud/` (o `repositories/`): Lógica de interacción con la base de datos (CRUD operations), desacoplada de los routers. Idealmente, funciones genéricas y específicas para cada entidad.
        * `services/`: Lógica de negocio compleja, orquestación de múltiples operaciones CRUD, validaciones adicionales. Aquí se implementarán las reglas de negocio principales.
        * `dependencies/`: Funciones para inyección de dependencias de FastAPI (ej. `get_db`, `get_current_user`, `verify_role`).
        * `core/config.py`: Gestión de configuración y variables de entorno.
        * `core/security.py`: Lógica de seguridad (hashing de contraseñas, JWT encoding/decoding).
        * `exceptions/`: Definición de excepciones personalizadas para errores de aplicación.
        * `tests/`: Pruebas unitarias y de integración.
7.  **Manejo de Errores:**
    * Implementar un manejo de excepciones global y específico, retornando respuestas HTTP apropiadas (400, 401, 403, 404, 500) con mensajes claros y consistentes.
    * Usar `HTTPException` de FastAPI para errores estándar.
8.  **Documentación Automática:**
    * Aprovechar la generación automática de documentación OpenAPI (Swagger UI y ReDoc) por parte de FastAPI.
    * Asegurar que los *path operations*, *request bodies* y *response models* estén bien documentados con docstrings y descripciones Pydantic.
9.  **Contenedorización:**
    * Proveer un `Dockerfile` para la aplicación FastAPI.
    * Proveer un `docker-compose.yml` para levantar la aplicación FastAPI junto con una instancia de MySQL (si se prefiere para desarrollo/testing).
10. **Conectividad con n8n/Python:**
    * Asegurar que los endpoints estén diseñados para ser fácilmente consumibles por n8n (ej. APIs RESTful claras, uso consistente de JSON).
    * Considerar la implementación de Webhooks específicos donde sea necesario para n8n (ej. notificaciones de nuevos registros, actualizaciones de estado).
    * Los endpoints deben ser idempotentes cuando sea apropiado para reintentos de automatización.
11. **Ejemplo de Implementación (Módulo `users` y `patients`):**
    * Proveer un ejemplo completo para el módulo `users` (CRUD de usuarios, registro, login, obtención de perfil de usuario) y el módulo `patients` (CRUD de pacientes, incluyendo la relación con `users` si un paciente está asociado a un usuario).
    * Implementar la lógica para `created_at`, `updated_at`, `deleted_at` (soft delete) en los modelos SQLAlchemy y en las operaciones CRUD, utilizando *mixins* o *listeners* de SQLAlchemy si es posible.
    * Considerar la implementación de la restricción `WHERE user_id = current_user()` de la vista `patient_invoices_view` en el backend para la autorización de acceso a datos del paciente.

**Instrucciones Adicionales para la IA:**

* **Comentarios:** Incluir comentarios claros y concisos en el código para explicar la lógica compleja, decisiones de diseño y dónde se aplican las mejores prácticas.
* **Gestión de Dependencias:** Usar `requirements.txt` (o `pyproject.toml` con Poetry/Rye) para listar las dependencias.
* **Configuración de Entorno:** Utilizar variables de entorno para datos sensibles (ej. credenciales de DB, secreto JWT).
* **Ejecución:** Proporcionar instrucciones claras sobre cómo ejecutar el proyecto (instalar dependencias, correr migraciones de DB si las hubiera, iniciar el servidor).
* **Consideraciones de Rendimiento:** Mencionar buenas prácticas para optimizar el rendimiento (ej. uso de `await` para operaciones I/O, índices de DB).
* **Testing:** Mencionar la importancia de las pruebas unitarias y de integración para asegurar la robustez y facilitar el crecimiento.

---

Este prompt es muy detallado y debería guiar a la IA para generar una base sólida para tu backend de FastAPI. Asegúrate de proporcionar los archivos `dump-ophthalmological_clinic-202505261551.sql` y `explicacionBaseDatos.md` cuando uses este prompt con la IA para que tenga todo el contexto del esquema de la base de datos.