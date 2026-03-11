@echo off
echo Starting Spam Email Detector App...

IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
    
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    
    echo Installing required packages...
    pip install -r requirements.txt
    
    IF NOT EXIST "models" (
        echo Training initial model...
        python train_model.py
    )
) ELSE (
    call venv\Scripts\activate.bat
)

echo Launching Streamlit...
streamlit run app.py
pause
