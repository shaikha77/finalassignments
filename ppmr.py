
class Employee:
    """Represents an employee within the event management system."""

    def __init__(self, employee_id, name, department, job_title, basic_salary):
        # Constructor to initialize the Employee object with various attributes
        self._employee_id = employee_id
        self._name = name
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary

    # Getter method for employee ID
    def get_employee_id(self):
        return self._employee_id

    # Setter method for employee ID
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    # Getter method for employee name
    def get_name(self):
        return self._name

    # Setter method for employee name
    def set_name(self, name):
        self._name = name

    # Getter method for department
    def get_department(self):
        return self._department

    # Setter method for department
    def set_department(self, department):
        self._department = department

    # Getter method for job title
    def get_job_title(self):
        return self._job_title

    # Setter method for job title
    def set_job_title(self, job_title):
        self._job_title = job_title

    # Getter method for basic salary
    def get_basic_salary(self):
        return self._basic_salary

    # Setter method for basic salary
    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary


class Event:
    """Represents an event, encapsulating details like type, date, and associated client."""

    def __init__(self, event_id, type, theme, date, time, venue_id, client_id):
        # Constructor to initialize the Event object with necessary event-specific attributes
        self._event_id = event_id
        self._type = type
        self._theme = theme
        self._date = date
        self._time = time
        self._venue_id = venue_id
        self._client_id = client_id

    # Getter and setter methods for all event-specific attributes
    def get_event_id(self):
        return self._event_id

    def set_event_id(self, event_id):
        self._event_id = event_id

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_theme(self):
        return self._theme

    def set_theme(self, theme):
        self._theme = theme

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_venue_id(self):
        return self._venue_id

    def set_venue_id(self, venue_id):
        self._venue_id = venue_id

    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id


class Client:
    """Manages client information for events."""

    def __init__(self, client_id, name, address, contact_details, budget, email, vip_status):
        # Constructor to initialize the Client object with necessary details for event management
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget
        self._email = email
        self._vip_status = vip_status

    # Getter and setter methods for all client-specific attributes
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_vip_status(self):
        return self._vip_status

    def set_vip_status(self, vip_status):
        self._vip_status = vip_status