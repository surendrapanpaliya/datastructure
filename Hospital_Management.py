class Graph:
    def __init__(self):
        # Graph structure represented as an adjacency list
        self.graph = {}

    # Add a new doctor (node) to the graph
    def add_doctor(self, doctor_id, doctor_name, department):
        if doctor_id not in self.graph:
            self.graph[doctor_id] = {
                "name": doctor_name,
                "type": "doctor",
                "department": department,
                "appointments": []
            }
            print(f"Doctor {doctor_name} (Department: {department}) added.")
        else:
            print(f"Doctor {doctor_name} already exists.")

    # Add a new patient (node) to the graph
    def add_patient(self, patient_id, patient_name):
        if patient_id not in self.graph:
            self.graph[patient_id] = {
                "name": patient_name,
                "type": "patient",
                "appointments": []
            }
            print(f"Patient {patient_name} added.")
        else:
            print(f"Patient {patient_name} already exists.")

    # Create a booking (an edge) between a patient and a doctor
    def create_booking(self, doctor_id, patient_id, appointment_time, duration):
        # Check if doctor and patient exist
        if doctor_id in self.graph and patient_id in self.graph:
            doctor = self.graph[doctor_id]
            patient = self.graph[patient_id]

            # Add appointment to both doctor and patient nodes
            appointment_details = {
                "patient_id": patient_id,
                "patient_name": patient["name"],
                "time": appointment_time,
                "duration": duration
            }
            doctor["appointments"].append(appointment_details)

            appointment_details_patient = {
                "doctor_id": doctor_id,
                "doctor_name": doctor["name"],
                "time": appointment_time,
                "duration": duration
            }
            patient["appointments"].append(appointment_details_patient)

            print(f"Booking created: Doctor {doctor['name']} with Patient {patient['name']} at {appointment_time} for {duration} minutes.")
        else:
            print("Either the doctor or patient does not exist.")

    # View doctor schedule
    def view_doctor_schedule(self, doctor_id):
        if doctor_id in self.graph:
            doctor = self.graph[doctor_id]
            if doctor["appointments"]:
                print(f"Doctor {doctor['name']}'s Schedule:")
                for appointment in doctor["appointments"]:
                    print(f"- Patient: {appointment['patient_name']}, Time: {appointment['time']}, Duration: {appointment['duration']} mins")
            else:
                print(f"Doctor {doctor['name']} has no appointments.")
        else:
            print(f"Doctor with ID {doctor_id} does not exist.")

    # View patient appointments
    def view_patient_appointments(self, patient_id):
        if patient_id in self.graph:
            patient = self.graph[patient_id]
            if patient["appointments"]:
                print(f"Patient {patient['name']}'s Appointments:")
                for appointment in patient["appointments"]:
                    print(f"- Doctor: {appointment['doctor_name']}, Time: {appointment['time']}, Duration: {appointment['duration']} mins")
            else:
                print(f"Patient {patient['name']} has no appointments.")
        else:
            print(f"Patient with ID {patient_id} does not exist.")

    # View all doctors in the system
    def view_all_doctors(self):
        print("Doctors in the hospital:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "doctor":
                print(f"- Doctor ID: {node_id}, Name: {node_data['name']}, Department: {node_data['department']}")

    # View all patients in the system
    def view_all_patients(self):
        print("Patients in the hospital:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "patient":
                print(f"- Patient ID: {node_id}, Name: {node_data['name']}")

    # View all appointments (edges)
    def view_all_appointments(self):
        print("All appointments:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "doctor":
                for appointment in node_data["appointments"]:
                    print(f"- Doctor: {node_data['name']}, Patient: {appointment['patient_name']}, Time: {appointment['time']}, Duration: {appointment['duration']} mins")


# Example usage of the Hospital Management System
if __name__ == "__main__":
    hospital = Graph()

    # Add doctors
    hospital.add_doctor("D1", "Dr. Smith", "Cardiology")
    hospital.add_doctor("D2", "Dr. Johnson", "Pediatrics")

    # Add patients
    hospital.add_patient("P1", "Alice")
    hospital.add_patient("P2", "Bob")

    # Create bookings (appointments)
    hospital.create_booking("D1", "P1", "10:00 AM", 30)  # Dr. Smith with Alice
    hospital.create_booking("D2", "P2", "11:00 AM", 45)  # Dr. Johnson with Bob

    # View doctors and patients
    hospital.view_all_doctors()
    hospital.view_all_patients()

    # View appointments
    hospital.view_all_appointments()

    # View individual doctor schedule and patient appointments
    hospital.view_doctor_schedule("D1")
    hospital.view_patient_appointments("P1")



# Nodes represent entities such as doctors, patients, and departments.
# Edges represent relationships, such as doctor-patient relationships, or
# patient-department interactions.
# We can also use a weighted graph where edge weights represent appointment
# durations or priority.

#Key Concepts:
# Doctors and Patients as Nodes: Doctors and patients are modeled as nodes,
# and edges between them represent bookings (appointments).
# Department as Nodes: Departments can be connected to doctors to indicate
# which doctor belongs to which department.
# Booking Management: This allows managing patient appointments with
# doctors, ensuring that relationships (bookings) between nodes are updated efficiently.

'''
Explanation:
1.	Graph Representation:
o	The graph is represented as an adjacency list, where the nodes
represent doctors and patients.
o	The appointments between doctors and patients are represented
by edges in the graph, stored as a list of dictionaries within
each node (doctor and patient).

2.	Functions:
o	add_doctor: Adds a doctor node to the graph with doctor information
(ID, name, department).
o	add_patient: Adds a patient node to the graph with patient
information (ID, name).

o	create_booking: Establishes an appointment (an edge) between a doctor and a
patient, storing appointment details such as time and duration.

o	view_doctor_schedule: Displays all the appointments for a specific doctor.

o	view_patient_appointments: Displays all the appointments for
a specific patient.
o	view_all_doctors: Lists all doctors in the system.
o	view_all_patients: Lists all patients in the system.
o	view_all_appointments: Displays all appointments (bookings)
between doctors and patients.

3.	Booking Management:
o	The function create_booking establishes a relationship between
a doctor and a patient by storing the appointment details in both nodes.
The doctor’s node stores the patient details, and the patient’s
node stores the doctor’s details.
o	Both doctor and patient nodes are updated to maintain consistency,
ensuring efficient bidirectional access to booking information.

Key Points:
•	Nodes in the graph represent doctors and patients.
•	Edges (appointments) connect patients with doctors, storing booking details.
•	Graph Traversal: The system efficiently retrieves schedules and appointments
using the adjacency list representation.
•	The system can be extended to include more features like
department management, cancellation of appointments, or
appointment rescheduling.
This system demonstrates how graphs can model real-world relationships
in hospital management systems, providing an efficient way
to manage doctor-patient interactions.


'''
