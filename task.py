class student:
    # Step 1: Class variable
    total_students = 0

    def __init__(self, id, name, class_name):
        self.id = id
        self.name = name
        self.class_name = class_name

        # Increment total_students each time a student is created
        student.total_students += 1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Class: {self.class_name}"

    def hello(self):
        print("Hello")

    # Step 2: introduce() method
    def introduce(self):
        print(f"Hi, I am {self.name} from {self.class_name} class. My ID is {self.id}.")


# Step 3: Create 3 student objects
s1 = student(1, "Ali", "CS4th AI")
s2 = student(2, "Sara", "CS4th AI")
s3 = student(3, "John", "CS4th AI")

# Call introduce() for each
s1.introduce()
s2.introduce()
s3.introduce()

# Print total number of students
print(f"Total number of students: {student.total_students}")
