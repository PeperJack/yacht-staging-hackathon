#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🍌 Yacht Interior Staging - Nano Banana Hackathon
Yacht interior design with Google Gemini AI
Based on the official Google Home Staging documentation
"""

import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit Configuration
st.set_page_config(
    page_title="🍌 Yacht Interior Staging - Nano Banana",
    page_icon="🛥️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styles
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(135deg, #2C3E50 0%, #34495E 100%);
    color: white;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.style-card {
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    padding: 1.2rem;
    margin: 0.5rem 0;
    background: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
.style-card:hover {
    border-color: #3498db;
    box-shadow: 0 6px 12px rgba(52, 152, 219, 0.2);
}
.result-container {
    border: 3px solid #27AE60;
    border-radius: 15px;
    padding: 1rem;
    background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%);
}
.banana-divider {
    text-align: center;
    font-size: 2rem;
    margin: 2rem 0;
}
.security-notice {
    background: #e8f4fd;
    border-left: 4px solid #3498db;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Interior design styles configuration
INTERIOR_STYLES = {
    "modern_luxury": {
        "name": "🏢 Modern Luxury",
        "description": "Contemporary design, clean lines, noble materials",
        "prompt": "Transform this yacht interior into a modern luxury design with clean lines, contemporary furniture, premium materials like marble and brushed steel, neutral color palette with white, grey, and black accents, minimalist aesthetic, high-end finishes, and sophisticated lighting."
    },
    "classic_elegance": {
        "name": "👑 Classic Elegance",
        "description": "Timeless style, woodwork, leather and precious fabrics",
        "prompt": "Transform this yacht interior into classic elegant style with rich mahogany wood paneling, leather upholstery, brass fixtures, traditional nautical elements, warm color palette, crystal chandeliers, antique-inspired furniture, and timeless luxury finishes."
    },
    "mediterranean": {
        "name": "🌊 Mediterranean",
        "description": "Blue and white, natural materials, coastal atmosphere",
        "prompt": "Transform this yacht interior with Mediterranean coastal style featuring blue and white color scheme, natural materials like rattan and teak, nautical stripes, sea-inspired decorative elements, light fabrics, rope details, and fresh coastal atmosphere."
    },
    "scandinavian": {
        "name": "🌲 Scandinavian",
        "description": "Light wood, functional design, natural tones",
        "prompt": "Transform this yacht interior with Scandinavian design featuring light wood finishes, functional minimalist furniture, natural color palette with whites and light greys, cozy textiles, simple clean lines, and bright airy atmosphere."
    },
    "art_deco": {
        "name": "✨ Art Deco",
        "description": "Geometry, gilding, 1920s glamour",
        "prompt": "Transform this yacht interior with Art Deco style featuring geometric patterns, gold accents, rich jewel tones, velvet upholstery, mirrored surfaces, dramatic lighting, luxurious materials, and glamorous 1920s-inspired design elements."
    },
    "industrial_chic": {
        "name": "🔩 Industrial Chic",
        "description": "Metal, aged leather, Edison lighting",
        "prompt": "Transform this yacht interior with industrial chic style featuring exposed metal elements, distressed leather, Edison bulb lighting, raw materials, steel and iron accents, vintage industrial furniture, and urban loft aesthetics."
    },
    "tropical_resort": {
        "name": "🌴 Tropical Resort",
        "description": "Bamboo, warm tones, exotic atmosphere",
        "prompt": "Transform this yacht interior with tropical resort style featuring bamboo elements, warm earth tones, tropical plants, natural fiber textiles, rattan furniture, exotic wood finishes, and relaxing vacation resort atmosphere."
    },
    "contemporary_minimalist": {
        "name": "⚪ Contemporary Minimalist",
        "description": "Simplicity, clean spaces, functionality",
        "prompt": "Transform this yacht interior with contemporary minimalist design featuring ultra-clean lines, monochromatic color scheme, hidden storage, sleek surfaces, minimal decoration, maximum functionality, and zen-like simplicity."
    }
}

def initialize_session_state():
    """Initializes Streamlit session state variables"""
    if 'generated_image' not in st.session_state:
        st.session_state.generated_image = None
    if 'original_image' not in st.session_state:
        st.session_state.original_image = None
    if 'generation_time' not in st.session_state:
        st.session_state.generation_time = None

# ▼▼▼ CODE CORRIGÉ ▼▼▼
def setup_api_client():
    """Configures the Google Gemini API client with environment variables"""
    api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
    
    if not api_key:
        st.error("🔐 API key not configured. Check your .env file")
        st.markdown("""
        <div class="security-notice">
        <h4>🛡️ Secure configuration required</h4>
        <p>Create a <code>.env</code> file in the project folder with:</p>
        <code>GOOGLE_GEMINI_API_KEY=your_api_key_here</code>
        <br><br>
        <p>Get your API key at: <a href="https://ai.google.dev/" target="_blank">https://ai.google.dev/</a></p>
        </div>
        """, unsafe_allow_html=True)
        return None
    
    try:
        # Reverting to the older genai.Client() method
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        st.error(f"❌ API configuration error: {repr(e)}")
        return None


# ▼▼▼ REMPLACEZ VOTRE FONCTION PAR CETTE DERNIÈRE VERSION ▼▼▼

# ▼▼▼ REMPLACEZ VOTRE FONCTION PAR CETTE VERSION PLUS SÉCURISÉE ▼▼▼

# ▼▼▼ REMPLACEZ VOTRE FONCTION PAR CETTE VERSION DÉFINITIVE ▼▼▼

def yacht_interior_staging(client, image, styling_prompt, custom_prompt=""):
    """
    Transforms the yacht interior with Google Gemini
    using the correct preview model and robust API call syntax.
    """
    
    base_prompt = f"""Using the provided image of a yacht interior space, transform the decoration and styling while maintaining the architectural structure.

{styling_prompt}

{f"Additional customization: {custom_prompt}" if custom_prompt else ""}

CRITICAL REQUIREMENTS FOR YACHT INTERIOR STAGING:
- Keep the room's architectural structure, windows, and basic layout unchanged
- Only change furniture, decorations, colors, lighting, and styling elements  
- Ensure all furniture and decorations are appropriate for a yacht/marine environment
- Consider space constraints and nautical safety requirements
- Make it look luxurious and professionally staged for yacht sales/charter
- Maintain yacht-specific elements like portholes, built-in features, marine lighting
- Create an aspirational interior that appeals to luxury yacht buyers/charterers

Style: Professional yacht interior photography, luxury marine interior design, magazine quality, perfect lighting, high-end yacht staging for marketing purposes."""

    try:
        # L'ingrédient secret ! On retourne au modèle "preview" qui a le pouvoir 
        # de générer des images.
        model_id = "gemini-2.5-flash-image-preview"
        
        response = client.models.generate_content(
            model=model_id,
            contents=[image, base_prompt],
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=4096
                # Pas besoin de "response_mime_type", ce modèle spécial sait quoi faire.
            )
        )
        
        # Initialiser une liste vide pour les parties d'image
        image_parts = []
        
        if (response.candidates and 
            response.candidates[0].content and
            response.candidates[0].content.parts):
            
            image_parts = [
                part.inline_data.data
                for part in response.candidates[0].content.parts
                if hasattr(part, 'inline_data') and part.inline_data
            ]

        if image_parts:
            generated_image = Image.open(BytesIO(image_parts[0]))
            return generated_image, None
        else:
            if hasattr(response, 'text') and response.text:
                return None, f"Model returned text instead of an image: {response.text[:200]}..."
            return None, "No image found in the API response."
            
    except Exception as e:
        return None, f"Error during generation: {repr(e)}"
    
def save_image_with_metadata(image, original_filename, styling_option):
    """Saves the image with metadata"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"yacht_interior_{styling_option}_{timestamp}.png"
    
    # Create the output directory if it doesn't exist
    os.makedirs("generated_interiors", exist_ok=True)
    filepath = os.path.join("generated_interiors", filename)
    
    image.save(filepath, "PNG", quality=95)
    return filepath

def display_comparison(original_image, generated_image):
    """Displays the before/after comparison"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏠 Before - Original")
        st.image(original_image, use_column_width=True, caption="Original interior")
    
    with col2:
        st.subheader("✨ After - Gemini Staging")
        st.image(generated_image, use_column_width=True, caption="Transformed interior")

def main():
    """Main Streamlit application"""
    initialize_session_state()
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🍌 Yacht Interior Staging Pro</h1>
        <h2>Nano Banana Hackathon</h2>
        <p>Transform the interior design of your yachts with Google Gemini AI</p>
        <p><strong>🏆 Powered by Google Gemini 2.5 Flash</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Secure API configuration
    client = setup_api_client() # Changed from model to client
    
    if not client: # Changed from model to client
        st.stop()
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📤 Upload & Configuration")
        
        # Image upload
        uploaded_file = st.file_uploader(
            "Select a yacht interior photo",
            type=['png', 'jpg', 'jpeg'],
            help="Can be an empty room, already furnished, living room, cabin, galley, etc. (max 10MB)"
        )
        
        if uploaded_file:
            # Load and display the original image
            original_image = Image.open(uploaded_file)
            st.session_state.original_image = original_image
            
            st.image(original_image, caption="Original interior", use_column_width=True)
            
            # Decoration style selection
            st.subheader("🎨 Decoration Style")
            
            # Display style options as cards
            styling_option = st.selectbox(
                "Choose your decoration style:",
                options=list(INTERIOR_STYLES.keys()),
                format_func=lambda x: INTERIOR_STYLES[x]["name"]
            )
            
            # Display the description of the selected style
            selected_style = INTERIOR_STYLES[styling_option]
            st.markdown(f"""
            <div class="style-card">
                <h4>{selected_style["name"]}</h4>
                <p><strong>Description:</strong> {selected_style["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Customization option
            st.subheader("🎯 Customization (Optional)")
            custom_prompt = st.text_area(
                "Specific requests:",
                placeholder="Ex: Add green plants, change the cushion color to navy blue, add nautical elements...",
                help="Specify your particular wishes in addition to the chosen style"
            )
            
            # Generation button
            if st.button("🚀 Transform the Interior", type="primary", use_container_width=True):
                with st.spinner("🍌 Nano Banana is generating your new style..."):
                    start_time = datetime.now()
                    
                    # Generation
                    generated_image, error = yacht_interior_staging(
                        client, # Changed from model to client
                        original_image, 
                        selected_style["prompt"],
                        custom_prompt
                    )
                    
                    if generated_image:
                        end_time = datetime.now()
                        generation_time = (end_time - start_time).total_seconds()
                        
                        st.session_state.generated_image = generated_image
                        st.session_state.generation_time = generation_time
                        
                        st.success(f"✅ New style created in {generation_time:.1f} seconds!")
                    else:
                        st.error(f"❌ {error}")
    
    with col2:
        st.header("✨ Result")
        
        if st.session_state.generated_image:
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.image(st.session_state.generated_image, caption="Transformed interior", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action buttons
            col_download, col_save = st.columns(2)
            
            with col_download:
                # Prepare for download
                img_buffer = BytesIO()
                st.session_state.generated_image.save(img_buffer, format="PNG", quality=95)
                img_data = img_buffer.getvalue()
                
                st.download_button(
                    "💾 Download HD",
                    data=img_data,
                    file_name=f"yacht_interior_staged_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                    mime="image/png",
                    use_container_width=True
                )
            
            with col_save:
                if st.button("💽 Save locally", use_container_width=True):
                    if uploaded_file:
                        filepath = save_image_with_metadata(
                            st.session_state.generated_image,
                            uploaded_file.name,
                            styling_option
                        )
                        st.success(f"Saved: {filepath}")
            
            # Statistics
            if st.session_state.generation_time:
                st.info(f"⏱️ Generation time: {st.session_state.generation_time:.1f}s")
        
        else:
            st.info("🎯 Your transformed interior will appear here")
            st.markdown("""
            ### 💡 Supported interior types:
            - **Saloons**: Reception and relaxation areas
            - **Cabins**: Bedrooms
            - **Galleys**: Kitchen and preparation areas
            - **Empty spaces**: To be fully decorated
            - **Covered decks**: Protected outdoor areas
            """)
    
    # Before/After comparison
    if st.session_state.original_image and st.session_state.generated_image:
        st.markdown('<div class="banana-divider">🍌🍌🍌</div>', unsafe_allow_html=True)
        st.header("📊 Before/After Comparison")
        display_comparison(st.session_state.original_image, st.session_state.generated_image)
    
    # Footer information
    st.markdown("---")
    st.markdown("""
    ### 🍌 Nano Banana Hackathon Information
    - **Specialty**: Luxury yacht interior design
    - **AI Model**: Google Gemini 2.5 Flash
    - **Technique**: Home Staging adapted for marine environments
    - **Security**: Secure API via environment variables
    - **Market**: Nautical agents, yacht brokers, marine architects
    
    **🏆 Innovation: First yacht interior staging tool with generative AI**
    """)

if __name__ == "__main__":
    main()