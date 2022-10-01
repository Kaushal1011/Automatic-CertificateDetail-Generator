# Automatic Certificate Detail Generator
Generates certificates by filling names and project / competition name based on a data present in the CSV file.

## Usage

- Install the dependencies using `pip install -r requirements.txt`
- Run the script using `python3 main.py`
- Enter the path to the CSV file
- Enter the path to the template file (certificate)
- Enter the path of the font file to be used
- Enter the path to the output folder (optional)

To use the drawrectage.py file, run the following command:
```bash
python3 drawrectage.py --image <path to image>
```


## CSV File Format
```csv
Participant Name,Project Name (or Competition Name)
```


## More about the program
- Reads `names.csv` and `certi.png` and adds names and project title in certificate based on coordinates specified.
- The format of the .csv can be altered as per the requirements of the details.
> Read Comments in code to get clearer idea of script


## Contribute
- Fork the repository
- Clone the repository using `git clone https://github.com/<username>/Automatic-CertificateDetail-Generator.git`
- Create a new branch using `git checkout -b <branch_name>`
- Make changes and commit using `git commit -m "<commit_message>"`
- Push the changes using `git push origin <branch_name>`
- Create a pull request


