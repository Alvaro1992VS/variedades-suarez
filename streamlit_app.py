import streamlit as st

st.set_page_config(page_title="Variedades Suárez")

st.title("Variedades Suárez")
st.subheader("Haz tu encargo de productos y yo se los llevo a mi pueblo")

# Lista de tus productos con precio, foto y ahora con DETALLES
productos = {
    "Arroz (Lb)": {
        "precio": 120, 
        "foto": "Arroz.jpg", 
        "detalle": "Arroz blanco de grano entero de primera calidad."
    },
    "Aceite de Cocina (1L)": {
        "precio": 850, 
        "foto": "Aceite.jpg", 
        "detalle": "Aceite vegetal ideal para freír y cocinar."
    },
    "Azucar(lb)": {
        "precio": 350, 
        "foto": "Azucar.jpg", 
        "detalle": "Azúcar blanca refinada bien dulce."
    },
    "Frijoles(lb)": {
        "precio": 400, 
        "foto": "Frijolrs.jpg", 
        "detalle": "Frijoles negros nuevos, blanditos al cocinar."
    },
    "Pan(Unidades)": {
        "precio": 50, 
        "foto": "Pan.jpg", 
        "detalle": "Pan suave horneado fresco del día."
    },
    # Para agregar más productos, cópialos con "precio", "foto" y "detalle" igual que arriba
}

# Aquí guardaremos lo que elija el cliente
encargo = {}

st.write("### Productos Disponibles")

# Mostrar productos con sus fotos, detalles y botones
for prod, info in productos.items():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Intenta cargar la foto desde GitHub
        try:
            st.image(info["foto"], width=100)
        except:
            st.caption("📸 (Sin foto)")
            
    with col2:
        st.write(f"**{prod}**")
        st.write(f"Precio: ${info['precio']}")
        # ESTA LÍNEA MUESTRA LOS DETALLES EN LETRA MÁS PEQUEÑA Y GRIS
        st.caption(info["detalle"]) 
        
        # Botones de más/menos
        cantidad = st.number_input(f"Cantidad para {prod}", min_value=0, max_value=100, value=0, step=1, key=prod)
        if cantidad > 0:
            encargo[prod] = cantidad
            
    st.divider() # Pone una línea fina gris para separar un producto del otro y que se vea más ordenado

# Datos del cliente
st.write("### Datos de entrega")
nombre = st.text_input("Nombre:")
direccion = st.text_input("Dirección:")
ci = st.text_input("Carnet de Identidad (CI):")

# Botón de envío directo por WhatsApp
if st.button("Enviar encargo por WhatsApp"):
    if nombre and direccion and ci and encargo:
        texto = f"Hola, soy {nombre}.\nMi dirección es: {direccion}\nMi CI es: {ci}\n\nEste es mi encargo:\n"
        total = 0
        for item, cant in encargo.items():
            subtotal = cant * productos[item]["precio"]
            total += subtotal
            texto += f"- {cant}x {item} (${subtotal})\n"
        texto += f"\n*Total a pagar: ${total}*"
        
        # ⚠️ PON AQUÍ TU NÚMERO DE TELÉFONO REAL
        mi_numero = "521234567890"
        
        # Codificar los espacios y saltos de línea para WhatsApp
        texto_url = texto.replace(" ", "%20").replace("\n", "%0A")
        enlace = f"https://wa.me/{mi_numero}?text={texto_url}"
        
        st.markdown(f'[👉 Haz clic aquí para enviar el pedido por WhatsApp]({enlace})')
    else:
        st.error("Por favor, llena tus datos y selecciona al menos 1 producto usando los botones de más (+).")

