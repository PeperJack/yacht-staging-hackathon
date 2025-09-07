#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
⚓ Yacht Interior Staging Professional
Transform yacht interiors with AI-powered design solutions
Professional yacht staging for luxury marine properties
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
    page_title="Yacht Interior Staging Pro",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styles - Professional Agency Design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

.main {
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(135deg, #18181b 0%, #23272f 100%);
    min-height: 100vh;
}

.hero-section {
    background: linear-gradient(135deg, #0f3460 0%, #16537e 50%, #2980b9 100%);
    color: white;
    padding: 3rem 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    text-align: center;
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M20 20h60v60H20z" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></svg>');
    opacity: 0.3;
}

.hero-section > * {
    position: relative;
    z-index: 1;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    background: linear-gradient(45deg, #ffffff, #a8d8ea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.4rem;
    font-weight: 300;
    opacity: 0.9;
    margin-bottom: 1rem;
}

.hero-description {
    font-size: 1.1rem;
    opacity: 0.8;
    max-width: 600px;
    margin: 0 auto;
}

.service-card {
    background: #111111;
    color: #fff;
    border-radius: 16px;
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.4s ease;
    backdrop-filter: blur(10px);
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 45px rgba(41, 128, 185, 0.2);
    border-color: #2980b9;
}

.style-option {
    background: linear-gradient(135deg, #18181b 0%, #23272f 100%);
    color: #fff;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 0.8rem 0;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.style-option:hover {
    border-color: #2980b9;
    background: linear-gradient(135deg, #23272f 0%, #18181b 100%);
    transform: translateX(5px);
}

.style-option.selected {
    border-color: #2980b9;
    background: linear-gradient(135deg, #23272f 0%, #18181b 100%);
    box-shadow: 0 4px 20px rgba(41, 128, 185, 0.3);
    color: #fff;
}

.result-showcase {
    background: linear-gradient(135deg, #18181b 0%, #23272f 100%);
    color: #fff;
    border: 3px solid #22c55e;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 40px rgba(34, 197, 94, 0.2);
}

.upload-section {
    background: #111111;
    color: #fff;
    border: 3px dashed #cbd5e1;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    margin: 1rem 0;
}

.upload-section:hover {
    border-color: #2980b9;
    background: #23272f;
}

.stats-container {
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    text-align: center;
}

.agency-cta {
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    margin: 2rem 0;
    box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.feature-item {
    background: #18181b;
    color: #fff;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.feature-item:hover {
    transform: translateY(-3px);
}

.btn-primary {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.btn-primary:hover {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.4);
}

.security-notice {
    background: linear-gradient(135deg, #18181b 0%, #23272f 100%);
    color: #fff;
    border-left: 4px solid #3b82f6;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 0 12px 12px 0;
}

.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #2980b9, transparent);
    margin: 3rem 0;
    border-radius: 1px;
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
    """Initialize Streamlit session state variables"""
    if 'generated_image' not in st.session_state:
        st.session_state.generated_image = None
    if 'original_image' not in st.session_state:
        st.session_state.original_image = None
    if 'generation_time' not in st.session_state:
        st.session_state.generation_time = None

def setup_api_client():
    """Configure the Google Gemini API client with environment variables"""
    api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
    
    if not api_key:
        st.error("🔐 API Configuration Required")
        st.markdown("""
        <div class="security-notice">
        <h4>🛡️ Secure API Configuration</h4>
        <p>Please create a <code>.env</code> file in your project directory with:</p>
        <code>GOOGLE_GEMINI_API_KEY=your_api_key_here</code>
        <br><br>
        <p>Obtain your API key at: <a href="https://ai.google.dev/" target="_blank">Google AI Studio</a></p>
        </div>
        """, unsafe_allow_html=True)
        return None
    
    try:
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        st.error(f"❌ API Configuration Error: {repr(e)}")
        return None

def yacht_interior_staging(client, image, styling_prompt, custom_prompt=""):
    """
    Transform yacht interior with Google Gemini
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
        model_id = "gemini-2.5-flash-image-preview"
        
        response = client.models.generate_content(
            model=model_id,
            contents=[image, base_prompt],
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=4096
            )
        )
        
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
    """Save the image with metadata"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"yacht_interior_{styling_option}_{timestamp}.png"
    
    os.makedirs("generated_interiors", exist_ok=True)
    filepath = os.path.join("generated_interiors", filename)
    
    image.save(filepath, "PNG", quality=95)
    return filepath

def display_comparison(original_image, generated_image):
    """Display the before/after comparison"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Original Interior")
        st.image(original_image, use_column_width=True, caption="Before transformation")
    
    with col2:
        st.subheader("✨ Transformed Design")
        st.image(generated_image, use_column_width=True, caption="After AI staging")

def main():
    """Main Streamlit application"""
    initialize_session_state()
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">⚓ Yacht Interior Staging</div>
        <div class="hero-subtitle">Professional AI-Powered Design Solutions</div>
        <div class="hero-description">
            Transform luxury yacht interiors with cutting-edge artificial intelligence. 
            Professional staging solutions for yacht brokers, marine architects, and luxury property specialists.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # API Configuration
    client = setup_api_client()
    
    if not client:
        st.stop()
    
    # Professional Features Section
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-item">
            <h3>🎨 8+ Design Styles</h3>
            <p>From modern luxury to classic elegance, covering all high-end interior design trends</p>
        </div>
        <div class="feature-item">
            <h3>⚡ Instant Results</h3>
            <p>Professional-grade transformations in seconds using Google Gemini AI</p>
        </div>
        <div class="feature-item">
            <h3>🛥️ Yacht-Specific</h3>
            <p>Specialized for marine environments with safety and space considerations</p>
        </div>
        <div class="feature-item">
            <h3>📈 Sales Ready</h3>
            <p>Magazine-quality results perfect for marketing materials and listings</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Main Interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="service-card">
            <h2>📤 Upload & Configuration</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Image Upload
        uploaded_file = st.file_uploader(
            "Select yacht interior photograph",
            type=['png', 'jpg', 'jpeg'],
            help="Upload high-resolution images for best results (max 10MB)"
        )
        
        if uploaded_file:
            # Load and display original image
            original_image = Image.open(uploaded_file)
            st.session_state.original_image = original_image
            
            st.image(original_image, caption="Original Interior", use_column_width=True)
            
            # Design Style Selection
            st.subheader("🎨 Select Design Style")
            
            styling_option = st.selectbox(
                "Choose your preferred interior design style:",
                options=list(INTERIOR_STYLES.keys()),
                format_func=lambda x: INTERIOR_STYLES[x]["name"]
            )
            
            # Style Description
            selected_style = INTERIOR_STYLES[styling_option]
            st.markdown(f"""
            <div class="style-option selected">
                <h4>{selected_style["name"]}</h4>
                <p><strong>Style Profile:</strong> {selected_style["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Custom Requirements
            st.subheader("🎯 Custom Requirements")
            custom_prompt = st.text_area(
                "Additional specifications:",
                placeholder="e.g., Add nautical artwork, change color scheme to navy and gold, include plants, specific furniture requests...",
                help="Specify any additional requirements or modifications to the selected style"
            )
            
            # Generation Button
            if st.button("🚀 Generate Professional Staging", type="primary", use_container_width=True):
                with st.spinner("🎨 Creating your professional yacht interior design..."):
                    start_time = datetime.now()
                    
                    # Generate transformation
                    generated_image, error = yacht_interior_staging(
                        client,
                        original_image, 
                        selected_style["prompt"],
                        custom_prompt
                    )
                    
                    if generated_image:
                        end_time = datetime.now()
                        generation_time = (end_time - start_time).total_seconds()
                        
                        st.session_state.generated_image = generated_image
                        st.session_state.generation_time = generation_time
                        
                        st.success(f"✅ Professional staging completed in {generation_time:.1f} seconds!")
                    else:
                        st.error(f"❌ {error}")
    
    with col2:
        st.markdown("""
        <div class="service-card">
            <h2>✨ Professional Results</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.generated_image:
            st.markdown('<div class="result-showcase">', unsafe_allow_html=True)
            st.image(st.session_state.generated_image, caption="Professionally Staged Interior", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col_download, col_save = st.columns(2)
            
            with col_download:
                # Prepare download
                img_buffer = BytesIO()
                st.session_state.generated_image.save(img_buffer, format="PNG", quality=95)
                img_data = img_buffer.getvalue()
                
                st.download_button(
                    "💾 Download High-Res",
                    data=img_data,
                    file_name=f"yacht_staging_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                    mime="image/png",
                    use_container_width=True
                )
            
            with col_save:
                if st.button("💽 Save to Gallery", use_container_width=True):
                    if uploaded_file:
                        filepath = save_image_with_metadata(
                            st.session_state.generated_image,
                            uploaded_file.name,
                            styling_option
                        )
                        st.success(f"✅ Saved: {filepath}")
            
            # Performance Stats
            if st.session_state.generation_time:
                st.markdown(f"""
                <div class="stats-container">
                    <h4>⚡ Performance Metrics</h4>
                    <p>Generation Time: <strong>{st.session_state.generation_time:.1f} seconds</strong></p>
                    <p>Model: <strong>Google Gemini 2.5 Flash</strong></p>
                    <p>Quality: <strong>Professional Grade</strong></p>
                </div>
                """, unsafe_allow_html=True)
        
        else:
            st.info("🎯 Your transformed yacht interior will appear here")
            st.markdown("""
            ### 🛥️ Supported Yacht Spaces:
            - **Main Salons** - Primary entertainment and dining areas
            - **Master Suites** - Owner's cabins and VIP staterooms  
            - **Guest Cabins** - Visitor accommodations
            - **Galley Areas** - Kitchen and food preparation spaces
            - **Sky Lounges** - Upper deck entertainment areas
            - **Covered Decks** - Protected outdoor living spaces
            """)
    
    # Before/After Comparison
    if st.session_state.original_image and st.session_state.generated_image:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
            <h2>📊 Before & After Comparison</h2>
        </div>
        """, unsafe_allow_html=True)
        display_comparison(st.session_state.original_image, st.session_state.generated_image)
    
    # Professional CTA
    st.markdown("""
    <div class="agency-cta">
        <h2>🏆 Professional Yacht Interior Staging</h2>
        <p>Elevate your yacht listings with AI-powered professional staging solutions. 
        Perfect for yacht brokers, marine real estate professionals, and luxury property specialists.</p>
        <p><strong>✨ Powered by Google Gemini 2.5 Flash - The Future of Interior Design</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    ### ⚓ Professional Yacht Staging Solutions
    **Specialized Services:**
    - Luxury yacht interior transformation
    - AI-powered design visualization  
    - Professional-grade staging for sales & charter
    - Marine-specific design considerations
    - High-resolution marketing materials
    
    **Target Markets:** Yacht brokers, marine architects, luxury property specialists, charter companies
    
    **Technology:** Google Gemini 2.5 Flash AI • Professional marine interior design algorithms
    """)

if __name__ == "__main__":
    main()