import uuid
class Appointment:

    def __init__(self, patient_id, staff_id, type_appointment, date_time_available, available_schedule):
        self.id = str(uuid.uuid4())
        self.patient_id = patient_id
        self.staff_id = staff_id
        self.type_appointment = type_appointment
        self.date_time_available = date_time_available
        self.available_schedule = available_schedule
        self.status = "scheduled"