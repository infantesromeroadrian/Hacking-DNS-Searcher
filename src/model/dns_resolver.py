
import dns.resolver

class DNSResolver:
    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Servidores DNS de Google
        self.resolver.timeout = 10  # Tiempo de espera por consulta (segundos)
        self.resolver.lifetime = 20  # Tiempo total de espera (segundos)

    def resolve_specific_records(self, domain, record_type):
        """Consulta registros DNS específicos."""
        try:
            answers = self.resolver.resolve(domain, record_type)
            return [str(rdata) for rdata in answers]
        except dns.resolver.LifetimeTimeout:
            return [f"Error: Tiempo de espera excedido al consultar {record_type} para {domain}."]
        except Exception as e:
            return [f"Error al consultar {record_type} para {domain}: {str(e)}"]

    def resolve_all_records(self, domain):
        """Consulta todos los registros comunes para un dominio."""
        record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        results = {}
        for record_type in record_types:
            results[record_type] = self.resolve_specific_records(domain, record_type)
        return results