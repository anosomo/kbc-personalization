import streamlit as st
import json
import os
from dotenv import load_dotenv
from google import genai

# ============================================================
# Clé API
# ============================================================
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ============================================================
# Config
# ============================================================
st.set_page_config(
    page_title="Personnalisation Client",
    page_icon="🏦",
    layout="centered"
)

# ============================================================
# CSS
# ============================================================
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .stApp {
        background: linear-gradient(160deg, #000A1F 0%, #001A4D 40%, #0033A0 100%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    .header {
        padding: 8px 0 36px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header-title { color: white; font-size: 22px; font-weight: 600; }
    .header-tag {
        color: rgba(255,255,255,0.5); font-size: 12px;
        letter-spacing: 1px; text-transform: uppercase;
    }
    .section-title { font-size: 22px; font-weight: 600; color: white; margin-bottom: 6px; }
    .section-subtitle { font-size: 14px; color: rgba(255,255,255,0.6); margin-bottom: 26px; }

    .tag {
        display: inline-block;
        background: rgba(59,130,246,0.2);
        color: #93C5FD;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 500;
        margin: 3px 3px 3px 0;
        border: 1px solid rgba(59,130,246,0.35);
    }

    .reco-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.04) 100%);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 34px 38px;
        margin-top: 26px;
        backdrop-filter: blur(14px);
        box-shadow:
            0 20px 50px rgba(0,0,0,0.55),
            0 4px 12px rgba(0,0,0,0.3),
            inset 0 1px 0 rgba(255,255,255,0.18),
            inset 0 -2px 4px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    .reco-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #3B82F6 0%, #60A5FA 50%, #3B82F6 100%);
    }
    .reco-label {
        display: inline-block;
        background: rgba(59,130,246,0.25);
        color: #93C5FD;
        font-size: 10px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 16px;
        border: 1px solid rgba(59,130,246,0.4);
    }
    .reco-title { font-size: 24px; font-weight: 700; color: white; margin: 0 0 14px 0; }
    .reco-message {
        font-size: 15px; color: rgba(255,255,255,0.85);
        line-height: 1.7; margin-bottom: 22px;
    }
    .reco-besoin {
        font-size: 13px; color: rgba(255,255,255,0.75);
        margin-bottom: 22px; padding: 12px 16px;
        background: rgba(0,0,0,0.25);
        border-radius: 8px;
        border-left: 3px solid #3B82F6;
        line-height: 1.7;
    }
    .reco-besoin b { color: white; }

    .cta {
        display: inline-block;
        background: linear-gradient(145deg, #3B82F6 0%, #2563EB 100%);
        color: white !important;
        padding: 13px 30px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s;
        box-shadow: 0 6px 16px rgba(59,130,246,0.4), inset 0 1px 0 rgba(255,255,255,0.25);
    }
    .cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(59,130,246,0.55);
        color: white !important;
    }

    .footer {
        text-align: center;
        color: rgba(255,255,255,0.3);
        font-size: 12px;
        padding: 30px 0 10px 0;
        border-top: 1px solid rgba(255,255,255,0.08);
        margin-top: 70px;
    }

    .stButton > button {
        background: linear-gradient(145deg, #3B82F6 0%, #2563EB 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 14px 24px;
        font-weight: 600;
        font-size: 15px;
        width: 100%;
        transition: all 0.2s;
        box-shadow: 0 6px 16px rgba(59,130,246,0.35);
    }
    .stButton > button:hover {
        background: linear-gradient(145deg, #4A8FF7 0%, #2E6FED 100%);
        color: white;
        transform: translateY(-2px);
    }

    .loader-box {
        background: linear-gradient(145deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.03) 100%);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 30px;
        text-align: center;
        color: rgba(255,255,255,0.85);
        font-size: 15px;
        margin-top: 20px;
    }

    .stTextArea label { color: rgba(255,255,255,0.7) !important; }
    .stTextArea textarea {
        background: rgba(255,255,255,0.95) !important;
        border-radius: 10px !important;
        border: none !important;
        font-size: 14px !important;
        color: #111 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Header
# ============================================================
st.markdown("""
<div class="header">
    <div class="header-title">Personnalisation Client</div>
    <div class="header-tag">Démo Tectonic</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Chargement produits
# ============================================================
with open('produits_kbc.json', 'r', encoding='utf-8') as f:
    produits = json.load(f)

# ============================================================
# Entrée libre
# ============================================================
st.markdown('<div class="section-title">Message client</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Collez un email, un chat ou n\'importe quel texte. L\'IA analyse et recommande.</div>', unsafe_allow_html=True)

message_client = st.text_area(
    "Message",
    height=220,
    placeholder="Collez ici n'importe quelle donnée client (email, chat, note, etc.)...",
    label_visibility="collapsed"
)

# ============================================================
# Analyse IA
# ============================================================
if st.button("Analyser avec l'IA"):

    if not message_client.strip():
        st.warning("Veuillez saisir un message.")
    else:
        prompt = f"""
Tu es un conseiller bancaire empathique et professionnel.

Voici une donnée client brute :
---
{message_client}
---

Liste EXHAUSTIVE des produits KBC disponibles :
{json.dumps(produits, ensure_ascii=False, indent=2)}

Règles de sélection (TRÈS IMPORTANT) :
- Achat immobilier / maison / appartement / hypothèque → "KBC Crédit hypothécaire"
- Projet personnel / voyage / voiture sans crédit auto spécifique → "KBC Prêt personnel"
- Revenus irréguliers / freelance / trésorerie → "KBC Flex Budget"
- Naissance / bébé / enfant → "KBC-Start2Save (épargne enfant)"
- Premier salaire / commencer à épargner → "KBC-Start2Save (épargne automatique)"
- Retraite / pension / 50 ans et plus → "KBC Home & Pension Plan"
- Famille / enfants / protection → "Assurance familiale KBC"
- Logement / habitation / incendie → "KBC Assurance habitation"
- Voiture / véhicule → "KBC Assurance auto"
- Investir / placements / bourse → "KBC Invest (fonds et actions)"
- Compte quotidien / opérations → "KBC Compte à vue / compte courant"
- App / mobile / numérique → "KBC Mobile"

Choisis LE produit le PLUS PERTINENT selon ces règles. Si le client parle d'achat immobilier, tu DOIS proposer "KBC Crédit hypothécaire", même si ce n'est pas explicitement dans la liste.

Analyse cette donnée et renvoie STRICTEMENT ce JSON :
{{
  "profil": "description du client (âge estimé, situation)",
  "signaux": ["signaux", "détectés"],
  "besoin": "besoin principal en 1 phrase",
  "produit": "nom EXACT du produit choisi dans la liste",
  "message": "réponse personnalisée de 2 phrases, chaleureuse et concrète",
  "url": "URL exacte du produit choisi"
}}

N'ajoute aucun autre texte avant ou après le JSON.
"""

        placeholder = st.empty()
        placeholder.markdown("""
        <div class="loader-box">
            Analyse en cours<span class="dots"></span>
        </div>
        <style>
            .dots::after { content: ''; animation: dots 1.4s infinite; }
            @keyframes dots {
                0%, 20% { content: ''; }
                40% { content: '.'; }
                60% { content: '..'; }
                80%, 100% { content: '...'; }
            }
        </style>
        """, unsafe_allow_html=True)

        data = None
        for modele in ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.6-flash",
                       "gemini-3.5-flash", "gemini-flash-latest"]:
            try:
                r = client.models.generate_content(model=modele, contents=prompt)
                t = r.text.strip()
                if t.startswith("```"):
                    t = t.split("```")[1]
                    if t.startswith("json"):
                        t = t[4:]
                    t = t.strip()
                data = json.loads(t)
                break
            except:
                continue

        placeholder.empty()

        if data:
            signaux = "".join([f'<span class="tag">{s}</span>' for s in data.get('signaux', [])])
            st.markdown(f"""
            <div class="reco-card">
                <span class="reco-label">Recommandation IA</span>
                <h2 class="reco-title">{data.get('produit', 'N/A')}</h2>
                <p class="reco-message">{data.get('message', '')}</p>
                <div class="reco-besoin">
                    <b>Profil détecté :</b> {data.get('profil', 'N/A')}<br><br>
                    <b>Besoin identifié :</b> {data.get('besoin', 'N/A')}<br><br>
                    <b>Signaux :</b><br>{signaux}
                </div>
                <a href="{data.get('url','https://www.kbc.be/particuliers/fr.html')}" 
                   target="_blank" class="cta">
                    En savoir plus
                </a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Aucun modèle n'a répondu. Veuillez réessayer.")

# ============================================================
# Footer
# ============================================================
st.markdown("""
<div class="footer">
    Démonstration Tectonic Hackathon · Aucune donnée réelle utilisée
</div>
""", unsafe_allow_html=True)