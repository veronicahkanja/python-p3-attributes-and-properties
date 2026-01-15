#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # Class attribute: list of approved jobs
    approved_jobs = [
        "Admin", 
        "Customer Service", 
        "Human Resources", 
        "ITC",
        "Production", 
        "Legal", 
        "Finance", 
        "Sales",
        "General Management", 
        "Research & Development",
        "Marketing", 
        "Purchasing"
    ]

    def __init__(self, name="Person", job="Admin"):
        # Set attributes using property setters
        self.name = name
        self.job = job

    # Name property
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Job property
    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
