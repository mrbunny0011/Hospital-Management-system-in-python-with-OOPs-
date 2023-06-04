# HOSPITAL CLASS
class Hospital:
    def __init__(self, name, location, opening_time, closing_time):
        self.name = name
        self.location = location
        self.opening_time = opening_time
        self.closing_time = closing_time

    def display(self):
        print("HOSPITAL NAME            : ", self.name)
        print("HOSPITAL LOCATION        : ", self.location)
        print("HOSPITAL OPENING TIME    : ", self.opening_time)
        print("HOSPITAL CLOSING TIME    : ", self.closing_time)


# PATIENT CLASS
class Patient:
    def __init__(self, name, disease_name, token_no):
        self.name = name
        self.disease_name = disease_name
        self.token_no = token_no

    def display(self):
        print("PATIENT NAME      : ", self.name)
        print("DISEASE NAME      : ", self.disease_name)
        print("TOKEN NUMBER      : ", self.token_no)


# DOCTOR CLASS
class Doctor:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


class Cardiologist(Doctor):
    def working(self):
        print("A cardiologist is a physician who is an expert in the care of your heart and blood vessels")

    specialization = "HEART specialist"

    def display(self):
        print("         CARDIOLOGIST DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("specialization : ", self.specialization)


class Pediatrician(Doctor):
    def working(self):
        print("A doctor who has special training in preventing, diagnosing, and treating diseases and injuries in children.")

    specialization = "DISEASE AND INJURIES IN CHILDREN"

    def display(self):
        print("         PEDIATRICIAN DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("specialization : ", self.specialization)


class Neurologist(Doctor):
    def working(self):
        print("Neurologists are specialists who treat diseases of the brain and spinal cord, peripheral nerves, and muscles")

    specialization = "specialization in NEUROLOGY"

    def display(self):
        print("         NEUROLOGIST DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("specialization : ", self.specialization)


# MAIN CODE
patients = []

a = 1

while a == 1:
    print("****** HOSPITAL MANAGEMENT *********")
    print("Press '1' for Hospital details")
    print("Press '2' for Doctor details")
    print("Press '3' for Patient Entry")
    print("Press '4' for patient details")
    print("Press '5' to Exit")
    try:
        num = int(input("Enter your number: "))
        if num == 1:
            print("___******____")
            obj = Hospital('NISHTER', 'NEW MULTAN', '7:00am', '11:00pm')
            obj.display()

        elif num == 2:
            print(" **There are three types of Doctors here**")
            print("1: Cardiologist")
            print("2: Pediatrician")
            print("3: Neurologist")
            num_doc = int(input("Enter your number for any doctor details: "))

            if num_doc == 1:
                print("_*******_")
                obj = Cardiologist("01", "Dr.Daniyal")
                obj.display()
                obj.working()

            elif num_doc == 2:
                print("_*******_")
                obj = Pediatrician("02", "Dr.Mubeen")
                obj.display()
                obj.working()

            elif num_doc == 3:
                print("_*******_")
                obj = Neurologist("03", "Dr.Sufyan")
                obj.display()
                obj.working()

        elif num == 3:
            print("____PATIENT ENTRY______")
            try:
                name = input("Enter patient name: ")
            except:
                print("Invalid Input")
            try:
                disease = input("Enter Patient disease: ")
            except:
                print("Invalid Input")
            try:
                token_no = int(input("Enter your Token Number: "))
            except:
                print("Invalid Input")
            obj = Patient(name, disease, token_no)
            patients.append(obj)
            print("Patient details entered.")

        elif num == 4:
            print("____PATIENT DETAILS______")
            for patient in patients:
                print("Patient name:      ", patient.name)
                print("Patient's disease: ", patient.disease_name)
                print("Token#:            ", patient.token_no)

        elif num == 5:
            print("___******____")
            print("Thanks for visiting.")
            a = 0
        else:
            print("Invalid Input. Try again")
    except:
        print("Aap ko sharam nahi aati. Menu mein se koi cheez choose karen")