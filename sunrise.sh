#!/bin/bash
cd /root/twitterpic/
python camcap.py
python t2.py >>/root/twitterpic/sunrise.log
python twitup.py >>/root/twitterpic/sunrise.log


