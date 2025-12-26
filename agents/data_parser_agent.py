
class DataParserAgent:
    def parse(self, raw_data):
        return {
            "name": raw_data["product_name"],
            "concentration": raw_data["concentration"],
            "ingredients": raw_data["key_ingredients"],
            "benefits": raw_data["benefits"],
            "usage": raw_data["how_to_use"],
            "side_effects": raw_data["side_effects"],
            "price": raw_data["price"]
        }
