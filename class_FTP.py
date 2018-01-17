#!/usr/bin/python
# -*- coding: utf-8 -*

from ftplib import *

class ftpManager():
    """
        Gestion FTP
    """
    def __init__(self, host, login, password):
        """Connection au serveur FTP"""
        self.ftp = FTP(host, login, password)
    def list(self):
        """Afficher le contenu du dossier"""
        self.ftp.dir()
    def cp(self, lpath, rpath):
        """
        Copier un fichier
        - lpath = Chemin local
        - rpath = Chemin distant
        """
        self.upfile = open(lpath, "rb")
        self.upname = rpath
        self.ftp.storlines("STOR " + self.upname, self.upfile)
    def ren(self, oldname, newname):
        """Renommer dossier"""
        self.ftp.rename(oldname, newname)
    def mkdir(self, name):
        """Créer un dossier"""
        self.ftp.mkd(name)
    def rmdir(self, name):
        """Supprimer un dossier"""
        self.ftp.rmd(name)
    def rm(self, name):
        """Supprimer un fichier"""
        self.ftp.delete(name)
    def cd(self, name):
        """Changer de dossier"""
        self.ftp.connect.sendcmd('CWD '+ name)