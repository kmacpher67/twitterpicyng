#!/bin/bash
cd /root/twitterpic/
python camcap.py
python t4.py >>/root/twitterpic/sunrise.log
python twitup.py >>/root/twitterpic/sunrise.log


