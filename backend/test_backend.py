import requests

REAL_TOKEN = "dari token frontend"
# dari backend (dummy item)
LISTING_ID = "175074eb-4b73-41f6-9a43-71435c8fd3df"

url = "http://127.0.0.1:8000/api/v1/orders"

headers = {"Authorization": f"Bearer {REAL_TOKEN}", "Content-Type": "application/json"}

data = {"listing_id": LISTING_ID}

print(f"Attempting to buy listing {LISTING_ID}...")

try:
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("\n✅ SUCCESS! The backend accepted your Google Token.")
        print("Order Details:", response.json())
    else:
        print("\n❌ FAILED")
        print("Status:", response.status_code)
        print("Error:", response.text)

except Exception as e:
    print("\n❌ CONNECTION ERROR", e)
