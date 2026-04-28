from ....product.usecases.get_all_products import get_all_products
from ....product import get_product_price
from ....account.user.models.customer_profile import Customer as Customer

def employee_list():
    employees = [
        {"id": 1, "name": "John Smith", "email": "john.smith@company.com", "age": 29, "department": "Sales"},
        {"id": 2, "name": "Maria Garcia", "email": "maria.garcia@company.com", "age": 34, "department": "Marketing"},
        {"id": 3, "name": "David Kim", "email": "david.kim@company.com", "age": 26, "department": "Engineering"},
        {"id": 4, "name": "Emma Brown", "email": "emma.brown@company.com", "age": 41, "department": "HR"},
        {"id": 5, "name": "Lucas Silva", "email": "lucas.silva@company.com", "age": 31, "department": "Finance"},
        {"id": 6, "name": "Olivia Wilson", "email": "olivia.wilson@company.com", "age": 27, "department": "Design"},
        {"id": 7, "name": "Noah Martinez", "email": "noah.martinez@company.com", "age": 36, "department": "Support"},
        {"id": 8, "name": "Isabella Lopez", "email": "isabella.lopez@company.com", "age": 30, "department": "Sales"},
        {"id": 9, "name": "Ethan Clark", "email": "ethan.clark@company.com", "age": 33, "department": "Engineering"},
        {"id": 10, "name": "Sophia Lewis", "email": "sophia.lewis@company.com", "age": 25, "department": "Marketing"},
        {"id": 11, "name": "Mason Walker", "email": "mason.walker@company.com", "age": 38, "department": "Finance"},
        {"id": 12, "name": "Ava Hall", "email": "ava.hall@company.com", "age": 28, "department": "HR"},
        {"id": 13, "name": "Logan Allen", "email": "logan.allen@company.com", "age": 42, "department": "Management"},
        {"id": 14, "name": "Mia Young", "email": "mia.young@company.com", "age": 24, "department": "Design"},
        {"id": 15, "name": "James Hernandez", "email": "james.hernandez@company.com", "age": 37, "department": "Support"},
        {"id": 16, "name": "Charlotte King", "email": "charlotte.king@company.com", "age": 29, "department": "Sales"},
        {"id": 17, "name": "Benjamin Wright", "email": "benjamin.wright@company.com", "age": 35, "department": "Engineering"},
        {"id": 18, "name": "Amelia Scott", "email": "amelia.scott@company.com", "age": 32, "department": "Marketing"},
        {"id": 19, "name": "Elijah Green", "email": "elijah.green@company.com", "age": 40, "department": "Finance"},
        {"id": 20, "name": "Harper Adams", "email": "harper.adams@company.com", "age": 27, "department": "HR"},
        {"id": 21, "name": "Alexander Baker", "email": "alexander.baker@company.com", "age": 39, "department": "Management"},
        {"id": 22, "name": "Evelyn Gonzalez", "email": "evelyn.gonzalez@company.com", "age": 26, "department": "Design"},
        {"id": 23, "name": "Daniel Nelson", "email": "daniel.nelson@company.com", "age": 34, "department": "Support"},
        {"id": 24, "name": "Abigail Carter", "email": "abigail.carter@company.com", "age": 31, "department": "Sales"},
        {"id": 25, "name": "Matthew Mitchell", "email": "matthew.mitchell@company.com", "age": 43, "department": "Engineering"},
        {"id": 26, "name": "Emily Perez", "email": "emily.perez@company.com", "age": 28, "department": "Marketing"},
        {"id": 27, "name": "Joseph Roberts", "email": "joseph.roberts@company.com", "age": 36, "department": "Finance"},
        {"id": 28, "name": "Ella Turner", "email": "ella.turner@company.com", "age": 25, "department": "HR"},
        {"id": 29, "name": "Samuel Phillips", "email": "samuel.phillips@company.com", "age": 38, "department": "Management"},
        {"id": 30, "name": "Scarlett Campbell", "email": "scarlett.campbell@company.com", "age": 29, "department": "Design"},
        {"id": 31, "name": "Henry Parker", "email": "henry.parker@company.com", "age": 33, "department": "Support"},
        {"id": 32, "name": "Sebastian Evans", "email": "sebastian.evans@company.com", "age": 41, "department": "Sales"},
        {"id": 33, "name": "Grace Edwards", "email": "grace.edwards@company.com", "age": 27, "department": "Engineering"},
        {"id": 34, "name": "Jack Collins", "email": "jack.collins@company.com", "age": 35, "department": "Marketing"},
        {"id": 35, "name": "Chloe Stewart", "email": "chloe.stewart@company.com", "age": 30, "department": "Finance"},
        {"id": 36, "name": "Owen Sanchez", "email": "owen.sanchez@company.com", "age": 37, "department": "HR"},
        {"id": 37, "name": "Lily Morris", "email": "lily.morris@company.com", "age": 26, "department": "Design"},
    ]
    return employees

def product_list():
    products = [
        {"id": 1, "name": "Wireless Mouse", "category": "Electronics", "stock": 120, "status": "Active"},
        {"id": 2, "name": "Mechanical Keyboard", "category": "Electronics", "stock": 75, "status": "Active"},
        {"id": 3, "name": "USB-C Cable", "category": "Accessories", "stock": 200, "status": "Active"},
        {"id": 4, "name": "Laptop Stand", "category": "Office", "stock": 50, "status": "Active"},
        {"id": 5, "name": "Noise Cancelling Headphones", "category": "Electronics", "stock": 30, "status": "Low Stock"},
        {"id": 6, "name": "Webcam HD", "category": "Electronics", "stock": 65, "status": "Active"},
        {"id": 7, "name": "Gaming Chair", "category": "Furniture", "stock": 15, "status": "Low Stock"},
        {"id": 8, "name": "Desk Lamp", "category": "Office", "stock": 90, "status": "Active"},
        {"id": 9, "name": "External Hard Drive", "category": "Storage", "stock": 40, "status": "Active"},
        {"id": 10, "name": "Monitor 24 inch", "category": "Electronics", "stock": 25, "status": "Active"},
        {"id": 11, "name": "Bluetooth Speaker", "category": "Audio", "stock": 60, "status": "Active"},
        {"id": 12, "name": "Smartphone Stand", "category": "Accessories", "stock": 110, "status": "Active"},
        {"id": 13, "name": "Portable Charger", "category": "Accessories", "stock": 85, "status": "Active"},
        {"id": 14, "name": "Office Desk", "category": "Furniture", "stock": 10, "status": "Low Stock"},
        {"id": 15, "name": "LED Strip Lights", "category": "Decor", "stock": 140, "status": "Active"},
    ]
    return products


def inventory_stock(products):
    inventory = []

    for product in products:
        item = {
            "id": product["id"],
            "name": product["name"],
            "stock": product["stock"],
            "unit": "kg",  # mock for now
            "status": "Low" if product["stock"] < 20 else "Normal",
        }
        inventory.append(item)

    return inventory





prices_table = {
    1: 25.99,
    2: 89.50,
    3: 9.99,
    4: 34.75,
    5: 199.99,
    6: 59.99,
    7: 150.00,
    8: 22.40,
    9: 120.00,
    10: 210.00,
    11: 75.25,
    12: 14.99,
    13: 29.99,
    14: 300.00,
    15: 18.99,
}




































##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

from ....account.user.models.employee_profile import Employee

def backoffice_view_context_handler():
    """LOAD DATA"""

    customers = Customer.objects.select_related("user").all()
    employees = Employee.objects.select_related("user").all()

    products = product_list()

    for product in products:
        product["current_price"] = prices_table.get(product["id"], 0)

    context = {
        "products": products,
        "inventory": inventory_stock(products),
        "customers": customers,
        "employees": employees,
    }
    return context