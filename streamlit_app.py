
import streamlit as st

st.set_page_config(page_title="Variedades Suárez", page_icon="🧺")

# --- INTERFAZ: COMPATIBILIDAD TOTAL CON MODO CLARO Y OSCURO ---
st.markdown("""
    <style>
    /* Forzar fondo agradable y textos legibles en cualquier modo */
    .stApp {
        background-color: var(--background-color, #f4f6f9);
    }
    
    /* Asegurar que los títulos, subtítulos y textos principales sean siempre legibles */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: var(--text-color, #111111) !important;
    }
    
    /* Pestañas de categorías adaptables */
    .stTabs [data-baseweb="tab"] p {
        font-size: 18px !important;    
        font-weight: bold !important;  
        color: var(--text-color, #111111) !important;    
    }
    
    /* Forzar que los textos descriptivos dentro de las columnas se vean claros u oscuros según el tema */
    .stMarkdown div p {
        color: var(--text-color, #111111) !important;
    }
    
    /* Color fijo para los textos de ayuda o capturas secundarias */
    .stCaption {
        color: #555555 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧺 Variedades Suárez")

# Muestra la foto de portada
try:
    st.image("copilot_image_1779749338479.jpeg", use_container_width=True)
except:
    pass

# Flujo visual del proceso
st.write("### **🛍️ Elige tus productos** ➔ **🛒 Revisa el carrito** ➔ **📝 Envía tu pedido**")

# Tarjeta informativa de entrega
st.info("🚚 **Información de Entrega:** Llevamos tu encargo directo hasta la puerta de tu casa en el pueblo de forma rápida y segura.")

st.subheader("Haz tu encargo de productos y yo se lo llevo hasta su casa")

# --- LISTA DE PRODUCTOS ---
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

# Aquí guardaremos lo que elija el cliente
encargo = {}

st.write("---")
st.write("### 🛍️ Productos Disponibles")

# Buscador (Lupa)
buscar = st.text_input("🔍 Buscar producto por su nombre...", value="")

# Categorías Horizontales (Pestañas)
tab_todo, tab_granos, tab_bebidas, tab_pastas, tab_otros = st.tabs([
    "✨ Todo", "🌾 Granos", "🥤 Bebidas", "🍝 Pastas", "📦 Otros"
])

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
            if info["etiqueta"]:
                st.warning(info["etiqueta"])
            st.write(f"**{prod}**")
            st.write(f"Precio: ${info['precio']}")
            st.caption(info["detalle"]) 
            
            cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=f"cant_{prod}_{nombre_pestana}")
            if cantidad > 0:
                encargo[prod] = cantidad
        st.divider()

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
    
    # Sistema de Cupón de Descuento
    st.write("---")
    cupon = st.text_input("🎟️ ¿Tienes un cupón de descuento? Escríbelo aquí:").strip()
    descuento = 0
    
    if cupon == "SUAREZ10":
        descuento = total_carrito * 0.10
        st.success(f"🎉 ¡Cupón aplicado con éxito! Descuento del 10%: -${descuento:.2f}")
    elif cupon != "":
        st.error("❌ Cupón inválido o vencido.")
        
    total_final = total_carrito - descuento
    
    # 🧾 RESUMEN DE CUENTA ESTILO TICKET EN PANTALLA
    st.write("### 🧾 Resumen de Cuenta (Tu Recibo)")
    
    st.markdown("#### **📦 Productos seleccionados:**")
    for item, cant in encargo.items():
        subtotal_item = cant * productos[item]["precio"]
        st.write(f"- {cant}x {item} (${subtotal_item:.2f})")
        
    if descuento > 0:
        st.write(f"🎟️ Cupón Aplicado: SUAREZ10 (-${descuento:.2f})")
        
    st.write(f"**Subtotal bruto:** ${total_carrito:.2f}")
    st.markdown(f"### **Total Neto a Pagar: ${total_final:.2f}**")
    st.write("---")
    
    # Casilla para activar la entrega
    confirmar = st.checkbox("⚙️ Presiona aquí para continuar con la compra y poner tus datos")
    
    if confirmar:
        st.write("## 📝 Información de Entrega")
        nombre = st.text_input("Nombre y Apellidos:")
        direccion = st.text_input("Dirección de entrega:")
        ci = st.text_input("Carnet de Identidad (CI):")
        
        # Selector de Horario de Entrega
        horario = st.selectbox(
            "🕒 ¿En qué horario prefieres recibir tu pedido?",
            ["Por la Mañana (9:00 AM - 12:00 PM)", "Por la Tarde (2:00 PM - 6:00 PM)"]
        )
        
        # Notas Especiales para el Reparto
        notas = st.text_area("📝 Notas adicionales para el reparto (Opcional):", placeholder="Ej: Fachada verde, si no estoy dejar con mi vecina, etc.")
        
        if nombre and direccion and ci:
            # Construcción del texto del pedido para WhatsApp
            texto = f"¡Hola Variedades Suárez! Quiero hacer un encargo:\n\n👤 *Cliente:* {nombre}\n📍 *Dirección:* {direccion}\n🪪 *CI:* {ci}\n🕒 *Horario de entrega:* {horario}\n"
            
            if notas:
                texto += f"📝 *Notas:* {notas}\n"
                
            texto += "\n📦 *Productos:* \n"
            for item, cant in encargo.items():
                subtotal = cant * productos[item]["precio"]
                texto += f"- {cant}x {item} (${subtotal})\n"
                
            if descuento > 0:
                texto += f"\n🎟️ *Cupón Aplicado:* SUAREZ10 (-${descuento:.2f})"
                
            texto += f"\n\n*Total neto a pagar: ${total_final:.2f}*"
            
            # Número de teléfono de destino
            mi_numero = "5351233908"
            texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
            enlace_wa = f"https://wa.me/{mi_numero}?text={texto_url}"
            
            st.write("---")
            # Único botón grande para mandar a WhatsApp
            st.link_button("🟢 ENVIAR PEDIDO COMPLETO POR WHATSAPP", enlace_wa, use_container_width=True)
                
        else:
            st.caption("Por favor, rellena tu nombre, dirección y CI para activar el botón de envío.")

# --- MÉTODOS DE PAGO DISPONIBLES (SOLO EFECTIVO) ---
st.write("---")
st.success("💰 **Método de pago aceptado:** Únicamente pago en efectivo al recibir los productos en casa.")

# Sección de contacto rápido abajo del todo
st.write("### 📞 ¿Tienes dudas o necesitas ayuda?")
col_tel, col_chat = st.columns(2)

with col_tel:
    st.link_button("📞 Llamar por Teléfono", "tel:+5351233908", use_container_width=True)
with col_chat:
    st.link_button("💬 Chat de Dudas en WhatsApp", "https://wa.me/5351233908", use_container_width=True)
