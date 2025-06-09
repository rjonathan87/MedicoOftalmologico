# Guía Técnica de Implementación
## Sistema de Automatización para Clínica Oftalmológica

---

## ARQUITECTURA DEL SISTEMA

### Microservicios Principales

```mermaid
graph LR
    A[API Gateway] --> B[Auth Service]
    A --> C[Patient Service]
    A --> D[Appointment Service]
    A --> E[Medical Service]
    A --> F[Billing Service]
    A --> G[Inventory Service]
    A --> H[Notification Service]
    
    B --> I[(User DB)]
    C --> J[(Patient DB)]
    D --> K[(Schedule DB)]
    E --> L[(Medical DB)]
    F --> M[(Billing DB)]
    G --> N[(Inventory DB)]
    H --> O[Message Queue]
```

---

## IMPLEMENTACIONES DETALLADAS

### 1. CHATBOT INTELIGENTE DE PRE-SCREENING

#### Estructura del Proyecto:
```
chatbot_service/
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── nlp_model.py
│   │   └── screening_model.py
│   ├── services/
│   │   ├── conversation_service.py
│   │   └── classification_service.py
│   └── utils/
│       └── medical_keywords.py
├── training/
│   ├── train_model.py
│   └── data/
│       └── medical_conversations.json
└── requirements.txt
```

