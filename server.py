import http.server
import socketserver
import webbrowser
from pathlib import Path

# Configuração do servidor
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Inicia o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    print("Pressione Ctrl+C para encerrar o servidor")
    
    # Abre o navegador automaticamente
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Mantém o servidor rodando
    httpd.serve_forever()
