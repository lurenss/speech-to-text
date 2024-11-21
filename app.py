import streamlit as st
import whisper
import os
import tempfile
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="App per le lezioni di Giorgia",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #FF69B4;
        font-size: 3em;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        color: #4B0082;
        font-size: 1.5em;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for the model
if 'model' not in st.session_state:
    st.session_state['model'] = None

def load_whisper_model(model_size):
    """Load the Whisper model."""
    try:
        model = whisper.load_model(model_size)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def process_audio(audio_file, model):
    """Process the audio file and return the transcription."""
    try:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the uploaded file to the temporary directory
            temp_path = Path(temp_dir) / "audio_file"
            with open(temp_path, "wb") as f:
                f.write(audio_file.getvalue())

            # Transcribe the audio
            result = model.transcribe(str(temp_path))
            return result["text"]
    except Exception as e:
        return f"Error processing audio: {str(e)}"

def main():
    # Display title and image
    st.markdown('<h1 class="main-title">App per le lezioni di Giorgia 👩‍🏫</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Trasforma le tue registrazioni audio in testo! 🎯</p>', unsafe_allow_html=True)
    
    # Display the image
    image_path = os.path.join("images", "teaching.png")
    if os.path.exists(image_path):
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(image_path, width=200)  # Set a specific width of 200 pixels
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 2])
    
    # Sidebar for model selection
    with st.sidebar:
        st.title("⚙️ Impostazioni")
        model_size = st.selectbox(
            "Seleziona il modello Whisper",
            ["tiny", "base", "small", "medium", "large"],
            help="I modelli più grandi sono più accurati ma più lenti"
        )
        
        if st.button("Carica/Cambia Modello"):
            with st.spinner(f"Caricamento del modello {model_size}..."):
                st.session_state['model'] = load_whisper_model(model_size)
                if st.session_state['model']:
                    st.success(f"✅ Modello {model_size} caricato con successo!")

    # Main content
    with col1:
        st.markdown("""
        ### 📝 Istruzioni:
        1. Seleziona un modello dalla barra laterale
        2. Carica un file audio
        3. Clicca su 'Trascrivi Audio'
        4. Scarica il testo trascritto
        """)
    
    with col2:
        st.write("### 🎤 Carica il tuo file audio")
        uploaded_file = st.file_uploader("Scegli un file audio", type=['mp3', 'wav', 'm4a', 'ogg'])
        
        if uploaded_file is not None:
            st.audio(uploaded_file)
            
            # Check if model is loaded
            if st.session_state['model'] is None:
                with st.spinner(f"Caricamento del modello {model_size}..."):
                    st.session_state['model'] = load_whisper_model(model_size)
            
            if st.button('Trascrivi Audio 🎯'):
                if st.session_state['model']:
                    with st.spinner('Trascrizione in corso...'):
                        transcription = process_audio(uploaded_file, st.session_state['model'])
                        
                    st.markdown("### 📄 Testo Trascritto:")
                    st.write(transcription)
                    
                    # Add download button for the transcribed text
                    st.download_button(
                        label="📥 Scarica trascrizione",
                        data=transcription,
                        file_name="trascrizione.txt",
                        mime="text/plain"
                    )
                else:
                    st.error("Attendi il caricamento del modello o prova a ricaricarlo dalla barra laterale.")

if __name__ == '__main__':
    main()
