# DNS Searcher Tool
Una herramienta para analizar registros DNS y obtener recomendaciones de seguridad utilizando OpenAI y Python.

## 🌟 Características
- Análisis completo de registros DNS (A, AAAA, CNAME, MX, NS, SOA, TXT)  
- Recomendaciones de seguridad mediante GPT-4
- Generación de reportes en HTML
- Consultas personalizadas mediante IA 
- Optimización de configuraciones DNS
- Interfaz de línea de comandos intuitiva

## 📋 Requisitos Previos
- Python 3.8+
- Poetry para gestión de dependencias
- API Key de OpenAI

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/dns-searcher.git
cd dns-searcher
```

2. Instalar dependencias:
```bash
poetry install
```

3. Configurar API Key de OpenAI:
```bash
poetry run dns-searcher config --api
```

4. 📁 Estructura del Proyecto
```
dns-searcher/
├── src/
│   ├── features/          # Funcionalidades principales
│   │   ├── __init__.py
│   │   └── dns_analyzer.py
│   ├── utils/            # Utilidades
│   │   ├── __init__.py
│   │   └── report_generator.py
│   ├── model/            # Modelos y configuraciones
│   │   ├── __init__.py
│   │   ├── dns_resolver.py
│   │   └── openai_client.py
│   ├── __init__.py
│   └── main.py
├── .env
├── pyproject.toml
└── README.md
```

5. 🚦 Uso
```bash
poetry shell
```

```bash
python -m src.main --domain google.com
```

## 📝 Ejemplo de Uso
```bash
Menú de opciones:

1: Consultar registros específicos
2: Analizar todos los registros DNS
3: Análisis de seguridad
4: Generar reporte HTML
5: Consulta personalizada con IA
6: Explicación de términos DNS
7: Optimizar configuraciones
8: Salir

Seleccione
```

⚙️ Configuración (pyproject.toml)
```toml
tomlCopy[tool.poetry]
name = "dns-searcher"
version = "0.1.0"
description = "Herramienta de análisis DNS con capacidades de IA"
authors = ["Tu Nombre <tu@email.com>"]

[tool.poetry.dependencies]
python = "^3.8"
dnspython = "^2.4.2"
openai = "^1.0.0"
python-dotenv = "^1.0.0"

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"
black = "^23.7.0"
isort = "^5.12.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

🤝 Contribuir
Si deseas contribuir a este proyecto, por favor lee el archivo CONTRIBUTING.md para obtener más información.


📝 Licencia
Distribuido bajo Licencia MIT. Ver LICENSE para más información.


✉️ Contacto
Adrián Infantes Romero - 
📧 Correo electrónico:
```bash
infantesromeroadrian@gmail.com
```


