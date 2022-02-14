import uuid
class Prescription:
    def __init__(self, type_prescription, patient, doctor, quantity, dosage):
        self.id = str(uuid.uuid4())
        self.type_prescription = type_prescription
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage

