from typing import List
import uuid
from helpers.appointment_types import AppointmentType

from models.appointment import Appointment
from models.prescription import Prescription
from models.receptionist import Receptionist


class Patient:

    def __init___(name, address, phone_number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.phone_number = phone_number
    

    def request_appointment(self, appointment_schedule, receptionist) -> List[Appointment]:
        date_time_available, staff_id  = receptionist.find_available_time(appointment_schedule)
        appointment_schedule = receptionist.make_appointment(self.id, staff_id, AppointmentType.APPOINTMENT, date_time_available, appointment_schedule)
        return appointment_schedule

    def request_repeat(self) -> Prescription:
        pass