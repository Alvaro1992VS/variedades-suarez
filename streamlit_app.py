import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺", layout="vertical")

# --- DISEÑO INSPIRADO EN EL YERRO MENU (INTERFAZ PREMIUM) ---
st.markdown("""
    <style>
    /* Fondo limpio y tipografía moderna */
    .stApp {
        background-color: #f7fafc;
    }
    h1, h2, h3, h4, p, label {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        color: #1a202c !important;
    }
    
    /* Encabezado de la tienda */
    .store-header {
        text-align: center;
        padding: 10px;
        margin-bottom: 5px;
    }
    .store-title {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #0f2d59 !important;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .store-tag {
        color: #2d3748 !important;
        font-size: 14px;
        font-weight: 500;
    }

    /* Pestañas de categorías estilo elyerromenu */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 20px !important;
        padding: 6px 16px !important;
    }
    .stTabs [data-baseweb="tab"] p {
        font-size: 14px !important;
        color: #4a5568 !important;
        font-weight: 600 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0f2d59 !important;
        border-color: #0f2d59 !important;
    }
    .stTabs [aria-selected="true"] p {
        color: #ffffff !important;
    }

    /* Tarjetas de productos en Cuadrícula (Grid) */
    .product-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border: 1px solid #edf2f7;
        text-align: center;
    }
    .product-title {
        font-size: 16px !important;
        font-weight: 700 !important;
        margin-top: 8px;
        margin-bottom: 2px;
    }
    .product-price {
        font-size: 15px !important;
        color: #0f2d59 !important;
        font-weight: 700 !important;
        margin-bottom: 5px;
    }

    /* Caja de Tipo de Servicio (Captura 2) */
    .service-box {
        background-color: #ffffff;
        border: 2px solid #0f2d59;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* BARRA FLOTANTE INFERIOR (VER PEDIDO) */
    .floating-bar {
        position: fixed;
        bottom: 20px;
        left: 5%;
        width: 90%;
        background-color: #0f2d59;
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 10px 20px rgba(15, 45, 89, 0.3);
        z-index: 999;
    }
    
    /* Botón verde de WhatsApp estilo elyerromenu */
    div.stLinkButton > a[href^="https://wa.me"] {
        background-color: #0f2d59 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        padding: 14px !important;
        font-size: 16px !important;
        box-shadow: 0 4px 12px rgba(15, 45, 89, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE LA TIENDA ---
st.markdown("""
    <div class="store-header">
        <p class="store-title">Conta's Empanadas Clone</p>
        <p class="store-tag">📍 Santiago de Cuba, Santiago de Cuba</p>
        <p style="color:#718096 !important; font-size:13px;">Bienvenidos al menú en línea. Haz tu encargo y te lo llevamos rápido.</p>
    </div>
    """, unsafe_allow_html=True)

# Control de navegación para simular las pantallas de las capturas
if 'ver_carrito' not in st.session_state:
    st.session_state.ver_carrito = False

# --- CATÁLOGO DE PRODUCTOS ---
productos = {
    "Americano": {"precio": 3300, "foto": "Arroz.jpg", "detalle": "Dos huevos, tostadas, bacon, frutas, café o té.", "categoria": "Desayunos"},
    "Cubano": {"precio": 2700, "foto": "Aceite.jpg", "detalle": "Tostadas, tortilla con queso, vegetales y café.", "categoria": "Desayunos"},
    "Empanada Jamón": {"precio": 450, "foto": "Azucar.jpg", "detalle": "Deliciosa empanada frita rellena de jamón y queso.", "categoria": "Empanadas"},
    "Frijoles (lb)": {"precio": 400, "foto": "Frijolrs.jpg", "detalle": "Frijoles negros nuevos, de primera calidad.", "categoria": "Otros"},
    "Pan (Unidades)": {"precio": 50, "foto": "Pan.jpg", "detalle": "Pan suave horneado fresco del día.", "categoria": "Otros"}
}

encargo = {}

# PANTALLA 1: CATÁLOGO DE PRODUCTOS (SI NO HA DADO CLICK EN VER PEDIDO)
if not st.session_state.ver_carrito:
    
    tab_todo, tab_desayunos, tab_empanadas, tab_otros = st.tabs(["🔍 Todo", "🍳 Desayunos", "🥐 Empanadas", "📦 Otros"])
    
    def render_grid(categoria_filtro=None):
        # Filtrar productos correspondientes
        prods_filtrados = {k: v for k, v in productos.items() if categoria_filtro is None or v["categoria"] == categoria_filtro}
        
        # Crear la cuadrícula de 2 columnas (Igual que en la captura 1)
        items = list(prods_filtrados.items())
        for i in range(0, len(items), 2):
            col1, col2 = st.columns(2)
            
            # Producto Izquierda
            with col1:
                prod, info = items[i]
                st.markdown('<div class="product-box">', unsafe_allow_html=True)
                try: st.image(info["foto"], use_container_width=True)
                except: st.caption("📸 (Sin foto)")
                st.markdown(f'<p class="product-title">{prod}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="product-price">{info["precio"]:.2f} CUP</p>', unsafe_allow_html=True)
                cant = st.number_input("Cantidad", min_value=0, max_value=20, value=0, step=1, key=f"grid_{prod}")
                if cant > 0: encargo[prod] = cant
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Producto Derecha (Si existe en el índice)
            with col2:
                if i + 1 < len(items):
                    prod, info = items[i+1]
                    st.markdown('<div class="product-box">', unsafe_allow_html=True)
                    try: st.image(info["foto"], use_container_width=True)
                    except: st.caption("📸 (Sin foto)")
                    st.markdown(f'<p class="product-title">{prod}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="product-price">{info["precio"]:.2f} CUP</p>', unsafe_allow_html=True)
                    cant = st.number_input("Cantidad", min_value=0, max_value=20, value=0, step=1, key=f"grid_{prod}")
                    if cant > 0: encargo[prod] = cant
                    st.markdown('</div>', unsafe_allow_html=True)

    with tab_todo: render_grid(None)
    with tab_desayunos: render_grid("Desayunos")
    with tab_empanadas: render_grid("Empanadas")
    with tab_otros: render_grid("Otros")

    # --- BARRA FLOTANTE DE REVISIÓN (CAPTURA 1 ABAJO) ---
    # Calcular totales instantáneos para colocarlos en la barra flotante
    total_items = sum(encargo.values())
    total_dinero = sum(cant * productos[item]["precio"] for item, cant in encargo.items())
    
    if total_items > 0:
        # Guardar en memoria de sesión para pasar a la otra pantalla
        st.session_state.pedido_actual = encargo
        st.session_state.total_dinero = total_dinero
        
        st.markdown(f'<div class="floating-bar">🛒 VER PEDIDO &nbsp;&nbsp;•&nbsp;&nbsp; {total_items} Producto(s) &nbsp;&nbsp;•&nbsp;&nbsp; {total_dinero:.2f} CUP</div>', unsafe_allow_html=True)
        
        # Botón invisible/transparente encima de la barra para activar el cambio de pantalla
        if st.button("Ir a pagar y revisar pedido ➔", use_container_width=True):
            st.session_state.ver_carrito = True
            st.rerun()

# PANTALLA 2: FORMULARIO DE PEDIDO Y REVISIÓN (IGUAL A LA CAPTURA 2)
else:
    # Botón para volver atrás al catálogo
    if st.button("⬅️ Volver al Menú"):
        st.session_state.ver_carrito = False
        st.rerun()
        
    st.markdown("## **Pedido**")
    
    # Caja de Tipo de Servicio
    st.markdown("""
        <div class="service-box">
            <span style="font-size:20px;">🛍️</span>
            <div>
                <strong style="color:#0f2d59 !important;">Tipo de Servicio</strong><br>
                <span style="font-size:14px; color:#4a5568;">Pedido para entregar a domicilio / casa</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    # Desglose de los productos agregados
    pedido = st.session_state.get('pedido_actual', {})
    total_final = st.session_state.get('total_dinero', 0)
    
    st.write("### Productos solicitados")
    for item, cant in pedido.items():
        subtotal_item = cant * productos[item]["precio"]
        col_img, col_txt = st.columns([1, 3])
        with col_img:
            try: st.image(productos[item]["foto"], width=65)
            except: pass
        with col_txt:
            st.markdown(f"**{item}**")
            st.markdown(f"<span style='color:#0f2d59; font-weight:bold;'>{productos[item]['precio']:.2f} CUP</span> x {cant}", unsafe_allow_html=True)
        st.divider()
        
    # Sección de Cupones Promocionales (Captura 2)
    st.write("### Cupones")
    col_cup, col_btn = st.columns([3, 1])
    with col_cup:
        cupon = st.text_input("¿Tienes código promocional?", placeholder="Escribe tu código aquí", label_visibility="collapsed").strip()
    with col_btn:
        st.button("Agregar")
        
    descuento = 0
    if cupon == "SUAREZ10":
        descuento = total_final * 0.10
        st.success(f"🎉 ¡Descuento del 10% aplicado!: -${descuento:.2f}")
        total_final -= descuento

    # Resumen de totales finales
    st.markdown(f"### **Total Neto a Pagar: {total_final:.2f} CUP**")
    st.write("---")
    
    # Formulario de datos del cliente obligatorios para WhatsApp
    st.write("### 📝 Datos de Entrega")
    nombre = st.text_input("Nombre y Apellidos:")
    direccion = st.text_input("Dirección de entrega:")
    ci = st.text_input("Carnet de Identidad (CI):")
    horario = st.selectbox("🕒 Horario de entrega preferido", ["Por la Mañana (9:00 AM - 12:00 PM)", "Por la Tarde (2:00 PM - 6:00 PM)"])
    
    if nombre and direccion and ci:
        # Construcción del mensaje formateado
        texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n🕒 *Horario:* {horario}\n\n📦 *Productos:* \n"
        for item, cant in pedido.items():
            texto += f"- {cant}x {item} (${cant * productos[item]['precio']:.2f} CUP)\n"
        texto += f"\n*Total neto a pagar: {total_final:.2f} CUP*"
        
        mi_numero = "5351233908"
        texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
        enlace_wa = f"https://wa.me/{mi_numero}?text={texto_url}"
        
        st.write("---")
        # Botón definitivo estilo Continuar con el Pedido
        st.link_button(f"CONTINUAR CON EL PEDIDO • {total_final:.2f} CUP", enlace_wa, use_container_width=True)
    else:
        st.caption("⚠️ Por favor rellena tu Nombre, Dirección y CI para activar el botón de WhatsApp.")
