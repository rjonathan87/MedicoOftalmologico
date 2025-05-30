### Resumen del Sistema de la Clínica Oftalmológica

Esta base de datos está diseñada para gestionar las operaciones de una clínica oftalmológica. Abarca desde la información del paciente y sus citas, hasta el historial médico, facturación, inventario, equipamiento y gestión de personal. El sistema busca centralizar y optimizar los procesos clave de una clínica moderna, incluyendo la administración de pacientes, gestión de citas, el manejo de expedientes clínicos, la facturación y los recursos de la clínica. También incluye módulos para la auditoría de actividades, gestión de permisos y roles de usuario, comunicación con pacientes y marketing.

### Módulos y Tablas: Descripción y Relaciones

A continuación, se describen los módulos principales y las tablas que los componen, así como sus relaciones:

#### 1. Gestión de Usuarios y Roles (Seguridad y Acceso)
Este módulo se encarga de la autenticación, autorización y auditoría de los usuarios que interactúan con el sistema.

* **`users`**: Almacena la información de todos los usuarios del sistema (médicos, administradores, recepcionistas, etc.), incluyendo credenciales, datos personales y el rol asignado.
    * Relaciona con `roles` (muchos a uno: un usuario tiene un rol).
    * Relaciona con `clinics` (muchos a uno: un usuario puede estar asociado a una clínica).
    * Relaciona con varias tablas como `appointments`, `consultations`, `patients`, `invoices`, etc., a través de `created_by_user_id` y `updated_by_user_id` para trazabilidad.
* **`roles`**: Define los diferentes tipos de roles de usuario en el sistema (ej. SuperAdministrador, Doctor, Recepcionista).
    * Relaciona con `users` (uno a muchos: un rol puede ser asignado a múltiples usuarios).
    * Relaciona con `rolepermissions` (uno a muchos: un rol tiene múltiples permisos).
* **`permissions`**: Contiene la lista granular de acciones que un usuario puede realizar en el sistema (ej. `paciente.crear`, `cita.agendar`).
    * Relaciona con `rolepermissions` (uno a muchos: un permiso puede ser parte de múltiples roles).
* **`rolepermissions`**: Tabla de unión que establece la relación muchos a muchos entre `roles` y `permissions`, definiendo qué permisos tiene cada rol.
* **`auditlogs`**: Registra todas las acciones importantes realizadas en el sistema (quién hizo qué, cuándo, desde dónde) para fines de auditoría y seguridad.
    * Relaciona con `users` y `clinics`.

#### 2. Gestión de Clínicas (Configuración Global)
Este módulo administra la información de las diferentes clínicas operadas por el sistema.

* **`clinics`**: Almacena los datos de cada clínica (nombre, dirección, contacto, zona horaria).
    * Es una tabla central, relacionada con casi todas las demás tablas, ya que muchas operaciones están ligadas a una clínica específica (ej. `patients`, `appointments`, `resources`, `invoices`, `users`).

#### 3. Gestión de Pacientes
Maneja toda la información demográfica y administrativa de los pacientes.

* **`patients`**: Contiene la información personal y de contacto del paciente, historial médico resumido, alergias, datos de seguro y preferencias de comunicación.
    * Relaciona con `clinics` (muchos a uno: un paciente está registrado en una clínica).
    * Relaciona con `appointments`, `consultations`, `invoices`, `payments`, `prescriptions`, `patientcommunications`, `patientdocuments`, `consentforms`, `surveyresponses`.

#### 4. Gestión de Citas
Este módulo facilita la programación, modificación y seguimiento de las citas de los pacientes.

* **`appointments`**: Registra los detalles de cada cita, incluyendo la clínica, paciente, doctor principal, recursos utilizados, horario, tipo y estado de la cita.
    * Relaciona con `clinics`, `patients`, `users` (para el doctor principal y usuarios que crearon/actualizaron), `resources`.
    * Relaciona con `consultations` (uno a uno: una cita puede tener una consulta asociada), `patientcommunications`, `invoices`.
* **`appointmentservices`**: Tabla de unión que relaciona citas con los servicios específicos que se realizarán durante la cita.
    * Relaciona con `appointments` y `services` (muchos a muchos).

#### 5. Expediente Clínico y Consultas
Permite el registro detallado del historial médico del paciente, las consultas y los exámenes.

* **`consultations`**: Almacena la información de cada consulta médica (motivo de consulta, historial, examen, plan de evaluación, etc.).
    * Tiene una relación uno a uno con `appointments` y se relaciona con `patients`, `clinics`, `users` (doctor tratante y usuarios que crearon/actualizaron).
    * Relaciona con `diagnoses`, `prescriptions`, `visualacuityexams`, `refractionexams`, `iopexams`, `consentforms`, `invoices`.
* **`diagnoses`**: Registra los diagnósticos de los pacientes para cada consulta, incluyendo códigos ICD-10.
    * Relaciona con `consultations` y `patients`.
* **`prescriptions`**: Almacena las recetas médicas (ópticas, medicamentos, órdenes de laboratorio).
    * Relaciona con `consultations` y `patients`.
    * Relaciona con `opticalprescriptiondetails` (uno a uno).
* **`opticalprescriptiondetails`**: Contiene los detalles específicos de las prescripciones ópticas (esfera, cilindro, eje, etc.).
    * Relaciona con `prescriptions` (uno a uno).
* **`visualacuityexams`**: Registra los resultados de los exámenes de agudeza visual.
    * Relaciona con `consultations`.
* **`refractionexams`**: Almacena los resultados de los exámenes de refracción.
    * Relaciona con `consultations`.
* **`iopexams`**: Guarda los resultados de los exámenes de presión intraocular (IOP).
    * Relaciona con `consultations`.

#### 6. Facturación y Pagos
Maneja la generación de facturas y el registro de pagos.

* **`services`**: Define los servicios que ofrece la clínica, con su descripción, duración y precio base.
    * Relaciona con `clinics`.
    * Relaciona con `appointmentservices` e `invoiceitems`.
* **`invoices`**: Almacena las facturas generadas para los pacientes, con detalles como número de factura, fechas, montos y estado de pago.
    * Relaciona con `clinics`, `patients`, `consultations`, `appointments`.
    * Relaciona con `invoiceitems` y `payments`.
* **`invoiceitems`**: Detalla los ítems incluidos en cada factura (servicios, cantidades, precios unitarios y totales).
    * Relaciona con `invoices` y `services`.
* **`payments`**: Registra los pagos realizados por los pacientes contra sus facturas.
    * Relaciona con `invoices`, `patients`, `clinics`.

#### 7. Gestión de Recursos y Equipamiento
Administra los recursos físicos de la clínica.

* **`resources`**: Define los recursos físicos de la clínica que pueden ser programables (ej. salas de examen, equipos grandes).
    * Relaciona con `clinics`.
    * Relaciona con `appointments` y `equipment`.
* **`equipment`**: Almacena información detallada del equipamiento médico (nombre, número de serie, fabricante, estado, fechas de mantenimiento y calibración).
    * Relaciona con `clinics` y `resources`.
    * Relaciona con `maintenancelogs`.
* **`maintenancelogs`**: Registra el historial de mantenimiento, calibración y reparaciones del equipamiento.
    * Relaciona con `equipment` y `users` (quién realizó la acción).

#### 8. Gestión de Inventario
Maneja los productos y consumibles utilizados en la clínica.

* **`inventoryitems`**: Contiene la información de los artículos en inventario (nombre, código, descripción, categoría, proveedor, cantidad, nivel de reorden, costo unitario, ubicación y fecha de caducidad).
    * Relaciona con `clinics`.

#### 9. Documentación y Consentimientos
Gestiona documentos y formularios de consentimiento de los pacientes.

* **`patientdocuments`**: Almacena referencias a documentos cargados relacionados con un paciente (ej. referidos, resultados de pruebas externas).
    * Relaciona con `patients` y `clinics`.
* **`consentforms`**: Administra los formularios de consentimiento informados que los pacientes deben firmar.
    * Relaciona con `patients`, `clinics`, `consultations`, `appointments`.

#### 10. Comunicación y Marketing
Permite la gestión de la comunicación con los pacientes y las campañas de marketing.

* **`patientcommunications`**: Registra todas las interacciones de comunicación con los pacientes (correos, SMS, llamadas).
    * Relaciona con `patients`, `clinics`, `appointments`, `invoices`.
* **`marketingcampaigns`**: Almacena los detalles de las campañas de marketing de la clínica.
    * Relaciona con `clinics`.
* **`surveys`**: Define las encuestas que la clínica puede realizar (satisfacción del paciente, retroalimentación de empleados).
    * Relaciona con `clinics`.
* **`surveyresponses`**: Almacena las respuestas a las encuestas.
    * Relaciona con `surveys`, `patients`, `users`, `appointments`.

#### 11. Cumplimiento y Licencias
Registra y da seguimiento a las licencias y permisos de la clínica.

* **`licensespermits`**: Mantiene un registro de las licencias y permisos necesarios para la operación de la clínica, con fechas de emisión y vencimiento.
    * Relaciona con `clinics`.

En resumen, la base de datos `ophthalmological_clinic` está bien estructurada para manejar la complejidad de una clínica moderna, con una clara separación de responsabilidades en diferentes módulos y una robusta interconexión entre ellos a través de claves foráneas, permitiendo una gestión integral de pacientes, citas, expedientes, recursos y finanzas.