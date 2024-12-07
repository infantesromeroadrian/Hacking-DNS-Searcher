class ReportGenerator:
    @staticmethod
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