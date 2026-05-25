import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺")

# --- INTERFAZ: COLOR DE FONDO Y DISEÑO DE CATEGORÍAS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f9;
    }
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

# --- CONTROL DEL FLUJO DE LA TIENDA ---
# Aquí controlamos si el cliente está mirando la tienda o llenando sus datos
if 'paso' not in st.session_state:
    st.session_state.paso = "tienda" # El paso inicial siempre es la tienda

# Aquí inicializamos el carrito vacío si es la primera vez que entra
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}


# ==========================================
# PASO 1: LA TIENDA Y EL CARRITO
# ==========================================
if st.session_state.paso == "tienda":

    # --- INTERFAZ: BUSCADOR (LUPA) ---
    st.write("### 🛍️ Productos Disponibles")
    buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

    # --- INTERFAZ: SECCIONES (PESTAÑAS) ---
    tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
        "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
    ])

    # Función interna para mostrar los productos filtrados en pantalla
    def mostrar_productos(categoria_filtro=None):
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
                
                # Obtenemos la cantidad actual que tiene guardada en el carrito (por defecto 0)
                cant_actual = st.session_state.carrito.get(prod, 0)
                
                # Botones de cantidad más/menos directos
                cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=cant_actual, step=1, key=f"{prod}_{categoria_filtro}")
                
                # Si la cantidad cambia, la actualizamos de inmediato en el carrito
                if cantidad > 0:
                    st.session_state.carrito[prod] = cantidad
                elif prod in st.session_state.carrito and cantidad == 0:
                    del st.session_state.carrito[prod] # Si baja a 0, se quita del carrito
                    
            st.divider()

    # Colocar los productos correctos dentro de cada pestaña correspondiente
    with tab_todo:
        mostrar_productos(categoria_filtro=None)
    with tab_granos:
        mostrar_productos(categoria_filtro="Granos")
    with tab_bebidas:
        mostrar_productos(categoria_filtro="Bebidas")
    with tab_pastas:
        mostrar_productos(categoria_filtro="Pastas")
    with tab_otros:
        mostrar_productos(categoria_filtro="Otros")

    # --- SECCIÓN DEL CARRITO DE COMPRAS ---
    st.write("---")
    st.write("## 🛒 Tu Carrito de Compras")
    
    if not st.session_state.carrito:
        st.info("El carrito está vacío. Agrega cantidades arriba 👆")
    else:
        total_carrito = 0
        # Mostrar el resumen de lo que va llevando en una lista limpia
        for item, cant in st.session_state.carrito.items():
            subtotal = cant * productos[item]["precio"]
            total_carrito += subtotal
            st.write(f"🔹 **{cant}x** {item} — ${subtotal}")
