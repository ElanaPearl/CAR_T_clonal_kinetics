import gzip
import os
import tarfile

raw_file = "GSE125881_raw.expMatrix.csv.gz"
transposed_file = "expMatrix_transposed.csv"


def transpose_csv(csv_path, output_csv_path="transposed.csv", delimiter=","):
    # code copied from: https://stackoverflow.com/questions/7156539/how-do-i-transpose-pivot-a-csv-file-with-python-without-loading-the-whole-file
    import csv

    transposed_iterator = zip(*csv.reader(open(csv_path)))
    with open(output_csv_path, "w") as out:
        for row in transposed_iterator:
            out.write(delimiter.join(row) + "\n")


print("Preparing expression matrix (unzipping and transposing)...")

if not os.path.exists(transposed_file):
    if not os.path.exists(raw_file):
        raise FileNotFoundError(f"Could not find {raw_file} in {os.getcwd()}")
    # un gzip raw_file
    with gzip.open(raw_file, "rb") as f_in:
        with open(raw_file[:-3], "wb") as f_out:
            f_out.write(f_in.read())
    os.remove(raw_file)
    raw_file = raw_file[:-3]

    transpose_csv(raw_file, transposed_file)
    os.remove(raw_file)
else:
    print(f"Found {transposed_file} in {os.getcwd()}")

print("-----------------------------------------------------------")
print("Un-tarring the TCR data")
if not os.path.exists("GSE125881_RAW"):
    if not os.path.exists("GSE_125881_RAW.tar"):
        raise FileNotFoundError(
            f"Could not find GSE_125881_RAW.tar in {os.getcwd()}"
        )
    tar = tarfile.open("GSE_125881_RAW.tar")
    tar.extractall()
    tar.close()
