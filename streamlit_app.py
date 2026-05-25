import streamlit as st

st.set_page_config(page_title="Variedades Suárez")

st.title("Variedades Suárez")
st.subheader("Haz tu encargo de productos y yo se lo llevo hasta la puerta de tu casa")

# Lista de tus productos actuales con sus precios y nombres de fotos
productos = {
    "Arroz (Lb)": {"precio": 120, "foto": "Arroz.jpg"},
    "Aceite de Cocina (1L)": {"precio": 850, "foto": "Aceite.jpg"},
    "Azucar(lb)": {"precio": 350, "foto": "Azucar.jpg"},
    "Frijoles(lb)": {"precio": 400, "foto": "Frijolrs.jpg"},
    "Pan(Unidades)": {"precio": 50, "foto": "Pan.jpg"},
    # Sigue agregando más productos aquí abajo manteniendo este mismo formato
}

# Aquí guardaremos lo que elija el cliente en esta pestaña
encargo = {}

st.write("### Productos Disponibles")

# Mostrar productos con sus fotos y botones de más y menos
for prod, info in productos.items():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Intenta cargar la foto desde GitHub
        try:
            st.image(info["foto"], width=100)
        except:
            st.caption("📸 (Sin foto)")
            
    with col2:
        st.write(f"{prod} - Precio: ${info['precio']}")
        # Botones de más/menos integrados (mínimo 0, máximo 100, avanza de 1 en 1)
        cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=prod)
        if cantidad > 0:
            encargo[prod] = cantidad

# Datos del cliente
st.write("### Datos de entrega")
nombre = st.text_input("Nombre:")
direccion = st.text_input("Dirección:")
ci = st.text_input("Carnet de Identidad (CI):")

# Botón de envío directo por WhatsApp
if st.button("Enviar encargo por WhatsApp"):
    if nombre and direccion and ci and encargo:
        texto = f"Hola, soy {nombre}.\nMi dirección es: {direccion}\nMi CI es: {ci}\n\nEste es mi encargo:\n"
        total = 0
        for item, cant in encargo.items():
            subtotal = cant * productos[item]["precio"]
            total += subtotal
            texto += f"- {cant}x {item} (${subtotal})\n"
        texto += f"\n*Total a pagar: ${total}*"
        
        # ⚠️ PON AQUÍ TU NÚMERO DE TELÉFONO REAL (ejemplo: "52123456789")
        mi_numero = "5351233908"
        
        # Codificar los espacios y saltos de línea para WhatsApp
        texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
        enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
        
        st.markdown(f'[👉 Haz clic aquí para enviar el pedido por WhatsApp]({enlace})')
    else:
        st.error("Por favor, llena tus datos y selecciona al menos 1 producto usando los botones de más (+).")
