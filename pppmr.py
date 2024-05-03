class Guest:
    """Manages guest information, including VIP status and dietary preferences for event planning."""

    def __init__(self, guest_id, name, address, contact_details, vip_status, dietary_preferences):
        # Constructor to initialize the Guest object with personal and preference details
        self._guest_id = guest_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._vip_status = vip_status
        self._dietary_preferences = dietary_preferences


    # Getter and setter methods for all guest-specific attributes
    def get_guest_id(self):
        return self._guest_id


    def set_guest_id(self, guest_id):
        self._guest_id = guest_id


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


    def get_vip_status(self):
        return self._vip_status


    def set_vip_status(self, vip_status):
        self._vip_status = vip_status


    def get_dietary_preferences(self):
        return self._dietary_preferences


    def set_dietary_preferences(self, dietary_preferences):
        self._dietary_preferences = dietary_preferences




class Supplier:
    """Handles supplier details for events, including service types and operating hours."""

    def __init__(self, supplier_id, name, address, contact_details, service_type, operating_hours):
        # Constructor to initialize the Supplier object with details for business operations
        self._supplier_id = supplier_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._service_type = service_type
        self._operating_hours = operating_hours


    # Getter and setter methods for all supplier-specific attributes
    def get_supplier_id(self):
        return self._supplier_id


    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id


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


    def get_service_type(self):
        return self._service_type


    def set_service_type(self, service_type):
        self._service_type = service_type


    def get_operating_hours(self):
        return self._operating_hours


    def set_operating_hours(self, operating_hours):
        self._operating_hours = operating_hours




class Venue:
    """Manages venue details for events, including capacity and accessibility features."""

    def __init__(self, venue_id, name, address, contact, parking_availability, accessibility_features):
        # Constructor to initialize the Venue object with essential location and facility details
        self._venue_id = venue_id
        self._name = name
        self._address = address
        self._contact = contact
        self._parking_availability = parking_availability
        self._accessibility_features = accessibility_features


    # Getter and setter methods for all venue-specific attributes
    def get_venue_id(self):
        return self._venue_id


    def set_venue_id(self, venue_id):
        self._venue_id = venue_id


    def get_name(self):
        return self._name


    def set_name(self, name):
        self._name = name


    def get_address(self):
        return self._address


    def set_address(self, address):
        self._address = address


    def get_contact(self):
        return self._contact


    def set_contact(self, contact):
        self._contact = contact


    def get_parking_availability(self):
        return self._parking_availability


    def set_parking_availability(self, parking_availability):
        self._parking_availability = parking_availability


    def get_accessibility_features(self):
        return self._accessibility_features


    def set_accessibility_features(self, accessibility_features):
        self._accessibility_features = accessibility_features




class Caterer(Supplier):
    """Specialized supplier managing catering services for events, including menus and guest capacity ranges."""

    def __init__(self, caterer_id, name, address, contact_details, menu, min_guests, max_guests):
        # Use the Supplier class constructor to handle common attributes
        super().__init__(caterer_id, name, address, contact_details, "Catering", "Varies")
        self._menu = menu
        self._min_guests = min_guests
        self._max_guests = max_guests


    # Getter and setter methods for catering-specific attributes
    def get_menu(self):
        return self._menu


    def set_menu(self, menu):
        self._menu = menu


    def get_min_guests(self):
        return self._min_guests


    def set_min_guests(self, min_guests):
        self._min_guests = min_guests


    def get_max_guests(self):
        return self._max_guests


    def set_max_guests(self, max_guests):
        self._max_guests = max_guests