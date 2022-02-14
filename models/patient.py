

from models.appointment import Appointment
from models.prescription import Prescription


class Patient:

    def __init___(name, address, phone_number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.phone_number = phone_number
    

    def request_appointment(self) -> Appointment:
        pass

    def request_repeat(self) -> Prescription:
        pass