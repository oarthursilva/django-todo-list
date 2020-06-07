#!/usr/bin/env python
"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
print(get_random_string(50, chars))
