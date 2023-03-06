import json

data = {
    "test": {
        "frequencies": [0] * 11,
        "gains": [0] * 11,
        "qs": [0] * 11
    }
}

with open("input.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    filter_params = line.split()
    if "Filter" in filter_params:
        filter_idx = int(filter_params[1].strip(":")) - 1
        fc_idx = filter_params.index("Hz") - 1
        gain_idx = filter_params.index("Gain") + 1
        q_idx = filter_params.index("Q") + 1
        data["test"]["frequencies"][filter_idx+1] = float(filter_params[fc_idx])
        data["test"]["gains"][filter_idx+1] = float(filter_params[gain_idx])
        data["test"]["qs"][filter_idx+1] = float(filter_params[q_idx])

with open("eq-script-output.json", "w") as f:
    json.dump(data, f, indent=4)
