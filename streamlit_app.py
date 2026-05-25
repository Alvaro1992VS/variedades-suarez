import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺")

# --- INTERFAZ: COLOR DE FONDO Y CATEGORÍAS HORIZONTALES MÁS GRANDES ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f9;
    }
    /* Estilo para las pestañas horizontales */
    .stTabs [data-baseweb="tab"] p {
        font-size: 18px !important;    
        font-weight: bold !important;  
        color: #111111 !important;    
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧺 Variedades Suárez")

# Muestra la foto de portada
try:
    st.image("Arroz.jpg", use_container_width=True)
except:
    pass

# --- NUEVO: FLUJO VISUAL DEL PROCESO ---
st.write("### **🛍️ Elige tus productos** ➔ **🛒 Revisa el carrito** ➔ **📝 Envía por WhatsApp**")

# --- NUEVO: TARJETAS INFORMATIVAS CON COLOR ---
st.info("🚚 **Información de Entrega:** Llevamos tu encargo directo hasta la puerta de tu casa en el pueblo de forma rápida y segura.")

st.subheader("Haz tu encargo de productos y yo se lo llevo hasta su casa")

# --- LISTA DE PRODUCTOS MEJORADA CON ETIQUETAS LLAMATIVAS ---
productos = {
    "Arroz (Lb)": {
        "precio": 120, 
        "foto": "Arroz.jpg", 
        "detalle": "Arroz blanco de grano entero de primera calidad.",
        "categoria": "Granos",
        "etiqueta": "🔥 ¡LO MÁS VENDIDO!"
    },
    "Aceite de Cocina (1L)": {
        "precio": 850, 
        "foto": "Aceite.jpg", 
        "detalle": "Aceite vegetal ideal para freír y cocinar.",
        "categoria": "Otros",
        "etiqueta": "✨ RECOMENDADO"
    },
    "Azucar(lb)": {
        "precio": 350, 
        "foto": "Azucar.jpg", 
        "detalle": "Azúcar blanca refinada bien dulce.",
        "categoria": "Otros",
        "etiqueta": ""
    },
    "Frijoles(lb)": {
        "precio": 400, 
        "foto": "Frijolrs.jpg", 
        "detalle": "Frijoles negros nuevos, blanditos al cocinar.",
        "categoria": "Granos",
        "etiqueta": "💪 CALIDAD PREMIUM"
    },
    "Pan(Unidades)": {
        "precio": 50, 
        "foto": "Pan.jpg", 
        "detalle": "Pan suave horneado fresco del día.",
        "categoria": "Otros",
        "etiqueta": "🥖 FRESCO DEL DÍA"
    }
}

# Aquí guardaremos lo que elija el cliente en la pantalla actual
encargo = {}

st.write("---")
st.write("### 🛍️ Productos Disponibles")

# --- INTERFAZ: BUSCADOR (LUPA) ---
buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

# --- INTERFAZ: CATEGORÍAS HORIZONTALES (PESTAÑAS) ---
tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
    "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
])

# Función interna corregida
def mostrar_productos(categoria_filtro=None, nombre_pestana="todo"):
    for prod, info in productos.items():
        if buscar and buscar.lower() not in prod.lower():
            continue
            
        if categoria_filtro and info["categoria"] != categoria_filtro:
            continue
            
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                st.image(info["foto"], width=100)
            except:
                st.caption("📸 (Sin foto)")
                
        with col2:
            # Muestra la etiqueta de color si tiene una asignada
            if info["etiqueta"]:
                st.warning(info["etiqueta"])
                
            st.write(f"**{prod}**")
            st.write(f"Precio: ${info['precio']}")
            st.caption(info["detalle"]) 
            
            cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"cant_{prod}_{nombre_pestana}")
            if cantidad > 0:
                encargo[prod] = cantidad
                
        st.divider()

# Colocar los productos correctos en sus pestañas
with tab_todo:
    mostrar_productos(categoria_filtro=None, nombre_pestana="todo")

with tab_granos:
    mostrar_productos(categoria_filtro="Granos", nombre_pestana="granos")

with tab_bebidas:
    mostrar_productos(categoria_filtro="Bebidas", nombre_pestana="bebidas")

with tab_pastas:
    mostrar_productos(categoria_filtro="Pastas", nombre_pestana="pastas")

with tab_otros:
    mostrar_productos(categoria_filtro="Otros", nombre_pestana="otros")


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
            # Creamos el texto del pedido
            texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n\n📦 *Productos:* \n"
            for item, cant in encargo.items():
                subtotal = cant * productos[item]["precio"]
                texto += f"- {cant}x {item} (${subtotal})\n"
            texto += f"\n*Total a pagar: ${total_carrito}*"
            
            mi_numero = "5351233908"
            texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
            enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
            
            st.write("---")
            st.link_button("👉 ENVIAR PEDIDO POR WHATSAPP", enlace, use_container_width=True)
        else:
            st.caption("Por favor, rellena tu nombre, dirección y CI para activar el botón de envío.")

# --- NUEVO: SECCIÓN DE CONTACTO RÁPIDO ABAJO DEL TODO ---
st.write("---")
st.write("### 📞 ¿Tienes dudas o necesitas ayuda?")
col_tel, col_chat = st.columns(2)

with col_tel:
    st.link_button("📞 Llamar por Teléfono", "tel:+5351233908", use_container_width=True)
with col_chat:
    st.link_button("💬 Chat de Dudas en WhatsApp", "https://wa.me/5351233908", use_container_width=True)
