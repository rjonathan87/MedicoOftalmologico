from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime, date, time

class ClinicBase(BaseModel):
    name: str
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    timezone: str = 'UTC'
    is_active: bool = True

class ClinicCreate(ClinicBase):
    pass

class Clinic(ClinicBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    clinic_id: int
    patient_id: int
    consultation_id: Optional[int] = None
    appointment_id: Optional[int] = None
    invoice_number: str
    invoice_date: date
    due_date: Optional[date] = None
    total_amount: float = 0.00
    amount_paid: float = 0.00
    status: str = 'Draft'
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class InvoiceItemBase(BaseModel):
    invoice_id: int
    service_id: Optional[int] = None
    description: str
    quantity: float = 1.00
    unit_price: float
    total_price: float

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItem(InvoiceItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class IOPExamBase(BaseModel):
    consultation_id: int
    exam_date: datetime
    method: Optional[str] = None
    iop_od: Optional[int] = None
    iop_os: Optional[int] = None
    time_measured: Optional[time] = None
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None

class IOPExamCreate(IOPExamBase):
    pass

class IOPExam(IOPExamBase):
    id: int
    class Config:
        from_attributes = True

class InventoryItemBase(BaseModel):
    clinic_id: int
    item_name: str
    item_code: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    supplier: Optional[str] = None
    quantity_on_hand: int = 0
    reorder_level: Optional[int] = None
    unit_cost: Optional[float] = None
    storage_location: Optional[str] = None
    expiry_date: Optional[date] = None
    last_counted_at: Optional[datetime] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItem(InventoryItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class EquipmentBase(BaseModel):
    clinic_id: int
    resource_id: Optional[int] = None
    equipment_name: str
    serial_number: Optional[str] = None
    model_number: Optional[str] = None
    manufacturer: Optional[str] = None
    purchase_date: Optional[date] = None
    warranty_expiry_date: Optional[date] = None
    location: Optional[str] = None
    status: str = 'Operational'
    last_maintenance_date: Optional[date] = None
    next_maintenance_date: Optional[date] = None
    last_calibration_date: Optional[date] = None
    next_calibration_date: Optional[date] = None
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class EducationalResourceBase(BaseModel):
    title: str
    content_type: str
    content_url: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[Any] = None
    language: Optional[str] = None

class EducationalResourceCreate(EducationalResourceBase):
    pass

class EducationalResource(EducationalResourceBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class DiagnosisBase(BaseModel):
    consultation_id: int
    patient_id: int
    icd10_code: Optional[str] = None
    diagnosis_description: str
    is_primary: bool = False
    diagnosis_date: date
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class DiagnosisCreate(DiagnosisBase):
    pass

class Diagnosis(DiagnosisBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class DataAccessLogBase(BaseModel):
    user_id: int
    accessed_table: str
    record_id: int
    access_type: str

class DataAccessLogCreate(DataAccessLogBase):
    pass

class DataAccessLog(DataAccessLogBase):
    id: int
    access_timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True

class ContactLensPrescriptionBase(BaseModel):
    prescription_id: int
    lens_type: Optional[str] = None
    brand: Optional[str] = None
    base_curve_od: Optional[float] = None
    base_curve_os: Optional[float] = None
    diameter_od: Optional[float] = None
    diameter_os: Optional[float] = None
    replacement_schedule: Optional[str] = None
    wear_schedule: Optional[str] = None

class ContactLensPrescriptionCreate(ContactLensPrescriptionBase):
    pass

class ContactLensPrescription(ContactLensPrescriptionBase):
    id: int

    class Config:
        from_attributes = True

class ConsultationBase(BaseModel):
    appointment_id: int
    patient_id: int
    clinic_id: int
    attending_doctor_id: int
    consultation_start_time: Optional[datetime] = None
    consultation_end_time: Optional[datetime] = None
    chief_complaint: Optional[str] = None
    history_of_present_illness: Optional[str] = None
    past_medical_history: Optional[str] = None
    family_history: Optional[str] = None
    social_history: Optional[str] = None
    review_of_systems: Optional[str] = None
    assessment_plan: Optional[str] = None
    status: str = 'Open'
    signed_at: Optional[datetime] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class ConsultationCreate(ConsultationBase):
    pass

class Consultation(ConsultationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ConsentFormBase(BaseModel):
    patient_id: int
    clinic_id: int
    consultation_id: Optional[int] = None
    appointment_id: Optional[int] = None
    form_template_id: Optional[int] = None
    form_title: str
    form_content_version: str
    status: str = 'Pending'
    signed_at: Optional[datetime] = None
    signature_data: Optional[str] = None
    signature_method: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class ConsentFormCreate(ConsentFormBase):
    pass

class ConsentForm(ConsentFormBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ClinicalStudyBase(BaseModel):
    study_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    principal_investigator_id: Optional[int] = None
    protocol_number: Optional[str] = None
    status: Optional[str] = None

class ClinicalStudyCreate(ClinicalStudyBase):
    pass

class ClinicalStudy(ClinicalStudyBase):
    id: int

    class Config:
        from_attributes = True

class ClinicalProtocolBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    protocol_content: Optional[Any] = None
    version: str
    is_active: bool = True

class ClinicalProtocolCreate(ClinicalProtocolBase):
    pass

class ClinicalProtocol(ClinicalProtocolBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class AuditLogBase(BaseModel):
    user_id: Optional[int] = None
    clinic_id: Optional[int] = None
    action_type: str
    entity_type: str
    entity_id: Optional[str] = None
    details: Optional[str] = None
    old_values: Optional[Any] = None
    new_values: Optional[Any] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    severity: Optional[str] = None
    related_records: Optional[Any] = None
    system_component: Optional[str] = None
    is_reviewed: bool = False
    reviewed_by_user_id: Optional[int] = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLog(AuditLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class AppointmentServiceBase(BaseModel):
    appointment_id: int
    service_id: int

class AppointmentServiceCreate(AppointmentServiceBase):
    pass

class AppointmentService(AppointmentServiceBase):
    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    clinic_id: int
    patient_identifier: Optional[str] = None
    first_name: str
    last_name: str
    date_of_birth: date
    gender: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    primary_care_physician: Optional[str] = None
    insurance_provider: Optional[str] = None
    insurance_policy_number: Optional[str] = None
    medical_history_summary: Optional[str] = None
    allergies: Optional[str] = None
    preferred_communication_channel: Optional[str] = None
    gdpr_consent: bool = False
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None
    user_id: Optional[int] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    role_id: int
    associated_clinic_id: Optional[int] = None
    is_active: bool = True
    last_login_at: Optional[datetime] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RolePermissionBase(BaseModel):
    role_id: int
    permission_id: int

class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermission(RolePermissionBase):
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    clinic_id: int
    patient_id: int
    primary_doctor_id: Optional[int] = None
    resource_id: Optional[int] = None
    start_time: datetime
    end_time: datetime
    appointment_type: Optional[str] = None
    status: str = 'Scheduled'
    reason_for_visit: Optional[str] = None
    cancellation_reason: Optional[str] = None
    confirmation_sent_at: Optional[datetime] = None
    reminder_sent_at: Optional[datetime] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class LicensePermitBase(BaseModel):
    clinic_id: int
    name: str
    authority: Optional[str] = None
    license_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: date
    status: str = 'Active'
    document_path: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class LicensePermitCreate(LicensePermitBase):
    pass

class LicensePermit(LicensePermitBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class MaintenanceLogBase(BaseModel):
    equipment_id: int
    log_type: str
    log_date: date
    description: str
    performed_by_user_id: Optional[int] = None
    external_technician: Optional[str] = None
    cost: Optional[float] = None
    next_due_date: Optional[date] = None

class MaintenanceLogCreate(MaintenanceLogBase):
    pass

class MaintenanceLog(MaintenanceLogBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class MarketingCampaignBase(BaseModel):
    clinic_id: int
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    channel: Optional[str] = None
    target_audience: Optional[str] = None
    budget: Optional[float] = None
    status: str = 'Planned'
    goal: Optional[str] = None
    results_summary: Optional[str] = None
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class MarketingCampaignCreate(MarketingCampaignBase):
    pass

class MarketingCampaign(MarketingCampaignBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class OphthalmologicalImageBase(BaseModel):
    consultation_id: int
    patient_id: int
    image_type: Optional[str] = None
    image_path: Optional[str] = None
    description: Optional[str] = None
    capture_date: Optional[datetime] = None
    analysis_notes: Optional[str] = None
    created_by_user_id: Optional[int] = None

class OphthalmologicalImageCreate(OphthalmologicalImageBase):
    pass

class OphthalmologicalImage(OphthalmologicalImageBase):
    id: int

    class Config:
        from_attributes = True

class OpticalPrescriptionDetailBase(BaseModel):
    prescription_id: int
    sphere_od: Optional[float] = None
    cylinder_od: Optional[float] = None
    axis_od: Optional[int] = None
    add_od: Optional[float] = None
    prism_od: Optional[str] = None
    sphere_os: Optional[float] = None
    cylinder_os: Optional[float] = None
    axis_os: Optional[int] = None
    add_os: Optional[float] = None
    prism_os: Optional[str] = None
    pd: Optional[float] = None
    lens_recommendations: Optional[str] = None
    expiry_date: Optional[date] = None

class OpticalPrescriptionDetailCreate(OpticalPrescriptionDetailBase):
    pass

class OpticalPrescriptionDetail(OpticalPrescriptionDetailBase):
    class Config:
        from_attributes = True

class PatientEducationTrackingBase(BaseModel):
    patient_id: int
    resource_id: int
    viewed_at: Optional[datetime] = None
    completion_status: str

class PatientEducationTrackingCreate(PatientEducationTrackingBase):
    pass

class PatientEducationTracking(PatientEducationTrackingBase):
    id: int

    class Config:
        from_attributes = True

class PatientNotificationBase(BaseModel):
    patient_id: int
    notification_type: str
    content: str
    is_read: bool = False

class PatientNotificationCreate(PatientNotificationBase):
    pass

class PatientNotification(PatientNotificationBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PatientPortalSessionBase(BaseModel):
    patient_id: int
    login_time: Optional[datetime] = None
    logout_time: Optional[datetime] = None
    ip_address: Optional[str] = None
    device_info: Optional[str] = None

class PatientPortalSessionCreate(PatientPortalSessionBase):
    pass

class PatientPortalSession(PatientPortalSessionBase):
    id: int

    class Config:
        from_attributes = True

class PatientCommunicationBase(BaseModel):
    patient_id: int
    clinic_id: int
    communication_type: str
    direction: str
    subject: Optional[str] = None
    content: str
    status: str
    sent_received_at: Optional[datetime] = None
    related_appointment_id: Optional[int] = None
    related_invoice_id: Optional[int] = None
    created_by_user_id: Optional[int] = None

class PatientCommunicationCreate(PatientCommunicationBase):
    pass

class PatientCommunication(PatientCommunicationBase):
    id: int

    class Config:
        from_attributes = True

class PatientDocumentBase(BaseModel):
    patient_id: int
    clinic_id: int
    document_type: str
    file_name: str
    file_path: str
    mime_type: Optional[str] = None
    description: Optional[str] = None
    uploaded_by_user_id: Optional[int] = None

class PatientDocumentCreate(PatientDocumentBase):
    pass

class PatientDocument(PatientDocumentBase):
    id: int
    uploaded_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PaymentBase(BaseModel):
    invoice_id: int
    patient_id: int
    clinic_id: int
    payment_date: date
    amount: float
    payment_method: Optional[str] = None
    transaction_reference: Optional[str] = None
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PerformanceMetricBase(BaseModel):
    clinic_id: int
    metric_name: str
    metric_value: float
    metric_target: Optional[float] = None
    measurement_date: date
    metric_category: str

class PerformanceMetricCreate(PerformanceMetricBase):
    pass

class PerformanceMetric(PerformanceMetricBase):
    id: int

    class Config:
        from_attributes = True

class PrescriptionBase(BaseModel):
    consultation_id: int
    patient_id: int
    prescription_type: str
    prescription_date: date
    notes: Optional[str] = None
    status: str = 'Active'
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class RefractionExamBase(BaseModel):
    consultation_id: int
    exam_date: datetime
    refraction_type: str
    sphere_od: Optional[float] = None
    cylinder_od: Optional[float] = None
    axis_od: Optional[int] = None
    add_od: Optional[float] = None
    prism_od: Optional[str] = None
    sphere_os: Optional[float] = None
    cylinder_os: Optional[float] = None
    axis_os: Optional[int] = None
    add_os: Optional[float] = None
    prism_os: Optional[str] = None
    pd: Optional[float] = None
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None

class RefractionExamCreate(RefractionExamBase):
    pass

class RefractionExam(RefractionExamBase):
    id: int

    class Config:
        from_attributes = True

class ResourceBase(BaseModel):
    clinic_id: int
    name: str
    resource_type: str
    location: Optional[str] = None
    is_schedulable: bool = True
    is_active: bool = True
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class SecurityPolicyBase(BaseModel):
    policy_name: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    last_review_date: Optional[date] = None
    next_review_date: Optional[date] = None
    status: str

class SecurityPolicyCreate(SecurityPolicyBase):
    pass

class SecurityPolicy(SecurityPolicyBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ServiceBase(BaseModel):
    clinic_id: int
    name: str
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    base_price: float = 0.00
    is_active: bool = True
    created_by_user_id: Optional[int] = None
    updated_by_user_id: Optional[int] = None

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class SurgicalProcedureBase(BaseModel):
    patient_id: int
    surgeon_id: int
    procedure_date: Optional[datetime] = None
    procedure_type: Optional[str] = None
    eye: Optional[str] = None
    pre_op_notes: Optional[str] = None
    surgical_notes: Optional[str] = None
    post_op_notes: Optional[str] = None
    complications: Optional[str] = None
    status: Optional[str] = None

class SurgicalProcedureCreate(SurgicalProcedureBase):
    pass

class SurgicalProcedure(SurgicalProcedureBase):
    id: int

    class Config:
        from_attributes = True

class SurveyResponseBase(BaseModel):
    survey_id: int
    patient_id: Optional[int] = None
    user_id: Optional[int] = None
    appointment_id: Optional[int] = None
    response_date: Optional[datetime] = None
    response_data: Any
    overall_rating: Optional[int] = None
    comments: Optional[str] = None
    is_anonymous: bool = False
    satisfaction_score: Optional[int] = None
    nps_score: Optional[int] = None
    feedback_category: Optional[str] = None
    action_taken: Optional[str] = None
    follow_up_date: Optional[date] = None

class SurveyResponseCreate(SurveyResponseBase):
    pass

class SurveyResponse(SurveyResponseBase):
    id: int

    class Config:
        from_attributes = True

class SurveyBase(BaseModel):
    clinic_id: int
    title: str
    description: Optional[str] = None
    survey_type: str
    is_active: bool = True
    created_by_user_id: Optional[int] = None

class SurveyCreate(SurveyBase):
    pass

class Survey(SurveyBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TelemedicineSessionBase(BaseModel):
    patient_id: int
    doctor_id: int
    session_date: Optional[datetime] = None
    platform_used: Optional[str] = None
    session_notes: Optional[str] = None
    follow_up_required: Optional[bool] = None

class TelemedicineSessionCreate(TelemedicineSessionBase):
    pass

class TelemedicineSession(TelemedicineSessionBase):
    id: int

    class Config:
        from_attributes = True

class TriageAssessmentBase(BaseModel):
    patient_id: int
    appointment_id: Optional[int] = None
    priority_level: str
    symptoms: str
    vital_signs: Optional[Any] = None
    assessment_notes: Optional[str] = None
    assessed_by_user_id: int
    assessed_at: Optional[datetime] = None

class TriageAssessmentCreate(TriageAssessmentBase):
    pass

class TriageAssessment(TriageAssessmentBase):
    id: int

    class Config:
        from_attributes = True

class VisualAcuityExamBase(BaseModel):
    consultation_id: int
    exam_date: datetime
    va_od_sc: Optional[str] = None
    va_os_sc: Optional[str] = None
    va_od_cc: Optional[str] = None
    va_os_cc: Optional[str] = None
    ph_od: Optional[str] = None
    ph_os: Optional[str] = None
    notes: Optional[str] = None
    created_by_user_id: Optional[int] = None

class VisualAcuityExamCreate(VisualAcuityExamBase):
    pass

class VisualAcuityExam(VisualAcuityExamBase):
    id: int

    class Config:
        from_attributes = True

class WorkflowInstanceBase(BaseModel):
    template_id: Optional[int] = None
    patient_id: Optional[int] = None
    current_step: Optional[int] = None
    status: str
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class WorkflowInstanceCreate(WorkflowInstanceBase):
    pass

class WorkflowInstance(WorkflowInstanceBase):
    id: int

    class Config:
        from_attributes = True

class WorkflowTemplateBase(BaseModel):
    name: str
    description: Optional[str] = None
    workflow_type: str
    steps: Any
    is_active: bool = True

class WorkflowTemplateCreate(WorkflowTemplateBase):
    pass

class WorkflowTemplate(WorkflowTemplateBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Create a schemas object that contains all schema classes
schemas = type('', (), {
    'ClinicBase': ClinicBase,
    'ClinicCreate': ClinicCreate,
    'Clinic': Clinic,
    'InvoiceBase': InvoiceBase,
    'InvoiceCreate': InvoiceCreate,
    'Invoice': Invoice,
    'InvoiceItemBase': InvoiceItemBase,
    'InvoiceItemCreate': InvoiceItemCreate,
    'InvoiceItem': InvoiceItem,
    'IOPExamBase': IOPExamBase,
    'IOPExamCreate': IOPExamCreate,
    'IOPExam': IOPExam,
    'InventoryItemBase': InventoryItemBase,
    'InventoryItemCreate': InventoryItemCreate,
    'InventoryItem': InventoryItem,
    'EquipmentBase': EquipmentBase,
    'EquipmentCreate': EquipmentCreate,
    'Equipment': Equipment,
    'EducationalResourceBase': EducationalResourceBase,
    'EducationalResourceCreate': EducationalResourceCreate,
    'EducationalResource': EducationalResource,
    'DiagnosisBase': DiagnosisBase,
    'DiagnosisCreate': DiagnosisCreate,
    'Diagnosis': Diagnosis,
    'DataAccessLogBase': DataAccessLogBase,
    'DataAccessLogCreate': DataAccessLogCreate,
    'DataAccessLog': DataAccessLog,
    'ContactLensPrescriptionBase': ContactLensPrescriptionBase,
    'ContactLensPrescriptionCreate': ContactLensPrescriptionCreate,
    'ContactLensPrescription': ContactLensPrescription,
    'ConsultationBase': ConsultationBase,
    'ConsultationCreate': ConsultationCreate,
    'Consultation': Consultation,
    'ConsentFormBase': ConsentFormBase,
    'ConsentFormCreate': ConsentFormCreate,
    'ConsentForm': ConsentForm,
    'ClinicalStudyBase': ClinicalStudyBase,
    'ClinicalStudyCreate': ClinicalStudyCreate,
    'ClinicalStudy': ClinicalStudy,
    'ClinicalProtocolBase': ClinicalProtocolBase,
    'ClinicalProtocolCreate': ClinicalProtocolCreate,
    'ClinicalProtocol': ClinicalProtocol,
    'AuditLogBase': AuditLogBase,
    'AuditLogCreate': AuditLogCreate,
    'AuditLog': AuditLog,
    'AppointmentServiceBase': AppointmentServiceBase,
    'AppointmentServiceCreate': AppointmentServiceCreate,
    'AppointmentService': AppointmentService,
    'PatientBase': PatientBase,
    'PatientCreate': PatientCreate,
    'Patient': Patient,
    'UserBase': UserBase,
    'UserCreate': UserCreate,
    'User': User,
    'RoleBase': RoleBase,
    'RoleCreate': RoleCreate,
    'Role': Role,
    'PermissionBase': PermissionBase,
    'PermissionCreate': PermissionCreate,
    'Permission': Permission,
    'RolePermissionBase': RolePermissionBase,
    'RolePermissionCreate': RolePermissionCreate,
    'RolePermission': RolePermission,
    'AppointmentBase': AppointmentBase,
    'AppointmentCreate': AppointmentCreate,
    'Appointment': Appointment,
    'LicensePermitBase': LicensePermitBase,
    'LicensePermitCreate': LicensePermitCreate,
    'LicensePermit': LicensePermit,
    'MaintenanceLogBase': MaintenanceLogBase,
    'MaintenanceLogCreate': MaintenanceLogCreate,
    'MaintenanceLog': MaintenanceLog,
    'MarketingCampaignBase': MarketingCampaignBase,
    'MarketingCampaignCreate': MarketingCampaignCreate,
    'MarketingCampaign': MarketingCampaign,
    'OphthalmologicalImageBase': OphthalmologicalImageBase,
    'OphthalmologicalImageCreate': OphthalmologicalImageCreate,
    'OphthalmologicalImage': OphthalmologicalImage,
    'OpticalPrescriptionDetailBase': OpticalPrescriptionDetailBase,
    'OpticalPrescriptionDetailCreate': OpticalPrescriptionDetailCreate,
    'OpticalPrescriptionDetail': OpticalPrescriptionDetail,
    'PatientEducationTrackingBase': PatientEducationTrackingBase,
    'PatientEducationTrackingCreate': PatientEducationTrackingCreate,
    'PatientEducationTracking': PatientEducationTracking,
    'PatientNotificationBase': PatientNotificationBase,
    'PatientNotificationCreate': PatientNotificationCreate,
    'PatientNotification': PatientNotification,
    'PatientPortalSessionBase': PatientPortalSessionBase,
    'PatientPortalSessionCreate': PatientPortalSessionCreate,
    'PatientPortalSession': PatientPortalSession,
    'PatientCommunicationBase': PatientCommunicationBase,
    'PatientCommunicationCreate': PatientCommunicationCreate,
    'PatientCommunication': PatientCommunication,
    'PatientDocumentBase': PatientDocumentBase,
    'PatientDocumentCreate': PatientDocumentCreate,
    'PatientDocument': PatientDocument,
    'PaymentBase': PaymentBase,
    'PaymentCreate': PaymentCreate,
    'Payment': Payment,
    'PerformanceMetricBase': PerformanceMetricBase,
    'PerformanceMetricCreate': PerformanceMetricCreate,
    'PerformanceMetric': PerformanceMetric,
    'PrescriptionBase': PrescriptionBase,
    'PrescriptionCreate': PrescriptionCreate,
    'Prescription': Prescription,
    'RefractionExamBase': RefractionExamBase,
    'RefractionExamCreate': RefractionExamCreate,
    'RefractionExam': RefractionExam,
    'ResourceBase': ResourceBase,
    'ResourceCreate': ResourceCreate,
    'Resource': Resource,
    'SecurityPolicyBase': SecurityPolicyBase,
    'SecurityPolicyCreate': SecurityPolicyCreate,
    'SecurityPolicy': SecurityPolicy,
    'ServiceBase': ServiceBase,
    'ServiceCreate': ServiceCreate,
    'Service': Service,
    'SurgicalProcedureBase': SurgicalProcedureBase,
    'SurgicalProcedureCreate': SurgicalProcedureCreate,
    'SurgicalProcedure': SurgicalProcedure,
    'SurveyResponseBase': SurveyResponseBase,
    'SurveyResponseCreate': SurveyResponseCreate,
    'SurveyResponse': SurveyResponse,
    'SurveyBase': SurveyBase,
    'SurveyCreate': SurveyCreate,
    'Survey': Survey,
    'TelemedicineSessionBase': TelemedicineSessionBase,
    'TelemedicineSessionCreate': TelemedicineSessionCreate,
    'TelemedicineSession': TelemedicineSession,
    'TriageAssessmentBase': TriageAssessmentBase,
    'TriageAssessmentCreate': TriageAssessmentCreate,
    'TriageAssessment': TriageAssessment,
    'VisualAcuityExamBase': VisualAcuityExamBase,
    'VisualAcuityExamCreate': VisualAcuityExamCreate,
    'VisualAcuityExam': VisualAcuityExam,
    'WorkflowInstanceBase': WorkflowInstanceBase,
    'WorkflowInstanceCreate': WorkflowInstanceCreate,
    'WorkflowInstance': WorkflowInstance,
    'WorkflowTemplateBase': WorkflowTemplateBase,
    'WorkflowTemplateCreate': WorkflowTemplateCreate,
    'WorkflowTemplate': WorkflowTemplate
})()
