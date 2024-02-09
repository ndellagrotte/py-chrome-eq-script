import json
import sys

# Check if a file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 script.py <file path of input file>")
    exit()

input_file = sys.argv[1]

data = {
    "test": {
        "frequencies": [0] * 11,
        "gains": [0] * 11,
        "qs": [0] * 11
    }
}

with open(input_file, "r") as f:
    lines = f.readlines()

pk_index = 1

for i, line in enumerate(lines):
    if line.startswith("Preamp:"):
        continue

    filter_params = line.split()
    if "Filter" in filter_params:
        fc_idx = filter_params.index("Hz") - 1
        gain_idx = filter_params.index("Gain") + 1
        q_idx = filter_params.index("Q") + 1

        if "LSC" in filter_params:
            data["test"]["frequencies"][0] = float(filter_params[fc_idx])
            data["test"]["gains"][0] = float(filter_params[gain_idx])
            data["test"]["qs"][0] = float(filter_params[q_idx])
        elif "HSC" in filter_params:
            data["test"]["frequencies"][10] = float(filter_params[fc_idx])
            data["test"]["gains"][10] = float(filter_params[gain_idx])
            data["test"]["qs"][10] = float(filter_params[q_idx])
        elif "PK" in filter_params:
            if pk_index > 9:
                print("Error: Input EQ is limited to one HSC filter, one LSC filter, and 9 PK filters.")
                print("Press return to exit")
                input()
                exit()
            data["test"]["frequencies"][pk_index] = float(filter_params[fc_idx])
            data["test"]["gains"][pk_index] = float(filter_params[gain_idx])
            data["test"]["qs"][pk_index] = float(filter_params[q_idx])
            pk_index += 1

with open("eq-script-output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Success. Import `eq-script-output.json` into the Ears EQ extension and enjoy.")
print("Press return to exit")
input()
