#!/bin/bash
echo "Git Pull"
git pull
echo "Service Restart"
sudo systemctl restart webradio
