with open("app.log", "r") as file, open("errors.log", "w") as outfile:
    for line in file:
        if "ERROR" in line:
            outfile.write(line)

