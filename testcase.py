from ppmr import Employee, Event, Client
from pppmr import Guest, Supplier, Venue, Caterer

# Example of creating an Employee
employee1 = Employee("E001", "Meera Saeed", "Sales", "Sales Manager", 50000)
print(employee1)

# Example of creating an Event
event1 = Event("EV001", "Wedding", "Spring Blossom", "2024-04-30", "15:00", "V001", "C001")
print(event1)

# Example of creating a Client
client1 = Client("C001", "Shaikha Mohammad", "Warqaa road 13", "555-1234", 15000, "shaikha@example.com", True)
print(client1)

# Example of creating another Client
client2 = Client("C002", "Hind Ali", "ALawair street 5", "555-5678", 20000, "hind@example.com", False)
print(client2)

# Example of creating a Guest
guest1 = Guest("G001", "Roudha Ahli", "Silicone oasis 3", "555-6789", False, "Gluten-Free")
print(guest1)

# Example of creating another Guest
guest2 = Guest("G002", "Khalifa Saeed", "Alkhawaneej road 1", "555-9876", True, "Vegetarian")
print(guest2)

# Example of creating a Supplier
supplier1 = Supplier("S001", "Deluxe Arabic Catering", "2 street dubai ", "555-2020", "Catering", "08:00-22:00")
print(supplier1)

# Example of creating another Supplier
supplier2 = Supplier("S002", "Eleganza Decorations", "45 wasl St", "555-3030", "Decorations", "09:00-17:00")
print(supplier2)

# Example of creating a Venue
venue1 = Venue("V001", "Grand Dubai Hall", "10  blvd ", "555-4040", 100, 300)
print(venue1)

# Example of creating a Caterer
caterer1 = Caterer("CT001", "Maryam Omar Gourmet", "Deira street 1 ", "555-5050", "Full Service", 50, 200)
print(caterer1)
