# Portinelly Tour - Site de Links

Este é um site estilo linktree personalizado para a Portinelly Tour, uma agência de turismo especializada em passeios de barco, buggy, paramotor e outras aventuras em praias paradisíacas.

## Características

- Design colorido e divertido inspirado no logo da Portinelly Tour
- Animações e efeitos visuais para uma experiência mais envolvente
- Elementos decorativos temáticos de praia (ondas, palmeiras, sol)
- Links para os diferentes serviços oferecidos
- Botões para redes sociais e contato direto via WhatsApp
- Layout totalmente responsivo para dispositivos móveis e desktop
- Efeitos de hover e animações nos cards

## Estrutura do Projeto

```
portinelly-tour/
│
├── index.html          # Estrutura principal do site
├── styles.css          # Estilos e animações
├── server.py           # Servidor Python para visualização local
├── netlify.toml        # Configuração para deploy no Netlify
│
└── images/
    └── portinelly-logo.png  # Logo da Portinelly Tour
```

## Como Visualizar Localmente

1. Certifique-se de ter o Python instalado em seu computador
2. Navegue até a pasta do projeto no terminal
3. Execute o servidor Python com o comando:
   ```
   python server.py
   ```
4. O navegador abrirá automaticamente com o site

## Personalização

### Alterando Links

Para alterar os links dos botões, edite os atributos `href` nas tags `<a>` no arquivo `index.html`. Por exemplo:

```html
<a href="https://wa.me/5521SEUNUMERO" class="link-card whatsapp" target="_blank">
```

### Alterando Cores

As cores principais do site estão definidas como variáveis CSS no início do arquivo `styles.css`:

```css
:root {
    --primary-color: #FF8C00;    /* Laranja vibrante */
    --secondary-color: #00CED1;  /* Azul turquesa */
    --accent-color-1: #FFD700;   /* Amarelo dourado */
    --accent-color-2: #32CD32;   /* Verde limão */
    --accent-color-3: #FF1493;   /* Rosa quente */
    --accent-color-4: #4169E1;   /* Azul royal */
    /* ... */
}
```

## Deploy no Netlify

Para implantar este site no Netlify:

1. Crie uma conta no [Netlify](https://www.netlify.com/) (se ainda não tiver)
2. Arraste e solte a pasta do projeto na área de upload do Netlify
3. Ou conecte ao GitHub se o projeto estiver em um repositório

O arquivo `netlify.toml` já está configurado para garantir que o site seja implantado corretamente.

## Importante

Antes de usar o site em produção:

1. Substitua o arquivo placeholder `portinelly-logo.png.txt` pela imagem real do logo
2. Atualize os links para as redes sociais e WhatsApp com os endereços corretos
3. Personalize os textos e descrições conforme necessário
