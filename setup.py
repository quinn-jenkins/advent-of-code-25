import os

def main():
    template_path = "template.py"

    # Load template contents once
    if not os.path.exists(template_path):
        print("Error: template.py not found in current directory.")
        return

    with open(template_path, "r") as f:
        template_contents = f.read()

    for i in range(1, 13):
        daystr = f"day{i:02d}"
        dirname = daystr
        pyfile = os.path.join(dirname, f"{daystr}.py")

        # Create directory if needed
        os.makedirs(dirname, exist_ok=True)

        # Create empty text files
        open(os.path.join(dirname, "ex.txt"), "w").close()
        open(os.path.join(dirname, "input.txt"), "w").close()

        # Write dayNN.py with custom header + template contents
        with open(pyfile, "w") as f:
            f.write(f'day = "{daystr}"\n\n')
            f.write(template_contents)

        print(f"Created {pyfile}")

if __name__ == "__main__":
    main()