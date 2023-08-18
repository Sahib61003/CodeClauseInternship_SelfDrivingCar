"""
This script contains snippets to download and extract the dataset into the dataset folder.
Use this script to setup the directory structure.

Run:
python setup.py
"""

import zipfile
import urllib.request


def download_dataset(verbose: bool = False) -> None:
    """
    Download and extract the given dataset. [cities, caltech, amazon]
    """

    URL = r"https://www.kaggle.com/datasets/andy8744/udacity-self-driving-car-behavioural-cloning/download?datasetVersionNumber=1"

    if URL is None:
        raise ValueError("Invalid dataset name.")

    filename = r"dataset.zip"  
    if verbose:
        print(f"Downloading dataset...")
        print(f"FROM: {URL}")
        print(f"INTO: {filename}")

    urllib.request.urlretrieve(URL, filename)
    if verbose:
        print(f"Downloaded dataset.")

    with zipfile.ZipFile(filename, "r") as ref:
        ref.extractall("dataset/")
        if verbose:
            print(f"Extracted dataset.")


if __name__ == "__main__":
    userinput = input("Choose [Y/N]: ")
    if userinput.casefold() == "y":
        download_dataset(verbose=True)
    else:
        print("No dataset downloaded.")