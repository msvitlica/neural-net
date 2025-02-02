import requests
from bs4 import BeautifulSoup
import json

# Osnovni URL sa paginacijom
base_url = "https://eshop.tropic.ba/?product-page="

# Lista za čuvanje proizvoda
products = []

# Definišemo broj stranica (možete ga povećati prema potrebi)
max_pages = 1444

for page in range(1, max_pages + 1):
    print(f"Scraping page {page}...")
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Pronađi sve proizvode na stranici
    product_elements = soup.find_all("li", class_="product")
    
    for product in product_elements:
        try:
            name = product.find("h2", class_="woocommerce-loop-product__title").text.strip()
            price = product.find("span", class_="woocommerce-Price-amount").text.strip().replace("KM", "").strip()
            product_url = product.find("a", class_="woocommerce-LoopProduct-link")["href"]
            image_url = product.find("img", class_="attachment-woocommerce_thumbnail")["src"]
            sku = product.find("a", class_="add_to_cart_button")["data-product_sku"]
            
            products.append({
                "name": name,
                "price_KM": float(price),
                "url": product_url,
                "image_url": image_url,
                "sku": sku
            })
        except Exception as e:
            print(f"Error processing product: {e}")

# Sačuvaj u JSON fajl
with open("tropic_products_1.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print(f"Scraping completed! {len(products)} products saved.")
