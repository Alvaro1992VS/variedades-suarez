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

# --- INTERFAZ: BUSCADOR (LUPA) ---
buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

# --- INTERFAZ: CATEGORÍAS HORIZONTALES (PESTAÑAS) ---
tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
    "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
])

# Función interna corregida (añade el nombre de la pestaña al "key" para evitar errores de duplicado)
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
            st.write(f"**{prod}**")
            st.write(f"Precio: ${info['precio']}")
            st.caption(info["detalle"]) 
            
            # El truco secreto: agregamos el nombre_pestana aquí para que cada botón sea único en el sistema
            cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"cant_{prod}_{nombre_pestana}")
            if cantidad > 0:
                # Si el cliente agrega cantidad desde cualquier pestaña, se guarda en el mismo pedido global
                encargo[prod] = cantidad
                
        st.divider()

# Colocar los productos correctos de forma horizontal en sus pestañas
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
            
            # Tu número de teléfono configurado
            mi_numero = "5351233908"
            texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
            enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
            
            st.write("---")
            st.link_button("👉 ENVIAR PEDIDO POR WHATSAPP", enlace, use_container_width=True)
        else:
            st.caption("Por favor, rellena tu nombre, dirección y CI para activar el botón de envío.")
