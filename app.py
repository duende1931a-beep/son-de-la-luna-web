import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Son de la Luna | Dúo Vocal",
    page_icon="🌙",
    layout="wide"
)

# Estilos visuales personalizados (Tema Nocturno / Elegante)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b132b 0%, #1c2541 100%);
        color: #edf2f4;
    }
    .main-title {
        text-align: center;
        color: #f4d35e;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #a3cef1;
        font-size: 1.3rem;
        margin-bottom: 30px;
    }
    .chord-box {
        background-color: #111827;
        border-left: 5px solid #f4d35e;
        padding: 15px;
        border-radius: 8px;
        font-family: monospace;
        font-size: 1.1rem;
        white-space: pre-wrap;
    }
    </style>
""", unsafe_allow_html=True)

# Menú lateral
st.sidebar.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400", width='stretch')
st.sidebar.title("🌙 Son de la Luna")
opcion = st.sidebar.radio("Navegación", ["Inicio / Bio", "Repertorio y Tonos", "Galería y Demos", "Contrataciones"])

# 1. INICIO / BIO
if opcion == "Inicio / Bio":
    st.markdown('<p class="main-title">🌙 SON DE LA LUNA</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Dúo Vocal & Música en Vivo</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=700", caption="Son de la Luna en Vivo", width='stretch')
    with col2:
        st.subheader("Sobre el Dúo")
        st.write("""
        **Son de la Luna** es un dúo vocal femenino caracterizado por su armonía única, 
        elegancia y un repertorio versátil que abarca desde la bohemia y el bolero hasta 
        la música acústica contemporánea.
        
        Con un equipamiento de sonido de alta fidelidad y procesamiento dedicado, 
        ofrecen una experiencia musical envolvente e inolvidable para todo tipo de eventos.
        """)
        st.info("💡 **Disponible para:** Bodas, eventos corporativos, noches culturales y presentaciones privadas.")

# 2. REPERTORIO Y TONOS
elif opcion == "Repertorio y Tonos":
    st.header("🎵 Repertorio Interactivo & Transportador")
    st.write("Selecciona una canción para ajustar la tonalidad de acuerdo a la voz:")

    repertorio = {
        "Luna de Plata (Bolero)": {
            "tono": "Am",
            "letra": "Bajo la luz de plata, tu voz se vuelve canción...\n\n[Intro]: Am - Dm - E7 - Am\n\nAm                   Dm\nEn la noche clara te escucho cantar\nG                    C\ncon la luna llena sobre la ciudad."
        },
        "Noche de Bohemia (Balada)": {
            "tono": "G",
            "letra": "Estrellas brillando en el cielo, cantando a dúo otra vez...\n\n[Intro]: G - Em - C - D\n\nG                    Em\nSiento tu armonía en cada compás\nC                    D\nson de la luna que no morirá."
        },
        "Sombra y Luz (Fusión)": {
            "tono": "Dm",
            "letra": "Caminando despacio, sintiendo el ritmo...\n\n[Intro]: Dm - A7 - Dm\n\nDm                   A7\nLuces y sombras en el escenario\nBb                   C          F\nnuestra guitarra marca el calendario."
        }
    }

    cancion = st.selectbox("Seleccionar Canción:", list(repertorio.keys()))
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Tono Base", repertorio[cancion]["tono"])
        semitonos = st.slider("Transportar Tono (Semitonos):", -6, 6, 0)
        if semitonos != 0:
            st.success(f"Ajuste: {semitonos:+d} semitonos")
    
    with col2:
        st.subheader("Letra con Acordes")
        st.markdown(f'<div class="chord-box">{repertorio[cancion]["letra"]}</div>', unsafe_allow_html=True)

# 3. GALERÍA Y DEMOS
elif opcion == "Galería y Demos":
    st.header("📸 Galería & Grabaciones de Ensayos")
    
    st.subheader("Escucha nuestros Ensayos")
    col_aud1, col_aud2 = st.columns(2)
    with col_aud1:
        st.write("🎵 Demo Vocal 1 - Prueba de Micrófonos")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    with col_aud2:
        st.write("🎵 Demo Vocal 2 - Acústico")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

    st.divider()
    st.subheader("Fotos de Presentaciones")
    g1, g2, g3 = st.columns(3)
    with g1:
        st.image("https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=400", caption="Prueba de Sonido", width='stretch')
    with g2:
        st.image("https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400", caption="En Vivo", width='stretch')
    with g3:
        st.image("https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=400", caption="Set Acústico", width='stretch')

# 4. CONTRATACIONES
elif opcion == "Contrataciones":
    st.header("📞 Agenda tu Evento con Son de la Luna")
    st.write("Completa los datos para coordinar una fecha o contáctanos por WhatsApp.")

    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Tu Nombre:")
        fecha = st.date_input("Fecha del Evento:")
        tipo_evento = st.selectbox("Tipo de Evento:", ["Boda", "Cumpleaños", "Corporativo", "Restaurante / Bar", "Otro"])
        if st.button("Enviar Solicitud"):
            st.success("¡Gracias! Nos pondremos en contacto contigo a la brevedad.")

    with col2:
        st.subheader("Contacto Directo")
        telefono = "51952894252" # Reemplazar con el número real
        mensaje_wa = f"Hola, me interesa contratar a Son de la Luna para un evento de tipo {tipo_evento}."
        url_wa = f"https://wa.me/{telefono}?text={mensaje_wa.replace(' ', '%20')}"
        
        st.markdown(f'''
            <a href="{url_wa}" target="_blank">
                <button style="background-color:#25D366; color:white; border:none; padding:15px 25px; border-radius:8px; font-size:18px; font-weight:bold; cursor:pointer; width:100%;">
                    💬 Contratar vía WhatsApp
                </button>
            </a>
        ''', unsafe_allow_html=True)