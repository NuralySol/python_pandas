
#! import reqests module
import requests

#! Define the URL of the Cat Facts API and get it
cat_facts_url = "https://catfact.ninja/fact"

# Function to get get_cat_fact(): {requests} - global function of 'requests module'!
def get_cat_fact():
    response = requests.get(cat_facts_url)
    
    if response.status_code == 200:
        fact_data = response.json()  
        return fact_data.get("fact")  
    else:
        return "Failed to retrieve a cat fact. Please try again later."

if __name__ == "__main__":
    cat_fact = get_cat_fact()
    print(f"Random Cat Fact: {cat_fact}")
    
	# Purpose: The above block of code will only run if the script is executed directly,
    # not when imported as a module.
	# Why Use It?: It allows your Python file to act both as a reusable module (when imported) and as a standalone script (when run directly).