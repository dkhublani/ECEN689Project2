#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:47:05 2018

Name: khalednakhleh
"""

from setuptools import setup

__version__ = "0.5.0"
__author__ = "Khaled Nakhleh"
__name__ = "ECEN 689 project 2"

description = "Capture and label gray images using a stereoscopic camera setup.\
Images were captured using a custom-built rover."

requirements = [
 "opencv=>3.4.2"]

setup(
      name = __name__,
      description = description,
      install_requires = requirements,
      version = __version__,
      author = __author__,
      author_email = "khaled.jkn@gmail.com",
      url = "https://github.com/khalednakhleh/ECEN689Project2"    
      )