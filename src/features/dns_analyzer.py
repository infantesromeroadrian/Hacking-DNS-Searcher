from src.model.dns_resolver import DNSResolver
from src.model.openai_client import OpenAIClient
from src.utils.report_generator import ReportGenerator


class DNSAnalyzer:
    def __init__(self):
        self.dns_resolver = DNSResolver()
        self.openai_client = OpenAIClient()
        self.report_generator = ReportGenerator()

    def run_cli(self):
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
                self._handle_specific_records()
            elif choice == "2":
                self._handle_all_records()
            elif choice == "3":
                self._handle_security_analysis()
            elif choice == "4":
                self._handle_report_generation()
            elif choice == "5":
                self._handle_ai_analysis()
            elif choice == "6":
                self._handle_term_explanation()
            elif choice == "7":
                self._handle_config_generation()
            elif choice == "8":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    def _handle_specific_records(self):
        domain = input("Introduce el dominio a consultar: ").strip()
        record_type = input("Introduce el tipo de registro (e.g., A, MX): ").strip()
        results = self.dns_resolver.resolve_specific_records(domain, record_type)
        print(f"{record_type} registros para {domain}:")
        for result in results:
            print(f" - {result}")

    def _handle_all_records(self):
        domain = input("Introduce el dominio a consultar: ").strip()
        results = self.dns_resolver.resolve_all_records(domain)
        for record_type, records in results.items():
            print(f"{record_type} registros para {domain}:")
            for record in records:
                print(f" - {record}")

    def _handle_security_analysis(self):
        domain = input("Introduce el dominio a analizar: ").strip()
        results = self.dns_resolver.resolve_all_records(domain)
        analysis = self.openai_client.analyze_dns_results(results)
        print(f"Análisis de seguridad:\n{analysis}")

    def _handle_report_generation(self):
        domain = input("Introduce el dominio para generar el reporte: ").strip()
        results = self.dns_resolver.resolve_all_records(domain)
        filename = input(
            "Introduce el nombre del archivo HTML (por defecto 'dns_report.html'): ").strip() or "dns_report.html"
        self.report_generator.generate_html_report(results, filename)

    def _handle_ai_analysis(self):
        user_query = input("Introduce tu consulta relacionada con DNS: ").strip()
        response = self.openai_client.explain_dns_term(user_query)
        print(f"Respuesta de OpenAI:\n{response}")

    def _handle_term_explanation(self):
        term = input("Introduce el término DNS a explicar: ").strip()
        explanation = self.openai_client.explain_dns_term(term)
        print(f"Explicación:\n{explanation}")

    def _handle_config_generation(self):
        purpose = input("¿Cuál es el propósito de las configuraciones DNS?: ").strip()
        configuration = self.openai_client.generate_dns_config(purpose)
        print(f"Configuración recomendada:\n{configuration}")