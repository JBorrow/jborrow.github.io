import pandas as pd

data_pubs = pd.read_table("pubs/Publications-Publications.csv", delimiter=",")
data_talks = pd.read_table("pubs/Talks-Talks.csv", delimiter=",")
data_posters = pd.read_table("pubs/Posters-Posters.csv", delimiter=",")

output = "## Publications\n\n"

for item in data_pubs.iterrows():
    item = item[1]

    if item["Title"] != item["Title"]:
        continue

    output += f"+ {item['Authors']}: _{item['Title']}_, published {item['Date Published']} in {item['Journal']}. [Link]({item['Link']}).\n"

output = output.replace("Josh Borrow", "**Josh Borrow**")

output += "\n\n## Talks\n\n"

for item in data_talks.iterrows():
    item = item[1]

    if item[0] != item[0]:
        continue

    output += f"+ {item['Title']}, given {item['Date Given']} at {item['Location']}. [Slides]({item['Link']}).\n"

output += "\n\n## Posters\n\n"

for item in data_posters.iterrows():
    item = item[1]

    if item[0] != item[0]:
        continue

    output += f"+ {item['Title']}, shown {item['Date Presented']} at {item['Conference']}. [View]({item['Link']}).\n"


with open("___intro_stuff.md", "r") as f:
    text = f.read()

with open("index.md", "w") as f:
    f.write(text + output)
