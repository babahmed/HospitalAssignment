import datetime
from health_care_professional import HealthCareProfessional
from models.appointment import Appointment

class Receptionist(HealthCareProfessional):
    def __init__(self, name, employee_number) -> None:
        super().__init__(name, employee_number)


    def make_appointment(self, patient_id, staff_id, booking_type, date_time_available, available_schedule):
        appointment  = Appointment(patient_id, staff_id, booking_type, date_time_available, available_schedule)
        available_schedule[appointment.id] = appointment
        return available_schedule

    def cancel_appointment(self, patient_id, appointment) -> None:
        pass

    def find_available_time(self) -> datetime:
        pass
