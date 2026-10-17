# Conveyor Belt Waste Sorter & Mass Estimator
class ConveyorWasteSorter:
    def __init__(self, density_map=None):
        self.density_map = density_map or {"plastic": 0.05, "paper": 0.03, "metal": 0.25}
        self.total_estimated_kg = 0.0

    def estimate_item_mass(self, class_name, bbox):
        area_px = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
        density = self.density_map.get(class_name, 0.05)
        # Scaled volume approximation
        mass_kg = area_px * density * 0.001
        self.total_estimated_kg += mass_kg
        return mass_kg

if __name__ == "__main__":
    sorter = ConveyorWasteSorter()
    print("Conveyor Waste Sorter & Mass Estimator initialized.")
