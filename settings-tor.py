#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.webdriver import FirefoxProfile


profile = webdriver.FirefoxProfile()
profile.set_preference("places.history.enabled", False)
profile.set_preference("privacy.clearOnShutdown.offlineApps", True)
profile.set_preference("privacy.clearOnShutdown.passwords", True)
profile.set_preference("privacy.clearOnShutdown.siteSettings", True)
profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
profile.set_preference("signon.rememberSignons", False)
profile.set_preference("network.cookie.lifetimePolicy", 2)
profile.set_preference("network.dns.disablePrefetch", True)
profile.set_preference("network.http.sendRefererHeader", 0)

#set socks proxy
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks_version", 5)
profile.set_preference("network.proxy.socks", '127.0.0.1')
profile.set_preference("network.proxy.socks_port", 9050)
profile.set_preference("network.proxy.socks_remote_dns", True)


profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", "/path/download")
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream")
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.closeWhenDone", True)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
profile.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(profile)
driver.get("hhttps://github.com/")
