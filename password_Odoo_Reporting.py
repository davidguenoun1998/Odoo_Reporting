import streamlit as st
import webbrowser
import hmac
import hashlib

# Configuration de la page
st.set_page_config(
    page_title="Accès Document Sécurisé",
    page_icon="🔒",
    layout="centered"
)

# URL du document Odoo à protéger
DOCUMENT_URL = "https://erp.viadialog.com/document/share/35/9301d290-9306-4ba7-97ee-764e06d172bd"

# Mot de passe défini
# Idéalement, utilisez une méthode plus sécurisée en production
CORRECT_PASSWORD_HASH = hashlib.sha256("Pereire152".encode()).hexdigest()

def verify_password(input_password):
    """Vérifie si le mot de passe saisi est correct en utilisant une comparaison sécurisée"""
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return hmac.compare_digest(input_hash, CORRECT_PASSWORD_HASH)

def main():
    # Titre et explication
    st.title("Accès Document Sécurisé")
    st.write("Veuillez saisir le mot de passe pour accéder au document.")
    
    # Zone de saisie du mot de passe
    password = st.text_input("Mot de passe", type="password")
    
    # Bouton de connexion
    if st.button("Accéder au document"):
        if password:
            if verify_password(password):
                st.success("Mot de passe correct ! Redirection vers le document...")
                
                # Option 1: Rediriger via JavaScript
                js_code = f"""
                <script>
                    window.open("{DOCUMENT_URL}", "_blank").focus();
                </script>
                """
                st.components.v1.html(js_code, height=0)
                
                # Option 2: Afficher un lien direct
                st.markdown(f"[Cliquez ici si la redirection automatique ne fonctionne pas]({DOCUMENT_URL})")
                
            else:
                st.error("Mot de passe incorrect. Veuillez réessayer.")
        else:
            st.warning("Veuillez saisir un mot de passe.")
    
    # Pied de page
    st.markdown("---")
    st.markdown("Document sécurisé par ViaDialog")

if __name__ == "__main__":
    main()