from health_care_professional import HealthCareProfessional


class Nurse(HealthCareProfessional):
    
    
    def __init__(self, name, employee_number, consultation) -> None:
        super().__init__(name, employee_number, consultation)
