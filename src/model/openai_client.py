import os
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_dns_results(self, results):
        """Usa OpenAI para analizar resultados DNS y dar recomendaciones de seguridad."""
        prompt = f"Analiza estos resultados DNS y proporciona recomendaciones de seguridad:\n{results}"
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en seguridad DNS."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def explain_dns_term(self, term):
        """Explica términos DNS utilizando OpenAI."""
        prompt = f"Explica qué es un '{term}' en términos sencillos y su importancia en la seguridad DNS."
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en seguridad DNS."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def generate_dns_config(self, purpose):
        """Genera configuraciones DNS óptimas con OpenAI."""
        prompt = f"Genera configuraciones DNS óptimas para el siguiente propósito: {purpose}"
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en configuraciones DNS."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content