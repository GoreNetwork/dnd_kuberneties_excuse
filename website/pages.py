from flask import Flask, render_template, render_template_string
from calls_to_api import pull_new_town
import yaml
import time

app = Flask(__name__)


@app.route("/")
def index():
    yml_data = {}
    town_data = pull_new_town()
    town_name = town_data["town_name"]
    town_data["town_name"] = {"town_name": town_data["town_name"]}
    for key, value in town_data.items():
        if key != "town_name":
            yml_data[key] = yaml.dump({key: value}, default_flow_style=False)
    return render_template("town_build.html", town_data=yml_data, town_name=town_name)


@app.route("/dnd")
def dnd_page():
    return index()


@app.route("/test")
def test():
    town_name = "Your Town Name"  # Replace with your town name
    town_data = {
        # Your other town data here...
    }

    random_npc = [
        {
            "race": "dwarf",
            "gender": "female",
            "first_name": "Thorina",
            "last_name": "Silveraxe",
            "motivation": "Driven by the desire to avoid a perceived threat or danger.",
        },
        {
            "race": "dragonborn",
            "gender": "male",
            "first_name": "Bharash",
            "last_name": "Yarjerit",
            "motivation": "Concerned with what they will leave behind, whether it's an heir, a body of work, or a changed world.",
        },
        {
            "race": "dwarf",
            "gender": "male",
            "first_name": "Thorin",
            "last_name": "Deepdelver",
            "motivation": "Acting out of love, whether it's romantic, familial, or platonic, or being driven by a passion for a particular craft or cause.",
        },
        {
            "race": "dragonborn",
            "gender": "female",
            "first_name": "Kava",
            "last_name": "Verthisathurgiesh",
            "motivation": "Motivated by spiritual beliefs or in service to a deity or religious order.",
        },
        {
            "race": "dwarf",
            "gender": "female",
            "first_name": "Filiel",
            "last_name": "Stronghammer",
            "motivation": "Struggling against harsh living conditions, dangerous wildlife, or scarcity of resources.",
        },
    ]

    # Convert the dictionary to YAML format
    yaml_data = yaml.dump({"random_npc": random_npc}, default_flow_style=False)

    return render_template(
        "test.html", town_name=town_name, town_data=town_data, yaml_data=yaml_data
    )


if __name__ == "__main__":
    time.sleep(16)
    app.run(host="0.0.0.0", port=5000, debug=True)
