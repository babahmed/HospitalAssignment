from health_care_professional import HealthCareProfessional
from models.prescription import Prescription





class Doctor(HealthCareProfessional):
    
    def __init__(self, name, employee_number, consultation) -> None:
        super().__init__(name, employee_number, consultation)

    def issue_prescription(self, patient_id, prescription) -> Prescription:
        pass
