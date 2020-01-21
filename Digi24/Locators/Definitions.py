# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, os, datetime

from selenium.webdriver.common.by import By


class Defs():
    driver = webdriver.Chrome()