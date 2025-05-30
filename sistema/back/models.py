from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Enum, Boolean, DECIMAL, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import JSON
from datetime import datetime
from database import Base

class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    address = Column(Text)
    phone_number = Column(String(30))
    email = Column(String(100))
    website = Column(String(255))
    timezone = Column(String(50), nullable=False, default='UTC')
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    patient_identifier = Column(String(50), unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other', 'PreferNotToSay'))
    address = Column(Text)
    phone_number = Column(String(30))
    email = Column(String(100))
    emergency_contact_name = Column(String(150))
    emergency_contact_phone = Column(String(30))
    primary_care_physician = Column(String(150))
    insurance_provider = Column(String(100))
    insurance_policy_number = Column(String(100))
    medical_history_summary = Column(Text)
    allergies = Column(Text)
    preferred_communication_channel = Column(Enum('Email', 'SMS', 'Phone', 'Portal'))
    gdpr_consent = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])
    user = relationship("User", foreign_keys=[user_id])

class IOPExam(Base):
    __tablename__ = "iopexams"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    exam_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    method = Column(String(50))
    iop_od = Column(Integer)
    iop_os = Column(Integer)
    time_measured = Column(Time)
    notes = Column(Text)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))

    consultation = relationship("Consultation")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class InvoiceItem(Base):
    __tablename__ = "invoiceitems"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"))
    description = Column(String(255), nullable=False)
    quantity = Column(DECIMAL(10, 2), nullable=False, default=1.00)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)

    invoice = relationship("Invoice")
    service = relationship("Service")

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"))
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    invoice_number = Column(String(50), unique=True, nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date)
    total_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    amount_paid = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    status = Column(Enum('Draft','Sent','PartiallyPaid','Paid','Overdue','Void'), nullable=False, default='Draft')
    notes = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    patient = relationship("Patient")
    consultation = relationship("Consultation")
    appointment = relationship("Appointment")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class InventoryItem(Base):
    __tablename__ = "inventoryitems"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    item_name = Column(String(150), nullable=False)
    item_code = Column(String(50), unique=True)
    description = Column(Text)
    category = Column(String(100))
    supplier = Column(String(150))
    quantity_on_hand = Column(Integer, nullable=False, default=0)
    reorder_level = Column(Integer)
    unit_cost = Column(DECIMAL(10, 2))
    storage_location = Column(String(100))
    expiry_date = Column(Date)
    last_counted_at = Column(DateTime)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class EducationalResource(Base):
    __tablename__ = "educational_resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content_type = Column(Enum('Article','Video','PDF','Interactive'), nullable=False)
    content_url = Column(String(512))
    description = Column(Text)
    category = Column(String(100))
    tags = Column(JSON)
    language = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    equipment_name = Column(String(150), nullable=False)
    serial_number = Column(String(100), unique=True)
    model_number = Column(String(100))
    manufacturer = Column(String(100))
    purchase_date = Column(Date)
    warranty_expiry_date = Column(Date)
    location = Column(String(100))
    status = Column(Enum('Operational','UnderMaintenance','Decommissioned','NeedsCalibration'), nullable=False, default='Operational')
    last_maintenance_date = Column(Date)
    next_maintenance_date = Column(Date)
    last_calibration_date = Column(Date)
    next_calibration_date = Column(Date)
    notes = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    resource = relationship("Resource")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class ContactLensPrescription(Base):
    __tablename__ = "contact_lens_prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False)
    lens_type = Column(String(100))
    brand = Column(String(100))
    base_curve_od = Column(DECIMAL(4, 2))
    base_curve_os = Column(DECIMAL(4, 2))
    diameter_od = Column(DECIMAL(4, 2))
    diameter_os = Column(DECIMAL(4, 2))
    replacement_schedule = Column(String(50))
    wear_schedule = Column(String(100))

    prescription = relationship("Prescription")

class DataAccessLog(Base):
    __tablename__ = "data_access_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    accessed_table = Column(String(100), nullable=False)
    record_id = Column(Integer, nullable=False)
    access_type = Column(Enum('View','Create','Update','Delete'), nullable=False)
    access_timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    icd10_code = Column(String(10))
    diagnosis_description = Column(String(255), nullable=False)
    is_primary = Column(Boolean, nullable=False, default=False)
    diagnosis_date = Column(Date, nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    consultation = relationship("Consultation")
    patient = relationship("Patient")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), unique=True, nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    attending_doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    consultation_start_time = Column(DateTime)
    consultation_end_time = Column(DateTime)
    chief_complaint = Column(Text)
    history_of_present_illness = Column(Text)
    past_medical_history = Column(Text)
    family_history = Column(Text)
    social_history = Column(Text)
    review_of_systems = Column(Text)
    assessment_plan = Column(Text)
    status = Column(Enum('Open','Signed','Closed'), nullable=False, default='Open')
    signed_at = Column(DateTime)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    appointment = relationship("Appointment")
    patient = relationship("Patient")
    clinic = relationship("Clinic")
    attending_doctor = relationship("User", foreign_keys=[attending_doctor_id])
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class AppointmentService(Base):
    __tablename__ = "appointmentservices"

    appointment_id = Column(Integer, ForeignKey("appointments.id"), primary_key=True)
    service_id = Column(Integer, ForeignKey("services.id"), primary_key=True)

    appointment = relationship("Appointment")
    service = relationship("Service")

class AuditLog(Base):
    __tablename__ = "auditlogs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    clinic_id = Column(Integer, ForeignKey("clinics.id"))
    action_type = Column(String(50), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(String(100))
    details = Column(Text)
    old_values = Column(JSON)
    new_values = Column(JSON)
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    severity = Column(Enum('Low','Medium','High','Critical'))
    related_records = Column(JSON)
    system_component = Column(String(100))
    is_reviewed = Column(Boolean, default=False)
    reviewed_by_user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", foreign_keys=[user_id])
    clinic = relationship("Clinic")
    reviewed_by_user = relationship("User", foreign_keys=[reviewed_by_user_id])

class ClinicalProtocol(Base):
    __tablename__ = "clinical_protocols"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text)
    protocol_content = Column(JSON, nullable=False)
    version = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ClinicalStudy(Base):
    __tablename__ = "clinical_studies"

    id = Column(Integer, primary_key=True, index=True)
    study_name = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    principal_investigator_id = Column(Integer, ForeignKey("users.id"))
    protocol_number = Column(String(100))
    status = Column(Enum('Active','Completed','Suspended'))

    principal_investigator = relationship("User")

class ConsentForm(Base):
    __tablename__ = "consentforms"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"))
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    form_template_id = Column(Integer)
    form_title = Column(String(255), nullable=False)
    form_content_version = Column(Text, nullable=False)
    status = Column(Enum('Pending','Signed','Revoked'), nullable=False, default='Pending')
    signed_at = Column(DateTime)
    signature_data = Column(Text)
    signature_method = Column(String(50))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    patient = relationship("Patient")
    clinic = relationship("Clinic")
    consultation = relationship("Consultation")
    appointment = relationship("Appointment")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(30))
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    associated_clinic_id = Column(Integer, ForeignKey("clinics.id"))
    is_active = Column(Boolean, nullable=False, default=True)
    last_login_at = Column(DateTime)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    role = relationship("Role")
    associated_clinic = relationship("Clinic")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class RolePermission(Base):
    __tablename__ = "rolepermissions"

    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)

    role = relationship("Role")
    permission = relationship("Permission")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    primary_doctor_id = Column(Integer, ForeignKey("users.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    appointment_type = Column(String(100))
    status = Column(Enum('Scheduled','Confirmed','CheckedIn','InProgress','Completed','Cancelled','NoShow'), nullable=False, default='Scheduled')
    reason_for_visit = Column(Text)
    cancellation_reason = Column(Text)
    confirmation_sent_at = Column(DateTime)
    reminder_sent_at = Column(DateTime)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    patient = relationship("Patient")
    primary_doctor = relationship("User", foreign_keys=[primary_doctor_id])
    resource = relationship("Resource")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class LicensePermit(Base):
    __tablename__ = "licensespermits"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    name = Column(String(255), nullable=False)
    authority = Column(String(150))
    license_number = Column(String(100))
    issue_date = Column(Date)
    expiry_date = Column(Date, nullable=False)
    status = Column(Enum('Active','Expired','PendingRenewal'), nullable=False, default='Active')
    document_path = Column(String(512))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class MaintenanceLog(Base):
    __tablename__ = "maintenancelogs"

    id = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=False)
    log_type = Column(Enum('Maintenance','Calibration','Repair'), nullable=False)
    log_date = Column(Date, nullable=False)
    description = Column(Text, nullable=False)
    performed_by_user_id = Column(Integer, ForeignKey("users.id"))
    external_technician = Column(String(150))
    cost = Column(DECIMAL(10, 2))
    next_due_date = Column(Date)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    equipment = relationship("Equipment")
    performed_by_user = relationship("User", foreign_keys=[performed_by_user_id])

class MarketingCampaign(Base):
    __tablename__ = "marketingcampaigns"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    name = Column(String(150), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    channel = Column(String(50))
    target_audience = Column(Text)
    budget = Column(DECIMAL(10, 2))
    status = Column(Enum('Planned','Active','Completed','Cancelled'), nullable=False, default='Planned')
    goal = Column(Text)
    results_summary = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class OphthalmologicalImage(Base):
    __tablename__ = "ophthalmological_images"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    image_type = Column(Enum('Retinography','OCT','Angiography','Topography','Other'))
    image_path = Column(String(512))
    description = Column(Text)
    capture_date = Column(DateTime)
    analysis_notes = Column(Text)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))

    consultation = relationship("Consultation")
    patient = relationship("Patient")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class OpticalPrescriptionDetail(Base):
    __tablename__ = "opticalprescriptiondetails"

    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), primary_key=True)
    sphere_od = Column(DECIMAL(4, 2))
    cylinder_od = Column(DECIMAL(4, 2))
    axis_od = Column(Integer)
    add_od = Column(DECIMAL(4, 2))
    prism_od = Column(String(50))
    sphere_os = Column(DECIMAL(4, 2))
    cylinder_os = Column(DECIMAL(4, 2))
    axis_os = Column(Integer)
    add_os = Column(DECIMAL(4, 2))
    prism_os = Column(String(50))
    pd = Column(DECIMAL(4, 1))
    lens_recommendations = Column(Text)
    expiry_date = Column(Date)

    prescription = relationship("Prescription")

class PatientEducationTracking(Base):
    __tablename__ = "patient_education_tracking"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("educational_resources.id"), nullable=False)
    viewed_at = Column(DateTime, default=datetime.utcnow)
    completion_status = Column(Enum('Started','Completed','In Progress'), nullable=False)

    patient = relationship("Patient")
    resource = relationship("EducationalResource")

class PatientNotification(Base):
    __tablename__ = "patient_notifications"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    notification_type = Column(Enum('Appointment','Results','Payment','Message'), nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient")

class PatientPortalSession(Base):
    __tablename__ = "patient_portal_sessions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    login_time = Column(DateTime, default=datetime.utcnow)
    logout_time = Column(DateTime)
    ip_address = Column(String(45))
    device_info = Column(String(255))

    patient = relationship("Patient")

class PatientCommunication(Base):
    __tablename__ = "patientcommunications"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    communication_type = Column(Enum('Email','SMS','PhoneCall','PortalMessage','Chatbot'), nullable=False)
    direction = Column(Enum('Outgoing','Incoming'), nullable=False)
    subject = Column(String(255))
    content = Column(Text, nullable=False)
    status = Column(Enum('Sent','Delivered','Failed','Read','Received'), nullable=False)
    sent_received_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    related_appointment_id = Column(Integer, ForeignKey("appointments.id"))
    related_invoice_id = Column(Integer, ForeignKey("invoices.id"))
    created_by_user_id = Column(Integer, ForeignKey("users.id"))

    patient = relationship("Patient")
    clinic = relationship("Clinic")
    related_appointment = relationship("Appointment")
    related_invoice = relationship("Invoice")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class PatientDocument(Base):
    __tablename__ = "patientdocuments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    document_type = Column(String(100), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(512), nullable=False)
    mime_type = Column(String(100))
    description = Column(Text)
    uploaded_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    uploaded_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    patient = relationship("Patient")
    clinic = relationship("Clinic")
    uploaded_by_user = relationship("User", foreign_keys=[uploaded_by_user_id])

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    payment_date = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(String(50))
    transaction_reference = Column(String(100))
    notes = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    invoice = relationship("Invoice")
    patient = relationship("Patient")
    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class PerformanceMetric(Base):
    __tablename__ = "performance_metrics"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    metric_name = Column(String(100), nullable=False)
    metric_value = Column(DECIMAL(10, 2), nullable=False)
    metric_target = Column(DECIMAL(10, 2))
    measurement_date = Column(Date, nullable=False)
    metric_category = Column(Enum('Clinical','Financial','Operational','Patient Satisfaction'), nullable=False)

    clinic = relationship("Clinic")

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    prescription_type = Column(Enum('Optical','Medication','LabOrder','Other'), nullable=False)
    prescription_date = Column(Date, nullable=False)
    notes = Column(Text)
    status = Column(Enum('Active','Expired','Cancelled'), nullable=False, default='Active')
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    consultation = relationship("Consultation")
    patient = relationship("Patient")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class RefractionExam(Base):
    __tablename__ = "refractionexams"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    exam_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    refraction_type = Column(Enum('Manifest','Cycloplegic','Auto'), nullable=False)
    sphere_od = Column(DECIMAL(4, 2))
    cylinder_od = Column(DECIMAL(4, 2))
    axis_od = Column(Integer)
    add_od = Column(DECIMAL(4, 2))
    prism_od = Column(String(50))
    sphere_os = Column(DECIMAL(4, 2))
    cylinder_os = Column(DECIMAL(4, 2))
    axis_os = Column(Integer)
    add_os = Column(DECIMAL(4, 2))
    prism_os = Column(String(50))
    pd = Column(DECIMAL(4, 1))
    notes = Column(Text)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))

    consultation = relationship("Consultation")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    name = Column(String(100), nullable=False)
    resource_type = Column(Enum('Room','Equipment'), nullable=False)
    location = Column(String(100))
    is_schedulable = Column(Boolean, nullable=False, default=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class SecurityPolicy(Base):
    __tablename__ = "security_policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_name = Column(String(100), nullable=False)
    description = Column(Text)
    requirements = Column(Text)
    last_review_date = Column(Date)
    next_review_date = Column(Date)
    status = Column(Enum('Active','Under Review','Archived'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    duration_minutes = Column(Integer)
    base_price = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    updated_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])
    updated_by_user = relationship("User", foreign_keys=[updated_by_user_id])

class SurgicalProcedure(Base):
    __tablename__ = "surgical_procedures"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    surgeon_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    procedure_date = Column(DateTime)
    procedure_type = Column(String(100))
    eye = Column(Enum('OD','OS','OU'))
    pre_op_notes = Column(Text)
    surgical_notes = Column(Text)
    post_op_notes = Column(Text)
    complications = Column(Text)
    status = Column(Enum('Scheduled','Completed','Cancelled'))

    patient = relationship("Patient")
    surgeon = relationship("User", foreign_keys=[surgeon_id])

class SurveyResponse(Base):
    __tablename__ = "surveyresponses"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    response_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    response_data = Column(JSON, nullable=False)
    overall_rating = Column(Integer)
    comments = Column(Text)
    is_anonymous = Column(Boolean, nullable=False, default=False)
    satisfaction_score = Column(Integer)
    nps_score = Column(Integer)
    feedback_category = Column(Enum('Service','Staff','Facilities','Treatment'))
    action_taken = Column(Text)
    follow_up_date = Column(Date)

    survey = relationship("Survey")
    patient = relationship("Patient")
    user = relationship("User", foreign_keys=[user_id])
    appointment = relationship("Appointment")

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    survey_type = Column(Enum('PatientSatisfaction','EmployeeFeedback','PostConsultation'), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime)

    clinic = relationship("Clinic")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class TelemedicineSession(Base):
    __tablename__ = "telemedicine_sessions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_date = Column(DateTime)
    platform_used = Column(String(100))
    session_notes = Column(Text)
    follow_up_required = Column(Boolean)

    patient = relationship("Patient")
    doctor = relationship("User", foreign_keys=[doctor_id])

class TriageAssessment(Base):
    __tablename__ = "triage_assessments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    priority_level = Column(Enum('Emergency','Urgent','Non-Urgent'), nullable=False)
    symptoms = Column(Text, nullable=False)
    vital_signs = Column(JSON)
    assessment_notes = Column(Text)
    assessed_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assessed_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient")
    appointment = relationship("Appointment")
    assessed_by_user = relationship("User", foreign_keys=[assessed_by_user_id])

class VisualAcuityExam(Base):
    __tablename__ = "visualacuityexams"

    id = Column(Integer, primary_key=True, index=True)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    exam_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    va_od_sc = Column(String(20))
    va_os_sc = Column(String(20))
    va_od_cc = Column(String(20))
    va_os_cc = Column(String(20))
    ph_od = Column(String(20))
    ph_os = Column(String(20))
    notes = Column(Text)
    created_by_user_id = Column(Integer, ForeignKey("users.id"))

    consultation = relationship("Consultation")
    created_by_user = relationship("User", foreign_keys=[created_by_user_id])

class WorkflowInstance(Base):
    __tablename__ = "workflow_instances"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("workflow_templates.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    current_step = Column(Integer)
    status = Column(Enum('InProgress','Completed','Cancelled'), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)

    template = relationship("WorkflowTemplate")
    patient = relationship("Patient")

class WorkflowTemplate(Base):
    __tablename__ = "workflow_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    workflow_type = Column(Enum('Clinical','Administrative','Emergency'), nullable=False)
    steps = Column(JSON, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create a models object that contains all model classes and Base
models = type('', (), {
    'Base': Base,
    'Clinic': Clinic,
    'Patient': Patient,
    'IOPExam': IOPExam,
    'InvoiceItem': InvoiceItem,
    'Invoice': Invoice,
    'InventoryItem': InventoryItem,
    'EducationalResource': EducationalResource,
    'Equipment': Equipment,
    'ContactLensPrescription': ContactLensPrescription,
    'DataAccessLog': DataAccessLog,
    'Diagnosis': Diagnosis,
    'Consultation': Consultation,
    'AppointmentService': AppointmentService,
    'AuditLog': AuditLog,
    'ClinicalProtocol': ClinicalProtocol,
    'ClinicalStudy': ClinicalStudy,
    'ConsentForm': ConsentForm,
    'User': User,
    'Role': Role,
    'Permission': Permission,
    'RolePermission': RolePermission,
    'Appointment': Appointment,
    'LicensePermit': LicensePermit,
    'MaintenanceLog': MaintenanceLog,
    'MarketingCampaign': MarketingCampaign,
    'OphthalmologicalImage': OphthalmologicalImage,
    'OpticalPrescriptionDetail': OpticalPrescriptionDetail,
    'PatientEducationTracking': PatientEducationTracking,
    'PatientNotification': PatientNotification,
    'PatientPortalSession': PatientPortalSession,
    'PatientCommunication': PatientCommunication,
    'PatientDocument': PatientDocument,
    'Payment': Payment,
    'PerformanceMetric': PerformanceMetric,
    'Prescription': Prescription,
    'RefractionExam': RefractionExam,
    'Resource': Resource,
    'SecurityPolicy': SecurityPolicy,
    'Service': Service,
    'SurgicalProcedure': SurgicalProcedure,
    'SurveyResponse': SurveyResponse,
    'Survey': Survey,
    'TelemedicineSession': TelemedicineSession,
    'TriageAssessment': TriageAssessment,
    'VisualAcuityExam': VisualAcuityExam,
    'WorkflowInstance': WorkflowInstance,
    'WorkflowTemplate': WorkflowTemplate
})()
