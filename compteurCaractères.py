# Bibliotheque pour récupérer les arguments du programme
import sys
from functions import *

AVAILABLES_EXTENSIONS = {"pdf" : pdf_count, "csv" : csv_count, "txt" : txt_count, "docx" : docx_count, "pptx" : pptx_count, "ppt" : pptx_count}

def is_file(path):
    try:
        with open(path, "r") as file:
            return True
    except FileNotFoundError:
        return False

def print_results(results):
    for result in results:
        print(f"{result[0]}: {result[1]}")

def main(argv):
    if len(argv) != 2:
        print("Veuillez indiquer le chemin du fichier à analyser ou écrire votre texte entre guillemets")
        return

    path = argv[1]
    extension = path.split(".")[-1]

    if not is_file(path):
        results = text_count(path)
    elif extension.lower() not in AVAILABLES_EXTENSIONS.keys():
        print("Nous ne sommes pas encore mesure de traiter ce type de fichier")
        return False
    else:
        results = AVAILABLES_EXTENSIONS[extension.lower()](path)

    print_results(results)
    return True

if __name__ == "__main__":
    main(sys.argv)
