#!/usr/bin/env bash
# Install Nginx if not already installed

if ! command -v nginx &> /dev/null; then
        apt-get update
        apt-get install -y nginx
fi

# Creates necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Holberton School!" > /data/web_static/releases/test/index.html

# Recreate the symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ to ubuntu user adn group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
CONFIG_FILE="/etc/nginx/sites-available/default"
STATIC_ALIAS="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"

# Add or update alias in nginx configuration
if grep -q "location /hbnb_static/" "$CONFIG_FILE"; then
        sed -i "/location \/hbnb_static\//c\\$STATIC_ALIAS" "$CONFIG_FILE"
else
        sed -i "s#^}#$STATIC_ALIAS\n\n\t}#" "$CONFIG_FILE"
fi

# Restart Nginx
service nginx restart
