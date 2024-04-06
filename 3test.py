import json

links = []

# Assuming you have a file named "link.txt" with one URL per line
with open("link.txt", "r") as file:
    links = file.readlines()
    # This removes any newline characters at the end of each line
    links = [link.strip().replace("?type=products", "") for link in links]

# Writing the list of links to a JSON file
with open("links.json", "w") as file:
    json.dump(links, file, indent=4)
