# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="ProyectoFinal_A01769388",
    version="1.0",
    description="Proyecto final de la materia de programación.",
    author="Víctor Alonzo Estévez Chávez",
    author_email="alonzoe04@hotmail.com",
    scripts=["main.py"],
    console=["main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)