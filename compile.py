import requests
import os

def compile_texlive(tex_file_path, style_files=[], output_dir='./'):
    # URL de l'API texlive.net
    url = "https://texlive.net/compile"

    # Lis le fichier .tex
    with open(tex_file_path, 'r') as tex_file:
        tex_content = tex_file.read()

    # Prépare le payload
    files = {
        'file': (os.path.basename(tex_file_path), tex_content)
    }

    # Ajoute les fichiers .sty s'il y en a
    for sty_file in style_files:
        with open(sty_file, 'r') as f:
            sty_content = f.read()
        files[os.path.basename(sty_file)] = (os.path.basename(sty_file), sty_content)

    # Envoi de la requête POST pour compiler le fichier .tex
    response = requests.post(url, files=files)

    if response.status_code == 200:
        # Le serveur renvoie un lien pour télécharger le PDF
        pdf_url = response.json().get('pdf_url')
        return pdf_url
    else:
        print("Erreur lors de la compilation : ", response.status_code)
        return None

# Exemple d'utilisation
tex_file = './chapitre-0-example/main.tex'
style_files = ['./style/main.sty']

pdf_url = compile_texlive(tex_file, style_files)

if pdf_url:
    print(f"Le PDF est disponible ici : {pdf_url}")
else:
    print("La compilation a échoué.")
