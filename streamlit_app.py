import streamlit as st

# ¡FIX PRINCIPAL!: st.set_page_config SIEMPRE debe ir primero que cualquier st.markdown
st.set_page_config(page_title="Variedades Suárez", page_icon="🧺", layout="centered")

# --- DISEÑO INSPIRADO EN EL YERRO MENU (INTERFAZ PREMIUM) ---
st.markdown("""
    <style>
    /* Fondo limpio y tipografía moderna */
    .stApp {
        background-color: #f7fafc;
    }
    h1, h2, h3, h4, p, label, span {
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
        color: #4a5568 !important;
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

    /* Tarjetas de productos en Cuadrícula (Grid de 2 Columnas) */
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
        font-size: 15px !important;
        font-weight: 700 !important;
        margin-top: 8px;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .product-price {
        font-size: 14px !important;
        color: #0f2d59 !important;
        font-weight: 700 !important;
        margin-bottom: 5px;
    }

    /* Caja de Tipo de Servicio */
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

    /* TRUCO MAESTRO: ESTILO INYECTADO PARA QUE EL BOTÓN FLOTE REALMENTE ABAJO */
    .boton-flotante-contenedor div.stButton > button {
        position: fixed !important;
        bottom: 25px !important;
        left: 5% !important;
        width: 90% !important;
        background-color: #0f2d59 !important;
        color: white !important;
        text-align: center !important;
        padding: 14px 20px !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        box-shadow: 0 8px 25px rgba(15, 45, 89, 0.45) !important;
        z-index: 999999 !important;
        border: none !important;
        display: block !important;
    }
    
    .boton-flotante-contenedor div.stButton > button:hover, 
    .boton-flotante-contenedor div.stButton > button:active, 
    .boton-flotante-contenedor div.stButton > button:focus {
        background-color: #0f2d59 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(15, 45, 89, 0.6) !important;
    }
    
    /* BOTONES ESTÁNDAR (Volver y Agregar Cupón se quedan quietos en su celda) */
    .boton-normal div.stButton > button {
        position: static !important;
        width: 100% !important;
        background-color: #ffffff !important;
        color: #1a202c !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        padding: 6px 12px !important;
        box-shadow: none !important;
    }

    .espacio-final {
        height: 95px;
    }
    
    /* Botón de confirmar pedido final (Llamativo de WhatsApp) */
    div.stLinkButton > a[href^="https://wa.me"] {
        background-color: #0f2d59 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        padding: 14px !important;
        font-size: 16px !important;
        box-shadow: 0 4px 12px rgba(15, 45, 89, 0.2) !important;
        display: block !important;
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE LA TIENDA ---
st.markdown("""
    <div class="store-header">
        <p class="store-title">🧺 Variedades Suárez</p>
        <p class="store-tag">🚚 Haz tu encargo de productos y yo se lo llevo hasta su casa</p>
    </div>
    """, unsafe_allow_html=True)

try:
    st.image("copilot_image_1779749338479.jpeg", use_container_width=True)
except:
    pass

st.info("🚚 **Información de Entrega:** Llevamos tu encargo directo hasta la puerta de tu casa en el pueblo de forma rápida y segura.")

if 'ver_carrito' not in st.session_state:
    st.session_state.ver_carrito = False

# --- TU LISTA DE PRODUCTOS ---
productos = {
    "Arroz (Lb)": {"precio": 120, "foto": "Arroz.jpg", "detalle": "Arroz blanco de grano entero de primera calidad.", "categoria": "Granos"},
    "Aceite de Cocina (1L)": {"precio": 850, "foto": "Aceite.jpg", "detalle": "Aceite vegetal ideal para freír y cocinar.", "categoria": "Otros"},
    "Azucar(lb)": {"precio": 350, "foto": "Azucar.jpg", "detalle": "Azúcar blanca refinada bien dulce.", "categoria": "Otros"},
    "Frijoles(lb)": {"precio": 400, "foto": "Frijolrs.jpg", "detalle": "Frijoles negros nuevos, blanditos al cocinar.", "categoria": "Granos"},
    "Pan(Unidades)": {"precio": 50, "foto": "Pan.jpg", "detalle": "Pan suave horneado fresco del día.", "categoria": "Otros"}
}

encargo = {}

# --- PANTALLA 1: EL CATÁLOGO EN CUADRÍCULA (GRID) ---
if not st.session_state.ver_carrito:
    
    buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")
    
    tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
        "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
    ])
    
    def render_grid(categoria_filtro=None):
        prods_filtrados = {}
        for k, v in productos.items():
            if buscar and buscar.lower() not in k.lower():
                continue
            if categoria_filtro and v["categoria"] != categoria_filtro:
                continue
            prods_filtrados[k] = v
            
        items = list(prods_filtrados.items())
        
        if len(items) == 0:
            st.caption("Próximamente agregaremos productos a esta categoría. ¡Mantente atento! 😉")
            return

        for i in range(0, len(items), 2):
            col1, col2 = st.columns(2)
            
            with col1:
                prod, info = items[i]
                st.markdown('<div class="product-box">', unsafe_allow_html=True)
                try: st.image(info["foto"], use_container_width=True)
                except: st.caption("📸 (Sin foto)")
                st.markdown(f'<p class="product-title">{prod}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="product-price">{info["precio"]:.2f} CUP</p>', unsafe_allow_html=True)
                cant = st.number_input("Cantidad", min_value=0, max_value=100, value=0, step=1, key=f"cat_{prod}_{categoria_filtro or 'todo'}")
                if cant > 0: encargo[prod] = cant
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                if i + 1 < len(items):
                    prod, info = items[i+1]
                    st.markdown('<div class="product-box">', unsafe_allow_html=True)
                    try: st.image(info["foto"], use_container_width=True)
                    except: st.caption("📸 (Sin foto)")
                    st.markdown(f'<p class="product-title">{prod}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="product-price">{info["precio"]:.2f} CUP</p>', unsafe_allow_html=True)
                    cant = st.number_input("Cantidad", min_value=0, max_value=100, value=0, step=1, key=f"cat_{prod}_{categoria_filtro or 'todo'}")
                    if cant > 0: encargo[prod] = cant
                    st.markdown('</div>', unsafe_allow_html=True)

    with tab_todo: render_grid(None)
    with tab_granos: render_grid("Granos")
    with tab_bebidas: render_grid("Bebidas")
    with tab_pastas: render_grid("Pastas")
    with tab_otros: render_grid("Otros")

    st.markdown('<div class="espacio-final"></div>', unsafe_allow_html=True)

    total_items = sum(encargo.values())
    total_dinero = sum(cant * productos[item]["precio"] for item, cant in encargo.items())
    
    if total_items > 0:
        st.session_state.pedido_actual = encargo
        st.session_state.total_dinero = total_dinero
        
        # LOGICA PERFECTA: Al estar condicionado aquí adentro, el botón deja de existir físicamente en la pantalla 2
        st.markdown('<div class="boton-flotante-contenedor">', unsafe_allow_html=True)
        if st.button(f"🛒 VER PEDIDO  •  {total_items} Producto(s)  •  {total_dinero:.2f} CUP ➔", key="btn_flotante", use_container_width=True):
            st.session_state.ver_carrito = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: EL CARRITO Y DATOS DE ENVÍO ---
else:
    st.markdown('<div class="boton-normal">', unsafe_allow_html=True)
    if st.button("⬅️ Volver al Catálogo"):
        st.session_state.ver_carrito = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("## **Pedido**")
    
    st.markdown("""
        <div class="service-box">
            <span style="font-size:22px;">📦</span>
            <div>
                <strong style="color:#0f2d59 !important; font-size:16px;">Tipo de Servicio</strong><br>
                <span style="font-size:14px; color:#4a5568;">Pedido con entrega directa a domicilio</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
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
        
    st.write("### Cupones")
    col_cup, col_btn = st.columns([3, 1])
    with col_cup:
        cupon = st.text_input("¿Tienes código promocional?", placeholder="Escribe tu código aquí", label_visibility="collapsed").strip()
    with col_btn:
        st.markdown('<div class="boton-normal">', unsafe_allow_html=True)
        st.button("Agregar")
        st.markdown('</div>', unsafe_allow_html=True)
        
    descuento = 0
    if cupon == "SUAREZ10":
        descuento = total_final * 0.10
        st.success(f"🎉 ¡Cupón SUAREZ10 aplicado! Descuento: -${descuento:.2f} CUP")
        total_final -= descuento

    st.markdown(f"### **Total Neto a Pagar: {total_final:.2f} CUP**")
    st.write("---")
    
    st.write("### 📝 Información de Entrega")
    nombre = st.text_input("Nombre y Apellidos:")
    direccion = st.text_input("Dirección de entrega:")
    ci = st.text_input("Carnet de Identidad (CI):")
    horario = st.selectbox("🕒 Horario de entrega preferido", ["Por la Mañana (9:00 AM - 12:00 PM)", "Por la Tarde (2:00 PM - 6:00 PM)"])
    notas = st.text_area("📝 Notas adicionales para el reparto (Opcional):", placeholder="Ej: Fachada verde, dejar con la vecina...")
    
    if nombre and direccion and ci:
        texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n🕒 *Horario:* {horario}\n"
        if notas:
            texto += f"📝 *Notas:* {notas}\n"
        
        texto += "\n📦 *Productos:* \n"
        for item, cant in pedido.items():
            texto += f"- {cant}x {item} (${cant * productos[item]['precio']:.2f} CUP)\n"
            
        if descuento > 0:
            texto += f"\n🎟️ *Cupón Aplicado:* {cupon} (-${descuento:.2f} CUP)\n"
            
        texto += f"\n*Total neto a pagar: {total_final:.2f} CUP*"
        
        mi_numero = "5351233908"
        texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
        enlace_wa = f"https://wa.me/{mi_numero}?text={texto_url}"
        
        st.write("---")
        st.link_button(f"CONTINUAR CON EL PEDIDO • {total_final:.2f} CUP", enlace_wa, use_container_width=True)
    else:
        st.caption("⚠️ Por favor completa tu Nombre, Dirección y CI para habilitar el botón de WhatsApp.")

# --- MÉTODOS DE PAGO Y CONTACTO ---
st.write("---")
st.success("💰 **Método de pago:** Únicamente pago en efectivo al recibir los productos en casa.")

st.write("### 📞 ¿Necesitas ayuda?")
col_tel, col_chat = st.columns(2)
with col_tel:
    st.link_button("📞 Llamar por Teléfono", "tel:+5351233908", use_container_width=True)
with col_chat:
    st.link_button("💬 Chat de WhatsApp", "https://wa.me/5351233908", use_container_width=True)
