import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Importar filtros individuais
from filters.grey_scale import apply_grayscale
from filters.invert_color import apply_invert
from filters.high_contrast import apply_contrast
from filters.blur import apply_blur
from filters.sharpen import apply_sharpen
from filters.border_detection import apply_edge

st.set_page_config(page_title="Visualizador de Imagens", layout="wide")
st.title("Atividade Visualizador de Imagens")

# Função para ajustar intensidades dos canais RGB
def adjust_channels(img: np.ndarray, r: float, g: float, b: float) -> np.ndarray:
    b_ch, g_ch, r_ch = cv2.split(img)
    r_ch = cv2.convertScaleAbs(r_ch * r)
    g_ch = cv2.convertScaleAbs(g_ch * g)
    b_ch = cv2.convertScaleAbs(b_ch * b)
    return cv2.merge([b_ch, g_ch, r_ch])

# Sidebar: upload, ajustes e filtros
def sidebar_controls():
    with st.sidebar:
        st.header("Carregue sua imagem")
        uploaded = st.file_uploader("Escolha um arquivo", type=["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"])
        if not uploaded:
            st.info("Faça upload de uma imagem para começar.")
            return None, None

        img = Image.open(uploaded).convert("RGB")
        img_np = np.array(img)[:, :, ::-1]  # RGB -> BGR

        # Ajuste de canais RGB
        st.subheader("Ajuste de canais RGB")
        red = st.slider("Vermelho", 0.0, 2.0, 1.0, key="red_ch")
        green = st.slider("Verde", 0.0, 2.0, 1.0, key="green_ch")
        blue = st.slider("Azul", 0.0, 2.0, 1.0, key="blue_ch")
        processed = adjust_channels(img_np, red, green, blue)

        # Filtros adicionais
        st.subheader("Filtros Adicionais")
        filtros = [
            "Escala de cinza", "Inversão de cores",
            "Aumento de contraste", "Blur", "Sharpen", "Detecção de borda"
        ]
        selected = st.multiselect("Escolha filtros (aplicação em ordem)", filtros)

        # Parâmetros específicos para cada filtro
        if "Escala de cinza" in selected:
            gray_intensity = st.slider(
                "Intensidade do filtro cinza", 0.0, 1.0, 1.0, key="gray_intensity"
            )
        if "Inversão de cores" in selected:
            color_inversion_factor = st.slider(
                "Fator de inversão de cores", 0.0, 3.0, 1.0, key="color_inversion"
            )
        if "Aumento de contraste" in selected:
            contrast_factor = st.slider(
                "Fator de contraste", 1.0, 3.0, 1.5, key="contrast_factor"
            )
        if "Blur" in selected:
            blur_kernel = st.slider(
                "Kernel Blur (ímpares)", 1, 51, 25, step=2, key="blur_ksize"
            )
        if "Sharpen" in selected:
            ksize = st.slider(
                "Kernel Sharpen (ímpares)", 1, 51, 25,step=2, key="sharpen_ksize"
            )
            strength = st.slider(
                "Sharpen Intensidade", 0.0, 5.0, 1.0, key="sharpen_strength"
            )
        if "Detecção de borda" in selected:    
            border_ksize = st.slider(
                "Kernel Border (ímpares)", 3, 7, 3, step=2, key="border_ksize"
            )
            
            
        # Aplicar filtros na ordem selecionada
        for filtro in selected:
            if filtro == "Escala de cinza":
                processed = apply_grayscale(processed, gray_intensity)
            elif filtro == "Inversão de cores":
                processed = apply_invert(processed, color_inversion_factor)
            elif filtro == "Aumento de contraste":
                processed = apply_contrast(processed, contrast_factor)
            elif filtro == "Blur":
                processed = apply_blur(processed, blur_kernel)
            elif filtro == "Sharpen":
                processed = apply_sharpen(processed, strength, ksize)
            elif filtro == "Detecção de borda":
                processed = apply_edge(processed, border_ksize)

    return img_np, processed

# Função principal
def main():
    orig, proc = sidebar_controls()
    if orig is None:
        st.stop()

    # Converter BGR -> RGB para exibição
    original = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    filtered = cv2.cvtColor(proc, cv2.COLOR_BGR2RGB)

    # Exibir lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original")
        st.image(original, use_container_width=True)
    with col2:
        st.subheader("Processada")
        st.image(filtered, use_container_width=True)

    # Botão de download
    buffer = BytesIO()
    Image.fromarray(filtered).save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button(
        label="Download Imagem Processada",
        data=buffer,
        file_name="imagem_processada.png",
        mime="image/png"
    )

if __name__ == "__main__":
    main()
