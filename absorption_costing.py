
class Product:
    def __init__(self, name, units_produced):
        self.name = name
        self.units_produced = units_produced
        self.direct_materials_cost = 0
        self.direct_labor_cost = 0
        self.overhead_cost = 0

    def set_direct_materials_cost(self, cost):
        self.direct_materials_cost = cost

    def set_direct_labor_cost(self, cost):
        self.direct_labor_cost = cost

    def set_overhead_cost(self, cost):
        self.overhead_cost = cost

    def total_cost(self):
        return self.direct_materials_cost + self.direct_labor_cost + self.overhead_cost

    def unit_cost(self):
        return self.total_cost() / self.units_produced if self.units_produced else 0

class Cost:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

# Example usage
if __name__ == "__main__":
    product = Product("Widget", 1000)
    product.set_direct_materials_cost(5000)
    product.set_direct_labor_cost(3000)
    product.set_overhead_cost(2000)

    print(f"Total cost for {product.name}: ${product.total_cost()}")
    print(f"Unit cost for {product.name}: ${product.unit_cost()}")
