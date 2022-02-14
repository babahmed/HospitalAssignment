import uuid
class Appointment:

    def __init__(self, type_appointment, patient, staff):
        self.id = str(uuid.uuid4())
        self.patient = patient
        self.staff = staff
        self.type_appointment = type_appointment