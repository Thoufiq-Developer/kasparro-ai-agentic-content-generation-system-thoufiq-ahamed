
def product_template(product):
    return {
        "product_name": product["name"],
        "ingredients": product["ingredients"],
        "benefits": product["benefits"],
        "usage": product["usage"],
        "price": product["price"]
    }
