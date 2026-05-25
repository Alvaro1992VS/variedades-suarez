import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺")

# --- INTERFAZ: COLOR DE FONDO ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f9;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧺 Variedades Suárez")

# Muestra la foto de portada
try:
    st.image("Arroz.jpg", use_container_width=True)
except:
    pass

st.subheader("Haz tu encargo de productos y yo se lo llevo hasta su casa")

# --- LISTA DE PRODUCTOS CON CATEGORÍAS ---
productos = {
    "Arroz (Lb)": {
        "precio": 120, 
        "foto": "Arroz.jpg", 
        "detalle": "Arroz blanco de grano entero de primera calidad.",
        "categoria": "Granos"
    },
    "Aceite de Cocina (1L)": {
        "precio": 850, 
        "foto": "Aceite.jpg", 
        "detalle": "Aceite vegetal ideal para freír y cocinar.",
        "categoria": "Otros"
    },
    "Azucar(lb)": {
        "precio": 350, 
        "foto": "Azucar.jpg", 
        "detalle": "Azúcar blanca refinada bien dulce.",
        "categoria": "Otros"
    },
    "Frijoles(lb)": {
        "precio": 400, 
        "foto": "Frijolrs.jpg", 
        "detalle": "Frijoles negros nuevos, blanditos al cocinar.",
        "categoria": "Granos"
    },
    "Pan(Unidades)": {
        "precio": 50, 
        "foto": "Pan.jpg", 
        "detalle": "Pan suave horneado fresco del día.",
        "categoria": "Otros"
    }
}

# Aquí guardaremos lo que elija el cliente en la pantalla actual
encargo = {}

st.write("### 🛍️ Productos Disponibles")

# --- FILTROS DE INTERFAZ (LUPA Y CATEGORÍAS) ---
buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

categoria_seleccionada = st.selectbox(
    "📂 Selecciona una sección para filtrar:",
    ["Todo", "Granos", "Bebidas", "Pastas", "Otros"]
)

st.write("---")

# --- MOSTRAR PRODUCTOS EN PANTALLA ---
for prod, info in productos.items():
    if buscar and buscar.lower() not in prod.lower():
        continue
        
    if categoria_seleccionada != "Todo" and info["categoria"] != categoria_seleccionada:
        continue
        
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            st.image(info["foto"], width=100)
        except:
            st.caption("📸 (Sin foto)")
            
    with col2:
        st.write(f"**{prod}**")
        st.write(f"Precio: ${info['precio']}")
        st.caption(info["detalle"]) 
        
        cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"cant_{prod}")
        if cantidad > 0:
            encargo[prod] = cantidad
            
    st.divider()


# --- SECCIÓN DEL CARRITO DE COMPRAS ---
st.write("## 🛒 Tu Carrito de Compras")

if not encargo:
    st.info("Tu carrito está vacío. Incrementa las cantidades arriba con el botón de más (+) para empezar a armar tu pedido.")
else:
    total_carrito = 0
    for item, cant in encargo.items():
        subtotal = cant * productos[item]["precio"]
        total_carrito += subtotal
        st.write(f"🔹 **{cant}x** {item} — ${subtotal}")
    
    st.write(f"### 💰 Total acumulado: ${total_carrito}")
    st.write("---")
    
    # Casilla para activar los datos de entrega
    confirmar = st.checkbox("⚙️ Presiona aquí para continuar con la compra y poner tus datos")
    
    if confirmar:
        st.write("## 📝 Información de Entrega")
        nombre = st.text_input("Nombre y Apellidos:")
        direccion = st.text_input("Dirección de entrega:")
        ci = st.text_input("Carnet de Identidad (CI):")
        
        if nombre and direccion and ci:
            # Creamos el texto del pedido en tiempo real
            texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n\n📦 *Productos:* \n"
            for item, cant in encargo.items():
                subtotal = cant * productos[item]["precio"]
                texto += f"- {cant}x {item} (${subtotal})\n"
            texto += f"\n*Total a pagar: ${total_carrito}*"
            
            # Tu número de teléfono configurado
            mi_numero = "5351233908"
            texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
            enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
            
            # ESTE BOTÓN REEMPLAZA AL ANTERIOR PROBLEMÁTICO Y ABRE DIRECTO WHATSAPP
            st.write("---")
            st.link_button("👉 ENVIAR PEDIDO POR WHATSAPP", enlace, use_container_width=True)
        else:
            st.caption("Por favor, rellena tu nombre, dirección y CI para activar el botón de envío.")
