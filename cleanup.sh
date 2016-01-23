#!/bin/bash
cd /root/twitterpic/
find ./  -name "*.jpg" -mmin +1200 -delete
find ./  -name "*.GIF" -mmin +120 -delete

