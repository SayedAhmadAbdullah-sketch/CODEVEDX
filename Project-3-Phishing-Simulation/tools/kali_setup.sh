#!/bin/bash
echo "Setting up Phishing Simulation on Kali Linux..."
sudo apt-get update -qq
sudo apt-get install -y python3 python3-pip -qq
pip3 install Flask fpdf2 --quiet
python3 -c "import flask; print('Flask OK')"
echo "Setup complete! Run: cd server && python3 app.py"
