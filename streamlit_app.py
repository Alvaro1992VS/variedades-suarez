import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺")

# --- INTERFAZ: COLOR DE FONDO DE LA PÁGINA ---
# Aquí puedes cambiar el color de fondo (background-color) si lo deseas en el futuro
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
# Nota que añadimos "categoria" a cada uno para poder dividirlos en secciones
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
    },
    # Ejemplos listos para cuando agregues en el futuro:
    # "Refresco Ciego Montero": {"precio": 250, "foto": "Refresco.jpg", "detalle": "Sabor original 1.5L", "categoria": "Bebidas"},
    # "Espaguetis (400g)": {"precio": 300, "foto": "Espaguetis.jpg", "detalle": "Pasta larga de sémola", "categoria": "Pastas"}
}

# Aquí guardaremos lo que elija el cliente
encargo = {}

# --- INTERFAZ: BUSCADOR (LUPA) ---
st.write("### 🛍️ Productos Disponibles")
buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

# --- INTERFAZ: SECCIONES (PESTAÑAS) ---
# Creamos las 5 pestañas que pediste
tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
    "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
])

# Función interna para mostrar los productos filtrados en pantalla
def mostrar_productos(categoria_filtro=None):
    for prod, info in productos.items():
        # Filtro 1: Si el usuario escribió en la lupa, comprobamos si el nombre coincide
        if buscar and buscar.lower() not in prod.lower():
            continue
            
        # Filtro 2: Si estamos en una pestaña específica, comprobamos la categoría
        if categoria_filtro and info["categoria"] != categoria_filtro:
            continue
            
        # Dibujar el producto en pantalla
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
            
            # Botones de cantidad más/menos
            cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"{prod}_{categoria_filtro}")
            if cantidad > 0:
                encargo[prod] = cantidad
                
        st.divider()

# Colocar los productos correctos dentro de cada pestaña correspondiente
with tab_todo:
    mostrar_productos(categoria_filtro=None) # Muestra absolutamente todos

with tab_granos:
    mostrar_productos(categoria_filtro="Granos")

with tab_bebidas:
    mostrar_productos(categoria_filtro="Bebidas")

with tab_pastas:
    mostrar_productos(categoria_filtro="Pastas")

with tab_otros:
    mostrar_productos(categoria_filtro="Otros")


# --- DATOS DEL CLIENTE ---
st.write("### Datos de entrega")
nombre = st.text_input("Nombre:")
direccion = st.text_input("Dirección:")
ci = st.text_input("Carnet de Identidad (CI):")

# --- BOTÓN DE WHATSAPP ---
if st.button("Enviar encargo por WhatsApp"):
    if nombre and direccion and ci and encargo:
        texto = f"Hola, soy {nombre}.\nMi dirección es: {direccion}\nMi CI es: {ci}\n\nEste es mi encargo:\n"
        total = 0
        for item, cant in encargo.items():
            subtotal = cant * productos[item]["precio"]
            total += subtotal
            texto += f"- {cant}x {item} (${subtotal})\n"
        texto += f"\n*Total a pagar: ${total}*"
        
        mi_numero = "5351233908" # Tu número real se mantiene intacto
        
        texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
        enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
        
        st.markdown(f'[👉 Haz clic aquí para enviar el pedido por WhatsApp]({enlace})')
    else:
        st.error("Por favor, llena tus datos y selecciona al menos 1 producto usando los botones de más (+).")
