# atividade-visualizador-imagens

Este projeto implementa um **visualizador de imagens** em Python utilizando Streamlit e OpenCV. O usuário pode carregar uma imagem, ajustar canais de cor (BGR), aplicar diversos filtros (escala de cinza, inversão de cores, contraste, blur, nitidez e detecção de bordas) e realizar transformações adicionais. Ao final, é possível baixar a imagem processada.

## Pré-requisitos

- Python 3.7 ou superior  
- Ambiente virtual (recomendado): venv, virtualenv ou similar

## Instalação

1. Clone o repositório:  

```bash
git clone https://<seu-repositório-url>/atividade-visualizador-imagens.git
cd atividade-visualizador-imagens
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Uso

Execute a aplicação Streamlit:

```bash
streamlit run interface.py
```

1. No navegador, acesse o endereço exibido (geralmente <http://localhost:8501>).

2. Na barra lateral:

- Faça o upload de uma imagem (JPEG ou PNG).

- Ajuste os canais B, G e R usando os sliders.

- Selecione um ou mais filtros na lista.

3. Ajuste parâmetros específicos de cada filtro, se disponível.

4. A imagem original e a imagem processada serão exibidas lado a lado.

5. Use o botão Download Imagem Processada para salvar o resultado.

## Estrutura do Projeto

```bash
atividade-visualizador-imagens/
├─ assets/              
│  └─ 2025-05-15 09-05-11.mp4 # Vídeo mostrando interface
├─ filters/               # Scripts de filtros individuais
│  ├─ grey_scale.py
│  ├─ invert_color.py
│  ├─ high_contrast.py
│  ├─ blur.py
│  ├─ sharpen.py
│  └─ border_detection.py
├─ interface.py           # Script principal da interface Streamlit
├─ requirements.txt       # Lista de dependências
├─ README.md              # Documentação de uso
├─ .gitignore
└─ venv/                  # Ambiente virtual
```
