from amazon import Amazon
from alert import Alert

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
PRODUCT_TARGET_PRICE = 100

product = Amazon(PRODUCT_URL)
product_data = product.get_product_data()
product_data['url'] = PRODUCT_URL

# If current product price is less than the target price, then send an email.
if product_data['price'] < PRODUCT_TARGET_PRICE:
    generate_alert = Alert(product_data)

