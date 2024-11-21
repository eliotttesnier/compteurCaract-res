# Bibliotheque pour ouvrir un PDF, un CSV, un document word, un pptx
import PyPDF2, csv, docx, pptx

def csv_count(path):
    file_name = str(path.split("/"))[1:-1].split("\\")[-1]
    nb_lines = 0
    with_spaces = 0
    without_spaces = 0
    words = 0

    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nb_lines += 1
            for cell in row:
                with_spaces += len(cell)
                without_spaces += len(cell.replace(" ", "").replace("\n", "").replace("\t", ""))
                words += len(cell.split())

    return [("Nom du fichier", file_name), ("Nombre de lignes", nb_lines), ("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]

def pdf_count(path):
    file_name = str(path.split("/"))[1:-1].split("\\")[-1]
    nb_pages = 0
    with_spaces = 0
    without_spaces = 0
    words = 0

    with open(path, "rb") as file:
        pdf = PyPDF2.PdfReader(file)
        nb_pages = len(pdf.pages)

        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            texte = page.extract_text()
            if texte:
                with_spaces += len(texte)
                without_spaces += len(texte.replace(" ", "").replace("\n", "").replace("\t", ""))
                words += len(texte.split())

    return [("Nom du fichier", file_name), ("Nombre de pages", nb_pages), ("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]

def txt_count(path):
    file_name = str(path.split("/"))[1:-1].split("\\")[-1]
    with_spaces = 0
    without_spaces = 0
    words = 0

    with open(path, "r") as file:
        text = file.read()
        with_spaces = len(text)
        without_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
        words = len(text.split())

    return [("Nom du fichier", file_name), ("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]

def docx_count(path):
    file_name = str(path.split("/"))[1:-1].split("\\")[-1]
    with_spaces = 0
    without_spaces = 0
    words = 0

    doc = docx.Document(path)
    for paragraph in doc.paragraphs:
        with_spaces += len(paragraph.text)
        without_spaces += len(paragraph.text.replace(" ", "").replace("\n", "").replace("\t", ""))
        words += len(paragraph.text.split())

    return [("Nom du fichier", file_name), ("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]

def pptx_count(path):
    file_name = str(path.split("/"))[1:-1].split("\\")[-1]
    with_spaces = 0
    without_spaces = 0
    words = 0

    ppt = pptx.Presentation(path)
    for slide in ppt.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                with_spaces += len(shape.text)
                without_spaces += len(shape.text.replace(" ", "").replace("\n", "").replace("\t", ""))
                words += len(shape.text.split())

    return [("Nom du fichier", file_name), ("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]

def text_count(text):
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    words = len(text.split())

    return [("Nombre de caractères avec espaces", with_spaces), ("Nombre de caractères sans espaces", without_spaces), ("Nombre de mots", words)]