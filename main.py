from models.receptionist import Receptionist

health_care_professionals =  {}
prescriptions =  {}
appointment_schedule =  {}
prescriptions =  {}
patients =  {}


def main():
    while True:
         if options == 1:
             patient  = input("Enter patient name: ")
             receptionist  = Receptionist()
             patient.request_appointment(appointment_schedule, receptionist)

if __name__ == "__main__":
    main()
