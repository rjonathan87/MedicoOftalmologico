import sys
sys.path.append(".")

from fastapi import FastAPI
from routers import (
    clinics, patients, roles, users, appointments, appointmentservices,
    auditlogs, clinical_protocols, clinical_studies, consentforms,
    consultations, contact_lens_prescriptions, data_access_logs, diagnoses,
    educational_resources, equipment, inventory_items, invoices, invoice_items,
    iop_exams, licenses_permits, maintenance_logs, marketing_campaigns,
    ophthalmological_images, optical_prescription_details, patient_education_tracking,
    patient_notifications, patient_portal_sessions, patient_communications,
    patient_documents, payments, performance_metrics, permissions, prescriptions,
    refraction_exams, resources, role_permissions, security_policies, services,
    surgical_procedures, surveys, survey_responses, telemedicine_sessions,
    triage_assessments, visual_acuity_exams, workflow_instances, workflow_templates
)
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clinics.router)
app.include_router(patients.router)
app.include_router(roles.router)
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(appointmentservices.router)
app.include_router(auditlogs.router)
app.include_router(clinical_protocols.router)
app.include_router(clinical_studies.router)
app.include_router(consentforms.router)
app.include_router(consultations.router)
app.include_router(contact_lens_prescriptions.router)
app.include_router(data_access_logs.router)
app.include_router(diagnoses.router)
app.include_router(educational_resources.router)
app.include_router(equipment.router)
app.include_router(inventory_items.router)
app.include_router(invoices.router)
app.include_router(invoice_items.router)
app.include_router(iop_exams.router)
app.include_router(licenses_permits.router)
app.include_router(maintenance_logs.router)
app.include_router(marketing_campaigns.router)
app.include_router(ophthalmological_images.router)
app.include_router(optical_prescription_details.router)
app.include_router(patient_education_tracking.router)
app.include_router(patient_notifications.router)
app.include_router(patient_portal_sessions.router)
app.include_router(patient_communications.router)
app.include_router(patient_documents.router)
app.include_router(payments.router)
app.include_router(performance_metrics.router)
app.include_router(permissions.router)
app.include_router(prescriptions.router)
app.include_router(refraction_exams.router)
app.include_router(resources.router)
app.include_router(role_permissions.router)
app.include_router(security_policies.router)
app.include_router(services.router)
app.include_router(surgical_procedures.router)
app.include_router(surveys.router)
app.include_router(survey_responses.router)
app.include_router(telemedicine_sessions.router)
app.include_router(triage_assessments.router)
app.include_router(visual_acuity_exams.router)
app.include_router(workflow_instances.router)
app.include_router(workflow_templates.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
