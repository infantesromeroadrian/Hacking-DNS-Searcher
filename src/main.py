from src.features.dns_analyzer import DNSAnalyzer

def main():
    analyzer = DNSAnalyzer()
    analyzer.run_cli()

if __name__ == "__main__":
    main()