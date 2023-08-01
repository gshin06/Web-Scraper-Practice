import pip._vendor.requests
from bs4 import BeautifulSoup 

URL = "https://realpython.github.io/fake-jobs/"
page = pip._vendor.requests.get(URL)

# BeautifulSoup ---------------------------------------------------------------------
soup = BeautifulSoup(page.content, "html.parser") # Creates a bs object
results = soup.find(id="ResultsContainer") # Finds the specific HTML element by ID
# print(results.prettify) # Prints results and uses prettify to make it look nice

job_elements = results.findAll("div", class_="card-content") # Finds all elements with the class "card-content" in results
 # Each job_element is a bs object
# for job_element in job_elements: # Print all job elements
#     title_element = job_element.find("h2", class_="title") 
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     # print(title_element)
#     # print(company_element)
#     # print(location_element)
    
#     # Adding .text prints only the text
#     # print(title_element.text)
#     # print(company_element.text)
#     # print(location_element.text)

#     # Adding .strip() removes whitespace
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# python_jobs = results.findAll("h2", string="Python ") Case sensitive
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# need to go 3 levels up to see text
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Finds and prints all python jobs
# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# Gets links for all elements
for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")