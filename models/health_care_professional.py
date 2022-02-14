import uuid

class HealthCareProfessional:

    def __init___(name, employee_number, consultation=""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.employee_number = employee_number
        self.consultation = consultation
    
