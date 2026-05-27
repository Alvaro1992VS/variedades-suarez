import streamlit as st

# Configuración de página obligatoria en la primera línea
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
        padding: 5px 0px;
        margin-bottom: 5px;
    }
    .store-title {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #0f2d59 !important;
        text-transform: uppercase;
        margin-bottom: 2px;
        line-height: 1.1;
    }
    .store-tag {
        color: #4a5568 !important;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 0px;
    }

    /* SECCIÓN DE PUBLICIDAD Y PROMOCIONES */
    .promo-section-title {
        font-size: 16px !important;
        font-weight: 700 !important;
        color: #0f2d59 !important;
        margin-top: 10px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .promo-box {
        background: linear-gradient(135deg, #0f2d59 0%, #1a4a86 100%);
        border-radius: 12px;
        padding: 12px;
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(15, 45, 89, 0.15);
        margin-bottom: 10px;
        text-align: center;
        min-height: 105px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .promo-box p, .promo-box span, .promo-box strong {
        color: #ffffff !important;
    }
    .promo-badge {
        background-color: #e53e3e;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        width: fit-content;
        margin: 0 auto 5px auto;
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
    }

    /* Caja informativa de Dirección del Local */
    .local-direction-box {
        background-color: #ebf8ff;
        border-left: 4px solid #3182ce;
        border-radius: 4px;
        padding: 12px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .local-direction-text {
        font-size: 14px !important;
        color: #2b6cb0 !important;
        font-weight: 600 !important;
        line-height: 1.4;
    }

    /* Botón estándar para cupones y volver */
    .boton-normal div.stButton > button {
        background-color: #ffffff !important;
        color: #1a202c !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        padding: 6px 12px !important;
    }
    
    /* Botón DEL CARRITO SUPERIOR DERECHA */
    .cart-btn-container div.stButton > button {
        background-color: #ffffff !important;
        color: #0f2d59 !important;
        border: 2px solid #0f2d59 !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        padding: 8px 12px !important;
        font-size: 14px !important;
        transition: all 0.3s ease;
    }
    .cart-active div.stButton > button {
        background-color: #0f2d59 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(15, 45, 89, 0.3) !important;
    }
    
    /* Botón final de WhatsApp */
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

# --- INICIALIZACIÓN DE VARIABLES GLOBALES DE SESIÓN ---
if 'ver_carrito' not in st.session_state:
    st.session_state.ver_carrito = False
if 'pedido_persistente' not in st.session_state:
    st.session_state.pedido_persistente = {}

# --- TU LISTA DE PRODUCTOS ---
productos = {
    "Arroz (Lb)": {"precio": 120, "foto": "Arroz.jpg", "categoria": "Granos"},
    "Aceite de Cocina (1L)": {"precio": 850, "foto": "Aceite.jpg", "categoria": "Otros"},
    "Azucar(lb)": {"precio": 350, "foto": "Azucar.jpg", "categoria": "Otros"},
    "Frijoles(lb)": {"precio": 400, "foto": "Frijolrs.jpg", "categoria": "Granos"},
    "Pan(Unidades)": {"precio": 50, "foto": "Pan.jpg", "categoria": "Otros"}
}

# --- FUNCIÓN DE CONTROL ---
def actualizar_carrito(prod_id, cat_filtro):
    key_input = f"cat_{prod_id}_{cat_filtro}"
    nueva_cantidad = st.session_state.get(key_input, 0)
    
    if nueva_cantidad > 0:
        st.session_state.pedido_persistente[prod_id] = nueva_cantidad
    else:
        if prod_id in st.session_state.pedido_persistente:
            del st.session_state.pedido_persistente[prod_id]

# Calcular totales
total_items = sum(st.session_state.pedido_persistente.values())
total_dinero = sum(cant * productos[item]["precio"] for item, cant in st.session_state.pedido_persistente.items())

# --- CABECERA SUPERIOR DINÁMICA ---
col_titulo, col_carrito = st.columns([3, 1.2])

with col_titulo:
    st.markdown("""
        <div class="store-header">
            <p class="store-title">🧺 Variedades Suárez</p>
            <p class="store-tag">🚚 Encarga y te lo llevo al pueblo</p>
        </div>
        """, unsafe_allow_html=True)

with col_carrito:
    if not st.session_state.ver_carrito:
        cart_style = "cart-active" if total_items > 0 else "cart-empty"
        st.markdown(f'<div class="cart-btn-container {cart_style}" style="margin-top: 15px; text-align: right;">', unsafe_allow_html=True)
        label_carrito = f"🛒 ({total_items})" if total_items > 0 else "🛒 Vacío"
        if st.button(label_carrito, key="ir_al_carrito_top"):
            if total_items > 0:
                st.session_state.ver_carrito = True
                st.rerun()
            else:
                st.toast("⚠️ Añade algún producto primero", icon="🧺")
        st.markdown('</div>', unsafe_allow_html=True)

try:
    st.image("copilot_image_1779749338479.jpeg", use_container_width=True)
except:
    pass

# --- PANTALLA 1: EL CATÁLOGO ---
if not st.session_state.ver_carrito:
    st.info(" Haz tu encargo de productos y yo se lo llevo directo hasta la puerta de su casa.")
    
    # SECCIÓN: DEstacados y Promociones
    st.markdown('<p class="promo-section-title">🔥 Destacados y Promociones</p>', unsafe_allow_html=True)
    col_promo1, col_promo2 = st.columns(2)
    
    with col_promo1:
        st.markdown("""
            <div class="promo-box">
                <div class="promo-badge">Descuento</div>
                <strong style="font-size: 13px;">10% MENOS</strong>
                <p style="font-size: 11px; margin: 2px 0 0 0;">Usa el cupón <span style="background-color:#fff; color:#0f2d59; padding:1px 4px; border-radius:4px; font-weight:bold;">SUAREZ10</span> al revisar tu pedido.</p>
            </div>
            """, unsafe_allow_html=True)
            
    with col_promo2:
        st.markdown("""
            <div class="promo-box" style="background: linear-gradient(135deg, #1d6132 0%, #113b1e 100%); text-align: center;">
                <div class="promo-badge" style="background-color:#d69e2e;">⭐ Más Vendido</div>
                <strong style="font-size: 13px;">🌾 Arroz Blanco</strong>
                <p style="font-size: 11px; margin: 2px 0 0 0;">El grano preferido del pueblo. ¡Calidad premium garantizada!</p>
            </div>
            """, unsafe_allow_html=True)
            
    st.write("")
    
    buscar = st.text_input("🔍 Buscar producto...", value="")
    
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
            st.caption("Próximamente más existencias. 😉")
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
                
                val_inicial = st.session_state.pedido_persistente.get(prod, 0)
                st.number_input("Cantidad", min_value=0, max_value=100, value=val_inicial, step=1, 
                                key=f"cat_{prod}_{categoria_filtro or 'todo'}", 
                                on_change=actualizar_carrito, args=(prod, categoria_filtro or 'todo'))
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                if i + 1 < len(items):
                    prod, info = items[i+1]
                    st.markdown('<div class="product-box">', unsafe_allow_html=True)
                    try: st.image(info["foto"], use_container_width=True)
                    except: st.caption("📸 (Sin foto)")
                    st.markdown(f'<p class="product-title">{prod}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="product-price">{info["precio"]:.2f} CUP</p>', unsafe_allow_html=True)
                    
                    val_inicial_2 = st.session_state.pedido_persistente.get(prod, 0)
                    st.number_input("Cantidad", min_value=0, max_value=100, value=val_inicial_2, step=1, 
                                    key=f"cat_{prod}_{categoria_filtro or 'todo'}", 
                                    on_change=actualizar_carrito, args=(prod, categoria_filtro or 'todo'))
                    st.markdown('</div>', unsafe_allow_html=True)

    with tab_todo: render_grid(None)
    with tab_granos: render_grid("Granos")
    with tab_bebidas: render_grid("Bebidas")
    with tab_pastas: render_grid("Pastas")
    with tab_otros: render_grid("Otros")

# --- PANTALLA 2: EL CARRITO Y DATOS DE ENVÍO ---
else:
    st.markdown('<div class="boton-normal">', unsafe_allow_html=True)
    if st.button("⬅️ Volver al Catálogo"):
        st.session_state.ver_carrito = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("## **Pedido**")
    
    # =========================================================================
    # NUEVO: SELECCIÓN DE TIPO DE SERVICIO (DOMICILIO O LOCAL)
    # =========================================================================
    tipo_servicio = st.radio(
        "📦 **Selecciona el Método de Entrega:**",
        ["🚚 Entrega a domicilio", "🏪 Recoger en el local"],
        index=0
    )
    
    # Lógica condicional: Si es en el local, muestra la dirección solicitada
    if tipo_servicio == "🏪 Recoger en el local":
        st.markdown("""
            <div class="local-direction-box">
                <span style="font-size:16px; font-weight:bold; color:#2b6cb0;">📍 Dirección del Local:</span><br>
                <p class="local-direction-text">Facultad №1 De Medicina Por Calle E de Sueño</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.caption("✨ Llevaremos tu pedido directo hasta la puerta de tu casa.")
    st.write("---")
    # =========================================================================
        
    pedido_seguro = st.session_state.pedido_persistente
    total_final = total_dinero
    
    st.write("### Productos solicitados")
    for item, cant in pedido_seguro.items():
        subtotal_item = cant * productos[item]["precio"]
        col_img, col_txt = st.columns([1, 3])
        with col_img:
            try: st.image(productos[item]["foto"], width=65)
            except: pass
        with col_txt:
            st.markdown(f"**{item}**")
            st.markdown(f"<span style='color:#0f2d59; font-weight:bold;'>{productos[item]['precio']:.2f} CUP</span> x {cant} = **{subtotal_item:.2f} CUP**", unsafe_allow_html=True)
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

    if descuento > 0:
        st.markdown(f"**Subtotal:** {total_dinero:.2f} CUP")
        st.markdown(f"<span style='color:green;'>**Descuento (SUAREZ10):** -{descuento:.2f} CUP</span>", unsafe_allow_html=True)
    
    st.markdown(f"### **Total Neto a Pagar: {total_final:.2f} CUP**")
    st.write("---")
    
    st.write("### 📝 Información de Entrega")
    nombre = st.text_input("Nombre y Apellidos:")
    
    # Si selecciona recoger en el local, el campo de dirección cambia automáticamente
    if tipo_servicio == "🏪 Recoger en el local":
        direccion = "Retira en el local (Facultad №1 De Medicina Por Calle E de Sueño)"
        st.text_input("Dirección de entrega:", value=direccion, disabled=True, help="Has seleccionado recoger en el local.")
    else:
        direccion = st.text_input("Dirección de entrega:", placeholder="Escribe tu dirección exacta del pueblo...")
        
    ci = st.text_input("Carnet de Identidad (CI):")
    horario = st.selectbox("🕒 Horario preferido", ["Por la Mañana (9:00 AM - 12:00 PM)", "Por la Tarde (2:00 PM - 6:00 PM)"])
    notas = st.text_area("📝 Notas adicionales (Opcional):", placeholder="Ej: Dejar el paquete listo, voy en moto...")
    
    # Validación para activar el botón final
    if nombre and direccion and ci:
        # CONSTRUCCIÓN DEL MENSAJE DINÁMICO DE WHATSAPP
        texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📦 *Método:* {tipo_servicio}\n📍 *Lugar/Dirección:* {direccion}\n🪪 *CI:* {ci}\n🕒 *Horario:* {horario}\n"
        if notas:
            texto += f"📝 *Notas:* {notas}\n"
        
        texto += "\n📦 *Productos:* \n"
        for item, cant in pedido_seguro.items():
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
st.success("💰 **Método de pago:** Únicamente pago en efectivo al recibir/recoger los productos.")

st.write("### 📞 ¿Necesitas ayuda?")
col_tel, col_chat = st.columns(2)
with col_tel:
    st.link_button("📞 Llamar por Teléfono", "tel:+5351233908", use_container_width=True)
with col_chat:
    st.link_button("💬 Chat de WhatsApp", "https://wa.me/5351233908", use_container_width=True)
