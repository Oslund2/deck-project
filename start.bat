@echo off
echo Starting Deck Cost Calculator...
echo Open http://localhost:8000 in your browser
cd /d "%~dp0"
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
