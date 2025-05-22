import pandas as pd
import argparse as args

parser = args.ArgumentParser()
parser.add_argument("--input", type = str, required = True, help = 'Path to input file')
parser.add_argument('--format', type = str, required = True, choices = ["csv", "json", "xlsx"], help = 'Format of output File' )
arguments = parser.parse_args()

df = pd.read_csv(arguments.input)

if arguments.format == 'csv':
    df.to_csv("output/output_session_3.csv")

elif arguments.format == 'json':
   df.to_json("output/output_session_3.json")

else:
    df.to_excel("output/output_session_3.xlsx")

print("saved succesfully")

