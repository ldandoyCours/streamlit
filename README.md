Cours YouTube — Découvrir Streamlit (Repo ldandoyCours/streamlit)

Bienvenue ! Ce dépôt contient des exemples minimaux pour présenter Streamlit pas à pas pendant une vidéo YouTube : éléments d’interface, images, graphiques, onglets, barre latérale, état de session, callbacks, etc.

🧰 Streamlit transforme un simple script Python en application web interactive en quelques minutes. Idéal pour des démos, des dashboards et des POC data/IA. 
GitHub

🚀 Démarrage rapide (local)
1) Cloner le projet
```bash
git clone https://github.com/ldandoyCours/streamlit.git
cd streamlit
```

2) Créer un venv + installer les deps
```bash
# Linux / macOS
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3) Lancer l’app de démo
```bash
streamlit run main.py
```

Ouvre ensuite le lien local (généralement http://localhost:8501).

💡 Tu peux aussi lancer un fichier spécifique (ex: graphiques) :
```bash
streamlit run chart.py
```

🐳 Option Docker (zéro install Python)

Le repo inclut un Dockerfile.
```bash
# Build

docker build -t streamlit-course .

# Run (map sur le port 8501)
docker run --rm -p 8501:8501 streamlit-course
```

🗂️ Structure du projet
```bash
streamlit/
├─ Dockerfile
├─ requirements.txt
├─ main.py              # Page d'accueil / menu des démos
├─ element.py           # Widgets & éléments de base (texte, inputs…)
├─ text.py              # Texte, titres, markdown
├─ bouton.py            # Boutons, events simples
├─ sidebar.py           # Barre latérale & organisation
├─ tabs.py              # Onglets / navigation interne
├─ image.py             # Affichage d'images
├─ chart.py             # Démo de graphiques
├─ state.py             # Gestion de st.session_state
├─ nostate.py           # Comparatif sans état
├─ callbacks.py         # Callbacks (on_change, etc.)
├─ reload.py            # Auto-reload / patterns dev
├─ complexe.py          # Exemple combiné
├─ advanced.py          # Exemples un peu plus avancés
└─ static/              # Ressources statiques (images, data…)
```

💡 Chaque fichier est lançable indépendamment :

```bash
streamlit run <nom_du_fichier>.py
```

🧪 Parcours de démo (suggestion)

- main.py : menu pour naviguer entre les exemples.
- element.py / text.py : bases de l’UI (titres, markdown, inputs).
- bouton.py : événements simples (clic bouton).
- sidebar.py : filtre en barre latérale + contenu central.
- tabs.py : organiser plusieurs vues.
- image.py : charger/afficher une image locale ou distante.
- chart.py : tracer un graphe (matplotlib/Altair/Plotly selon deps).
- state.py vs nostate.py : pourquoi et comment st.session_state.
- callbacks.py : réagir à un changement d’input proprement.
- reload.py : cycle dev rapide.
- complexe.py / advanced.py : assembler tout ça.

🧵 Scripts utiles (copier-coller à l’écran)

```bash
# Installer Streamlit (si besoin)
pip install streamlit

# Créer une app minimale
echo "import streamlit as st; st.title('Hello, Streamlit!')" > app.py
streamlit run app.py
```

🛠️ Dépannage rapide

- Port déjà utilisé (8501) → lancer avec un autre port :
```bash
streamlit run main.py --server.port 8502
```

- Police d’accès aux fichiers → placer les assets dans static/ et utiliser des chemins relatifs.

- Modules manquants → vérifier requirements.txt puis pip install -r requirements.txt.

- Lenteurs → envisager le cache (@st.cache_data, @st.cache_resource) pour les opérations coûteuses.

📚 Ressources officielles

- Repo Streamlit (code & issues) — utile pour l’actualité, exemples et best practices. 
GitHub

- Organisation Streamlit sur GitHub (exemples supplémentaires, templates de composants). 
GitHub

🙌 Auteur & licence

Auteur : Loïc Dandoy (formateur & créateur de contenu)