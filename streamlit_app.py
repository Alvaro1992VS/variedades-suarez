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

# Aquí guardaremos lo que elija el cliente en la pantalla actual
encargo = {}

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
            
            # Botones de cantidad más/menos directos
            cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"{prod}_{categoria_filtro}")
            if cantidad > 0:
                encargo[prod] = cantidad
                
        st.divider()
