#!/bin/bash

locust -f /locustfile.py --host=$TARGET_URL
