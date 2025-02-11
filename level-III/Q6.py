"""
6. Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance
"""

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_team(self):
        print(f"{self.name} manages the {self.department} department.")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        Employee.__init__(self, name, emp_id)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is coding in {self.programming_language}.")

class TechLead(Manager, Developer):
    def __init__(self, name, emp_id, department, programming_language, project):
        Manager.__init__(self, name, emp_id, department)
        Developer.__init__(self, name, emp_id, programming_language)
        self.project = project

    def lead_project(self):
        print(f"{self.name} is leading the {self.project} project.")

class SeniorTechLead(TechLead):
    def __init__(self, name, emp_id, department, programming_language, project, experience):
        TechLead.__init__(self, name, emp_id, department, programming_language, project)
        self.experience = experience

    def mentor_team(self):
        print(f"{self.name} is mentoring with {self.experience} years of experience.")


print("\n--- Single Inheritance Example ---")
manager = Manager("Alice", 101, "HR")
manager.display_info()
manager.manage_team()

print("\n--- Multiple Inheritance Example ---")
tech_lead = TechLead("Bob", 102, "IT", "Python", "AI Automation")
tech_lead.display_info()
tech_lead.manage_team()
tech_lead.write_code()
tech_lead.lead_project()

print("\n--- Multilevel Inheritance Example ---")
senior_lead = SeniorTechLead("Charlie", 103, "IT", "Java", "Cloud Migration", 10)
senior_lead.display_info()
senior_lead.manage_team()
senior_lead.write_code()
senior_lead.lead_project()
senior_lead.mentor_team()
