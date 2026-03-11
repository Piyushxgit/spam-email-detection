#!/bin/bash
echo "Starting Spam Email Detector App..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    echo "Installing required packages..."
    pip install -r requirements.txt
    
    echo "Training initial model if needed..."
    if [ ! -d "models" ]; then
        python train_model.py
    fi
else
    source venv/bin/activate
fi

echo "Launching Streamlit..."
streamlit run app.py
