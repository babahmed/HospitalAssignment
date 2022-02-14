from health_care_professional import HealthCareProfessional
from models.appointment import Appointment

class Receptionist(HealthCareProfessional):
    def __init__(self, name, employee_number) -> None:
        super().__init__(name, employee_number)


    def make_appointment(self, patient_id, appointment) -> Appointment:
        pass

    def cancel_appointment(self, patient_id, appointment) -> None:
        pass
