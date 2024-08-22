# bicycle.py

class Bicycle:
    def __init__(self, color, type, wear):
        self.color = color
        self.type = type
        self.wear = wear
        self.owner = None

    def __str__(self):
        owner_info = f", Propietario: {self.owner}" if self.owner else ""
        return f"Color: {self.color}, Tipo: {self.type}, Desgaste: {self.wear}{owner_info}"

    def calculate_wear(self, distance):
        wear_increase_per_km = 0.1  # Ejemplo: 0.1% de desgaste por km
        return min(self.wear + (distance * wear_increase_per_km), 100)

    def calculate_next_maintenance(self, distance):
        maintenance_interval = 1000  # Ejemplo: cada 1000 km
        return max(0, maintenance_interval - distance)

