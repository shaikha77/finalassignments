import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from ppmr import Employee, Event, Client
from pppmr import Guest, Supplier, Venue, Caterer


class EventManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Management System")
        self.geometry("600x400")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.employee_frame = EmployeeManagementFrame(self.notebook)
        self.event_frame = EventManagementFrame(self.notebook)
        self.client_frame = ClientManagementFrame(self.notebook)
        self.guest_frame = GuestManagementFrame(self.notebook)
        self.supplier_frame = SupplierManagementFrame(self.notebook)
        self.venue_frame = VenueManagementFrame(self.notebook)
        self.caterer_frame = CatererManagementFrame(self.notebook)

        self.notebook.add(self.employee_frame, text="Employees")
        self.notebook.add(self.event_frame, text="Events")
        self.notebook.add(self.client_frame, text="Clients")
        self.notebook.add(self.guest_frame, text="Guests")
        self.notebook.add(self.supplier_frame, text="Suppliers")
        self.notebook.add(self.venue_frame, text="Venues")
        self.notebook.add(self.caterer_frame, text="Caterers")


class EmployeeManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Employee Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Employee", command=self.modify_employee)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Employee Details", command=self.display_employee_details)
        self.display_button.pack()

        # Dummy data for testing
        self.employees = []

    def add_employee(self):
        name = simpledialog.askstring("Employee Details", "Enter Name:")
        employee_id = simpledialog.askstring("Employee Details", "Enter Employee ID:")
        department = simpledialog.askstring("Employee Details", "Enter Department:")
        job_title = simpledialog.askstring("Employee Details", "Enter Job Title:")
        basic_salary = simpledialog.askfloat("Employee Details", "Enter Basic Salary:")
        age = simpledialog.askinteger("Employee Details", "Enter Age:")
        date_of_birth = simpledialog.askstring("Employee Details", "Enter Date of Birth:")
        passport_details = simpledialog.askstring("Employee Details", "Enter Passport Details:")

        new_employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth,
                                passport_details)
        self.employees.append(new_employee)

    def delete_employee(self):
        employee_id = simpledialog.askstring("Delete Employee", "Enter Employee ID to delete:")
        for employee in self.employees:
            if employee.employeeID == employee_id:
                self.employees.remove(employee)
                messagebox.showinfo("Success", "Employee deleted successfully.")
                return
        messagebox.showerror("Error", "Employee not found.")

    def modify_employee(self):
        employee_id = simpledialog.askstring("Modify Employee", "Enter Employee ID to modify:")
        for employee in self.employees:
            if employee.employeeID == employee_id:
                name = simpledialog.askstring("Modify Employee", f"Enter new name for {employee.name}:")
                employee.setName(name)
                messagebox.showinfo("Success", "Employee modified successfully.")
                return
        messagebox.showerror("Error", "Employee not found.")

    def display_employee_details(self):
        employee_id = simpledialog.askstring("Display Employee Details", "Enter Employee ID to display:")
        for employee in self.employees:
            if employee.employeeID == employee_id:
                details = f"Name: {employee.name}\nEmployee ID: {employee.employeeID}\nDepartment: {employee.department}\nJob Title: {employee.jobTitle}\nBasic Salary: {employee.basicSalary}\nAge: {employee.age}\nDate of Birth: {employee.dateOfBirth}\nPassport Details: {employee.passportDetails}"
                messagebox.showinfo("Employee Details", details)
                return
        messagebox.showerror("Error", "Employee not found.")


class EventManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Event Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Event", command=self.modify_event)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Event Details", command=self.display_event_details)
        self.display_button.pack()

        # Dummy data for testing
        self.events = []

    def add_event(self):
        event_id = simpledialog.askstring("Event Details", "Enter Event ID:")
        type = simpledialog.askstring("Event Details", "Enter Type:")
        theme = simpledialog.askstring("Event Details", "Enter Theme:")
        date = simpledialog.askstring("Event Details", "Enter Date:")
        venue_address = simpledialog.askstring("Event Details", "Enter Venue Address:")
        client_id = simpledialog.askstring("Event Details", "Enter Client ID:")

        new_event = Event(event_id, type, theme, date, venue_address, client_id)
        self.events.append(new_event)

    def delete_event(self):
        event_id = simpledialog.askstring("Delete Event", "Enter Event ID to delete:")
        for event in self.events:
            if event.eventID == event_id:
                self.events.remove(event)
                messagebox.showinfo("Success", "Event deleted successfully.")
                return
        messagebox.showerror("Error", "Event not found.")

    def modify_event(self):
        event_id = simpledialog.askstring("Modify Event", "Enter Event ID to modify:")
        for event in self.events:
            if event.eventID == event_id:
                type = simpledialog.askstring("Modify Event", f"Enter new type for {event.type}:")
                event.setType(type)
                messagebox.showinfo("Success", "Event modified successfully.")
                return
        messagebox.showerror("Error", "Event not found.")

    def display_event_details(self):
        event_id = simpledialog.askstring("Display Event Details", "Enter Event ID to display:")
        for event in self.events:
            if event.eventID == event_id:
                details = f"Event ID: {event.eventID}\nType: {event.type}\nTheme: {event.theme}\nDate: {event.date}\nVenue Address: {event.venueAddress}\nClient ID: {event.clientID}"
                messagebox.showinfo("Event Details", details)
                return
        messagebox.showerror("Error", "Event not found.")


class ClientManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Client Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Client", command=self.add_client)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Client", command=self.delete_client)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Client", command=self.modify_client)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Client Details", command=self.display_client_details)
        self.display_button.pack()

        # Dummy data for testing
        self.clients = []

    def add_client(self):
        client_id = simpledialog.askstring("Client Details", "Enter Client ID:")
        name = simpledialog.askstring("Client Details", "Enter Name:")
        address = simpledialog.askstring("Client Details", "Enter Address:")
        contact_details = simpledialog.askstring("Client Details", "Enter Contact Details:")
        budget = simpledialog.askfloat("Client Details", "Enter Budget:")

        new_client = Client(client_id, name, address, contact_details, budget)
        self.clients.append(new_client)

    def delete_client(self):
        client_id = simpledialog.askstring("Delete Client", "Enter Client ID to delete:")
        for client in self.clients:
            if client.clientID == client_id:
                self.clients.remove(client)
                messagebox.showinfo("Success", "Client deleted successfully.")
                return
        messagebox.showerror("Error", "Client not found.")

    def modify_client(self):
        client_id = simpledialog.askstring("Modify Client", "Enter Client ID to modify:")
        for client in self.clients:
            if client.clientID == client_id:
                name = simpledialog.askstring("Modify Client", f"Enter new name for {client.name}:")
                client.setName(name)
                messagebox.showinfo("Success", "Client modified successfully.")
                return
        messagebox.showerror("Error", "Client not found.")

    def display_client_details(self):
        client_id = simpledialog.askstring("Display Client Details", "Enter Client ID to display:")
        for client in self.clients:
            if client.clientID == client_id:
                details = f"Client ID: {client.clientID}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contactDetails}\nBudget: {client.budget}"
                messagebox.showinfo("Client Details", details)
                return
        messagebox.showerror("Error", "Client not found.")


class GuestManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Guest Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Guest", command=self.add_guest)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Guest", command=self.delete_guest)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Guest", command=self.modify_guest)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Guest Details", command=self.display_guest_details)
        self.display_button.pack()

        # Dummy data for testing
        self.guests = []

    def add_guest(self):
        guest_id = simpledialog.askstring("Guest Details", "Enter Guest ID:")
        name = simpledialog.askstring("Guest Details", "Enter Name:")
        address = simpledialog.askstring("Guest Details", "Enter Address:")
        contact_details = simpledialog.askstring("Guest Details", "Enter Contact Details:")

        new_guest = Guest(guest_id, name, address, contact_details)
        self.guests.append(new_guest)

    def delete_guest(self):
        guest_id = simpledialog.askstring("Delete Guest", "Enter Guest ID to delete:")
        for guest in self.guests:
            if guest.guestID == guest_id:
                self.guests.remove(guest)
                messagebox.showinfo("Success", "Guest deleted successfully.")
                return
        messagebox.showerror("Error", "Guest not found.")

    def modify_guest(self):
        guest_id = simpledialog.askstring("Modify Guest", "Enter Guest ID to modify:")
        for guest in self.guests:
            if guest.guestID == guest_id:
                name = simpledialog.askstring("Modify Guest", f"Enter new name for {guest.name}:")
                guest.setName(name)
                messagebox.showinfo("Success", "Guest modified successfully.")
                return
        messagebox.showerror("Error", "Guest not found.")

    def display_guest_details(self):
        guest_id = simpledialog.askstring("Display Guest Details", "Enter Guest ID to display:")
        for guest in self.guests:
            if guest.guestID == guest_id:
                details = f"Guest ID: {guest.guestID}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contactDetails}"
                messagebox.showinfo("Guest Details", details)
                return
        messagebox.showerror("Error", "Guest not found.")


class SupplierManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Supplier Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Supplier", command=self.add_supplier)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Supplier", command=self.modify_supplier)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Supplier Details", command=self.display_supplier_details)
        self.display_button.pack()

        # Dummy data for testing
        self.suppliers = []

    def add_supplier(self):
        supplier_id = simpledialog.askstring("Supplier Details", "Enter Supplier ID:")
        name = simpledialog.askstring("Supplier Details", "Enter Name:")
        address = simpledialog.askstring("Supplier Details", "Enter Address:")
        contact_details = simpledialog.askstring("Supplier Details", "Enter Contact Details:")

        new_supplier = Supplier(supplier_id, name, address, contact_details)
        self.suppliers.append(new_supplier)

    def delete_supplier(self):
        supplier_id = simpledialog.askstring("Delete Supplier", "Enter Supplier ID to delete:")
        for supplier in self.suppliers:
            if supplier.supplierID == supplier_id:
                self.suppliers.remove(supplier)
                messagebox.showinfo("Success", "Supplier deleted successfully.")
                return
        messagebox.showerror("Error", "Supplier not found.")

    def modify_supplier(self):
        supplier_id = simpledialog.askstring("Modify Supplier", "Enter Supplier ID to modify:")
        for supplier in self.suppliers:
            if supplier.supplierID == supplier_id:
                name = simpledialog.askstring("Modify Supplier", f"Enter new name for {supplier.name}:")
                supplier.setName(name)
                messagebox.showinfo("Success", "Supplier modified successfully.")
                return
        messagebox.showerror("Error", "Supplier not found.")

    def display_supplier_details(self):
        supplier_id = simpledialog.askstring("Display Supplier Details", "Enter Supplier ID to display:")
        for supplier in self.suppliers:
            if supplier.supplierID == supplier_id:
                details = f"Supplier ID: {supplier.supplierID}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contactDetails}"
                messagebox.showinfo("Supplier Details", details)
                return
        messagebox.showerror("Error", "Supplier not found.")


class VenueManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Venue Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Venue", command=self.add_venue)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Venue", command=self.delete_venue)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Venue", command=self.modify_venue)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Venue Details", command=self.display_venue_details)
        self.display_button.pack()

        # Dummy data for testing
        self.venues = []

    def add_venue(self):
        venue_id = simpledialog.askstring("Venue Details", "Enter Venue ID:")
        name = simpledialog.askstring("Venue Details", "Enter Name:")
        address = simpledialog.askstring("Venue Details", "Enter Address:")
        contact = simpledialog.askstring("Venue Details", "Enter Contact:")
        min_guests = simpledialog.askinteger("Venue Details", "Enter Minimum Guests:")
        max_guests = simpledialog.askinteger("Venue Details", "Enter Maximum Guests:")

        new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        self.venues.append(new_venue)

    def delete_venue(self):
        venue_id = simpledialog.askstring("Delete Venue", "Enter Venue ID to delete:")
        for venue in self.venues:
            if venue.venueID == venue_id:
                self.venues.remove(venue)
                messagebox.showinfo("Success", "Venue deleted successfully.")
                return
        messagebox.showerror("Error", "Venue not found.")

    def modify_venue(self):
        venue_id = simpledialog.askstring("Modify Venue", "Enter Venue ID to modify:")
        for venue in self.venues:
            if venue.venueID == venue_id:
                name = simpledialog.askstring("Modify Venue", f"Enter new name for {venue.name}:")
                venue.setName(name)
                messagebox.showinfo("Success", "Venue modified successfully.")
                return
        messagebox.showerror("Error", "Venue not found.")

    def display_venue_details(self):
        venue_id = simpledialog.askstring("Display Venue Details", "Enter Venue ID to display:")
        for venue in self.venues:
            if venue.venueID == venue_id:
                details = f"Venue ID: {venue.venueID}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMin Guests: {venue.minGuests}\nMax Guests: {venue.maxGuests}"
                messagebox.showinfo("Venue Details", details)
                return
        messagebox.showerror("Error", "Venue not found.")


class CatererManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self, text="Caterer Management")
        self.label.pack()

        self.add_button = ttk.Button(self, text="Add Caterer", command=self.add_caterer)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Caterer", command=self.delete_caterer)
        self.delete_button.pack()

        self.modify_button = ttk.Button(self, text="Modify Caterer", command=self.modify_caterer)
        self.modify_button.pack()

        self.display_button = ttk.Button(self, text="Display Caterer Details", command=self.display_caterer_details)
        self.display_button.pack()

        # Dummy data for testing
        self.caterers = []

    def add_caterer(self):
        caterer_id = simpledialog.askstring("Caterer Details", "Enter Caterer ID:")
        name = simpledialog.askstring("Caterer Details", "Enter Name:")
        address = simpledialog.askstring("Caterer Details", "Enter Address:")
        contact_details = simpledialog.askstring("Caterer Details", "Enter Contact Details:")
        menu = simpledialog.askstring("Caterer Details", "Enter Menu:")
        min_guests = simpledialog.askinteger("Caterer Details", "Enter Minimum Guests:")
        max_guests = simpledialog.askinteger("Caterer Details", "Enter Maximum Guests:")

        new_caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
        self.caterers.append(new_caterer)

    def delete_caterer(self):
        caterer_id = simpledialog.askstring("Delete Caterer", "Enter Caterer ID to delete:")
        for caterer in self.caterers:
            if caterer.catererID == caterer_id:
                self.caterers.remove(caterer)
                messagebox.showinfo("Success", "Caterer deleted successfully.")
                return
        messagebox.showerror("Error", "Caterer not found.")

    def modify_caterer(self):
        caterer_id = simpledialog.askstring("Modify Caterer", "Enter Caterer ID to modify:")
        for caterer in self.caterers:
            if caterer.catererID == caterer_id:
                name = simpledialog.askstring("Modify Caterer", f"Enter new name for {caterer.name}:")
                caterer.setName(name)
                messagebox.showinfo("Success", "Caterer modified successfully.")
                return
        messagebox.showerror("Error", "Caterer not found.")

    def display_caterer_details(self):
        caterer_id = simpledialog.askstring("Display Caterer Details", "Enter Caterer ID to display:")
        for caterer in self.caterers:
            if caterer.catererID == caterer_id:
                details = f"Caterer ID: {caterer.catererID}\nName: {caterer.name}\nAddress: {caterer.address}\nContact Details: {caterer.contactDetails}\nMenu: {caterer.menu}\nMin Guests: {caterer.minGuests}\nMax Guests: {caterer.maxGuests}"
                messagebox.showinfo("Caterer Details", details)
                return
        messagebox.showerror("Error", "Caterer not found.")


if __name__ == "__main__":
    app = EventManagementApp()
    app.mainloop()
