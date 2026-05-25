import streamlit as st
import urllib.parse

# Configuración de la página (Título y diseño)
st.set_page_config(page_title="Variedades Suárez", page_icon="🛍️", layout="centered")

# Título principal
st.title("🛍️ VARIEDADES SUÁREZ")
st.subheader("Haz tu pedido de forma fácil y recíbelo en casa")
st.markdown("---")

# Lista de productos (Puedes ampliarla hasta 20 aquí mismo)
if 'productos' not in st.session_state:
    st.session_state.productos = [
        {"nombre": "Arroz (lb)", "precio": 150,"foto":Arroz.jpg},
        {"nombre": "Frijoles (lb)", "precio": 200},
        {"nombre": "Aceite (lt)", "precio": 500},
        {"nombre": "Pan (unidad)", "precio": 50},
        {"nombre": "Azúcar (lb)", "precio": 120},
    ]

# Inicializar el carrito en la sesión si no existe
if 'carrito' not in st.session_state:
    st.session_state.carrito = {p["nombre"]: 0 for p in st.session_state.productos}

# --- SECCIÓN DE PRODUCTOS ---
st.header("📋 Menú de Productos")

for p in st.session_state.productos:
    nombre = p["nombre"]
    precio = p["precio"]
    
    # Creamos 3 columnas: Nombre/Precio, Botón Menos, Botón Más
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.write(f"**{nombre}**")
        st.write(f"${precio} * Cantidad: {st.session_state.carrito[nombre]}*")
    
    with col2:
        if st.button(f"➖", key=f"restar_{nombre}"):
            if st.session_state.carrito[nombre] > 0:
                st.session_state.carrito[nombre] -= 1
                st.rerun()
                
    with col3:
        if st.button(f"➕", key=f"sumar_{nombre}"):
            st.session_state.carrito[nombre] += 1
            st.rerun()
            
    st.markdown("---")

# --- SECCIÓN DE DATOS DE ENVÍO ---
st.header("📍 Datos de Entrega")
nombre_cliente = st.text_input("Nombre Completo:")
ci_cliente = st.text_input("Carné de Identidad (CI):")
direccion_cliente = st.text_input("Dirección de Entrega:")

st.markdown("---")

# --- LÓGICA DE ENVÍO POR WHATSAPP ---
texto_productos = ""
total = 0
hay_productos = False

# Calcular totales
for p in st.session_state.productos:
    cant = st.session_state.carrito[p["nombre"]]
    if cant > 0:
        subtotal = cant * p["precio"]
        texto_productos += f"• {p['nombre']} x{cant}: ${subtotal}\n"
        total += subtotal
        hay_productos = True

# Botón para enviar por WhatsApp
if st.button("🚀 ENVIAR PEDIDO POR WHATSAPP", use_container_width=True):
    if not nombre_cliente or not ci_cliente or not direccion_cliente:
        st.error("⚠️ Por favor, completa todos los campos de entrega antes de enviar.")
    elif not hay_productos:
        st.error("⚠️ No has seleccionado ningún producto en tu carrito.")
    else:
        # Formatear el mensaje para WhatsApp
        mensaje_completo = (
            f"🛍️ *VARIEDADES SUÁREZ - NUEVO PEDIDO*\n\n"
            f"👤 *Cliente:* {nombre_cliente}\n"
            f"🪪 *CI:* {ci_cliente}\n"
            f"📍 *Dirección:* {direccion_cliente}\n\n"
            f"📋 *Detalle del Pedido:*\n{texto_productos}\n"
            f"💰 *TOTAL A PAGAR: ${total}*"
        )
        
        # Codificar texto para la URL
        mensaje_codificado = urllib.parse.quote(mensaje_completo)
        enlace_wa = f"https://wa.me/5351233908?text={mensaje_codificado}"
        
        # En la web, mostramos un enlace directo estilizado
        st.success("¡Pedido listo para enviar!")
        st.markdown(
            f'<a href="{enlace_wa}" target="_blank" style="text-decoration:none;">'
            '<div style="background-color:#25D366;color:white;padding:12px;text-align:center;'
            'font-weight:bold;border-radius:5px;font-size:18px;">'
            '🟢 CONFIRMAR Y ABRIR WHATSAPP 🟢</div></a>', 
            unsafe_allow_html=True
        )
