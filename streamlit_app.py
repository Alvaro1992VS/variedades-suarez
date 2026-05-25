import streamlit as st

# 1. ESTO QUITA LOS MENÚS EXTRAÑOS Y DEJA LA WEB LIMPIA PARA LOS CLIENTES
st.set_page_config(page_title="Variedades Suárez", page_icon="🛒", layout="centered")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 Variedades Suárez")
st.write("Haz tu encargo fácilmente y recíbelo en la puerta de tu casa.")

# 2. AQUÍ CONTROLAS TUS PRODUCTOS (Nombre, Precio, y el nombre de la foto que subiste)
productos = {
    "Arroz (1 Libra)": {"precio": 120, "foto": "arroz.jpg"},
    "Aceite de Cocina (1L)": {"precio": 850, "foto": "aceite.webp"},
    "Jabón de Baño": {"precio": 90, "foto": "jabon.png"},
    # ¡Aquí puedes seguir agregando los 20 productos hacia abajo siguiendo el mismo formato!
}

# Carrito de compras en la sesión
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

# Mostrar productos en pantalla
st.subheader("🛍️ Nuestros Productos disponibles")

for prod, info in productos.items():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Intenta cargar la foto desde GitHub, si no la encuentra no rompe la página
        try:
            st.image(info["foto"], width=120)
        except:
            st.caption("📸 (Sin foto)")
            
    with col2:
        st.write(f"**{prod}**")
        st.write(f"Precio: ${info['precio']} C选题") # Cambia aquí a tu moneda local si no es pesos
        
        # Botón para añadir
        if st.button(f"Añadir", key=prod):
            st.session_state.carrito[prod] = st.session_state.carrito.get(prod, 0) + 1
            st.success(f"Agregado: {prod}")

# Formulario de pedido obligatorio
st.subheader("📝 Datos de Entrega")
nombre = st.text_input("Nombre Completo:")
direccion = st.text_input("Dirección de entrega:")
ci = st.text_input("Carnet de Identidad (CI):")

# Botón para enviar por WhatsApp
if st.button("🟢 ENVIAR PEDIDO POR WHATSAPP"):
    if not nombre or not direccion or not ci:
        st.error("⚠️ Por favor, rellena todos tus datos antes de enviar.")
    elif not st.session_state.carrito:
        st.error("⚠️ El carrito está vacío. Añade algún producto.")
    else:
        # Construir el mensaje de texto
        texto_pedido = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n"
        texto_pedido += f"👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n\n"
        texto_pedido += "📦 *Productos:* \n"
        
        total = 0
        for item, cant in st.session_state.carrito.items():
            subtotal = cant * productos[item]["precio"]
            total += subtotal
            texto_pedido += f"- {cant}x {item} (${subtotal})\n"
            
        texto_pedido += f"\n💰 *Total a pagar:* ${total}"
        
        # Crear enlace de WhatsApp (Reemplaza el 521234567890 por TU número con código de país)
        numero_telefono = "521234567890" 
        enlace_ws = f"https://wa.me/{numero_telefono}?text={encodeURIComponent(texto_pedido)}"
        
        st.markdown(f'<a href="{enlace_ws}" target="_blank" style="text-decoration:none;"><button style="background-color:#25D366;color:white;padding:10px;border:none;border-radius:5px;width:100%;font-weight:bold;cursor:pointer;">👉 HACER CLIC AQUÍ PARA CONFIRMAR EN WHATSAPP</button></a>', unsafe_allow_html=True)
