import os
from pypdf import PdfReader

# ---------------------------------------------------------
# 1. TON DOSSIER (Je l'ai copié exactement)
# ---------------------------------------------------------
dossier_source = "/Users/jessicabourdouxhe/Desktop/Master 1/Data/Projet /Databases /DatabaseDataMangement - Texts"

# ---------------------------------------------------------
# 2. VÉRIFICATION DE SÉCURITÉ
# ---------------------------------------------------------
# On demande à Python : "Est-ce que ce dossier existe vraiment ?"
if not os.path.exists(dossier_source):
    print("❌ AÏE ! Python ne trouve pas le dossier.")
    print("Vérifie bien qu'il n'y a pas d'espaces en trop dans le chemin.")
    print(f"Chemin testé : {dossier_source}")
    
else:
    print(f"✅ Dossier trouvé ! Démarrage de la conversion dans : {dossier_source}\n")

    # ---------------------------------------------------------
    # 3. LA MOULINETTE (Conversion)
    # ---------------------------------------------------------
    compteur = 0
    
    # On regarde chaque fichier dans ton dossier
    for filename in os.listdir(dossier_source):
        
        # Si c'est un PDF, on l'attaque
        if filename.endswith(".pdf"):
            chemin_pdf = os.path.join(dossier_source, filename)
            
            try:
                # Lecture du PDF
                reader = PdfReader(chemin_pdf)
                text_complet = ""
                
                # On recolle toutes les pages
                for page in reader.pages:
                    # On ajoute le texte de la page + un saut de ligne
                    extracted = page.extract_text()
                    if extracted:
                        text_complet += extracted + "\n"
                
                # Création du nom du nouveau fichier .txt
                # Exemple : "2000-Democrats.pdf" devient "2000-Democrats.txt"
                nom_txt = filename.replace(".pdf", ".txt")
                chemin_txt = os.path.join(dossier_source, nom_txt)
                
                # Sauvegarde
                with open(chemin_txt, "w", encoding="utf-8") as f:
                    f.write(text_complet)
                    
                print(f"📄 Converti : {filename} -> {nom_txt}")
                compteur += 1
                
            except Exception as e:
                print(f"⚠️ Erreur sur le fichier {filename} : {e}")

    print("-" * 30)
    print(f"🎉 Terminé ! {compteur} fichiers ont été transformés en texte.")


