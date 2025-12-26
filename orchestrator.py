
from data.product_data import PRODUCT_DATA
from agents.data_parser_agent import DataParserAgent
from agents.page_assembler_agent import PageAssemblerAgent
from templates.product_template import product_template

def run_pipeline():
    product = DataParserAgent().parse(PRODUCT_DATA)
    PageAssemblerAgent().save("product_page.json", product_template(product))

if __name__ == "__main__":
    run_pipeline()
