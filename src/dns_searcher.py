import dns.resolver
from openai import OpenAI
import os

# Configuración de la API Key de OpenAI
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde un archivo .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configuración del resolver DNS con servidores públicos y tiempos de espera ajustados
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Servidores DNS de Google
resolver.timeout = 10  # Tiempo de espera por consulta (segundos)
resolver.lifetime = 20  # Tiempo total de espera (segundos)


def resolve_specific_records(domain, record_type):
    """Consulta registros DNS específicos."""
    try:
        answers = resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except dns.resolver.LifetimeTimeout:
        return [f"Error: Tiempo de espera excedido al consultar {record_type} para {domain}."]
    except Exception as e:
        return [f"Error al consultar {record_type} para {domain}: {str(e)}"]


def resolve_all_records(domain):
    """Consulta todos los registros comunes para un dominio."""
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    results = {}
    for record_type in record_types:
        results[record_type] = resolve_specific_records(domain, record_type)
    return results


def analyze_dns_results_with_openai(results):
    """Usa OpenAI para analizar resultados DNS y dar recomendaciones de seguridad."""
    prompt = f"Analiza estos resultados DNS y proporciona recomendaciones de seguridad:\n{results}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en seguridad DNS."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def explain_dns_term_with_openai(term):
    """Explica términos DNS utilizando OpenAI."""
    prompt = f"Explica qué es un '{term}' en términos sencillos y su importancia en la seguridad DNS."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en seguridad DNS."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def generate_dns_config_with_openai(purpose):
    """Genera configuraciones DNS óptimas con OpenAI."""
    prompt = f"Genera configuraciones DNS óptimas para el siguiente propósito: {purpose}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en configuraciones DNS."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def generate_html_report(results, filename="dns_report.html"):
    """Genera un reporte HTML con los resultados DNS."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("<html><body><h1>Reporte de Consultas DNS</h1><ul>")
        for record_type, records in results.items():
            file.write(f"<li><b>{record_type}</b>:<ul>")
            for record in records:
                file.write(f"<li>{record}</li>")
            file.write("</ul></li>")
        file.write("</ul></body></html>")
    print(f"Reporte HTML generado: {filename}")


def main():
    while True:
        print("\nOpciones disponibles:")
        print("1. Consultar registros específicos (A, MX, etc.)")
        print("2. Consultar todos los registros comunes (A, AAAA, CNAME, etc.)")
        print("3. Analizar configuraciones de seguridad y detectar vulnerabilidades")
        print("4. Generar reporte")
        print("5. Análisis con IA de OpenAI")
        print("6. Explicación de términos DNS")
        print("7. Generar configuraciones DNS óptimas")
        print("8. Salir")

        choice = input("Selecciona una opción (1-8): ")

        if choice == "1":
            domain = input("Introduce el dominio a consultar: ").strip()
            record_type = input("Introduce el tipo de registro (e.g., A, MX): ").strip()
            results = resolve_specific_records(domain, record_type)
            print(f"{record_type} registros para {domain}:")
            for result in results:
                print(f" - {result}")

        elif choice == "2":
            domain = input("Introduce el dominio a consultar: ").strip()
            results = resolve_all_records(domain)
            for record_type, records in results.items():
                print(f"{record_type} registros para {domain}:")
                for record in records:
                    print(f" - {record}")

        elif choice == "3":
            domain = input("Introduce el dominio a analizar: ").strip()
            results = resolve_all_records(domain)
            analysis = analyze_dns_results_with_openai(results)
            print(f"Análisis de seguridad:\n{analysis}")

        elif choice == "4":
            domain = input("Introduce el dominio para generar el reporte: ").strip()
            results = resolve_all_records(domain)
            filename = input(
                "Introduce el nombre del archivo HTML (por defecto 'dns_report.html'): ").strip() or "dns_report.html"
            generate_html_report(results, filename)

        elif choice == "5":
            user_query = input("Introduce tu consulta relacionada con DNS: ").strip()
            response = explain_dns_term_with_openai(user_query)
            print(f"Respuesta de OpenAI:\n{response}")

        elif choice == "6":
            term = input("Introduce el término DNS a explicar: ").strip()
            explanation = explain_dns_term_with_openai(term)
            print(f"Explicación:\n{explanation}")

        elif choice == "7":
            purpose = input("¿Cuál es el propósito de las configuraciones DNS?: ").strip()
            configuration = generate_dns_config_with_openai(purpose)
            print(f"Configuración recomendada:\n{configuration}")

        elif choice == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()