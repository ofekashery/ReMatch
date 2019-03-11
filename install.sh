#!/usr/bin/env bash

# Clone and enter ReMatch directory
git clone https://github.com/tweirtx/ReMatch
cd ReMatch

# Install pyenv
curl https://pyenv.run | bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
echo 'export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Install Python dependencies
pyenv install 3.7.2
pyenv local 3.7.2
pip install -Ur requirements.txt

# Set up postgres
sudo -u postgres psql "CREATE DATABASE rematch;"
sudo -u postgres psql "CREATE ROLE rematch;"
sudo -u postgres psql "ALTER ROLE rematch PASSWORD 'matchbox';"
sudo -u postgres psql "ALTER ROLE rematch LOGIN;"

echo "All done!"
