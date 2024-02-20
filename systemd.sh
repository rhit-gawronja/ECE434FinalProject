#!/bin/bash

sudo cp entrycam.service /lib/systemd/system
sudo systemctl enable entrycam.service
