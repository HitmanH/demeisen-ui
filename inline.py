#!/usr/bin/env python3
"""Inline dist/demeisen.css (at a git ref) into a single-file web page, between the lines
<!-- demeisen-ui:begin --> and <!-- demeisen-ui:end -->. The logo and favicon become data: URIs, so the page
needs no other files. For apps deployed as one HTML file. Usage: python3 inline.py <ref> <page.html>"""
import base64, os, re, subprocess, sys
ref, page = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
show = lambda p: subprocess.check_output(["git", "-C", here, "show", f"{ref}:{p}"])
uri = lambda p: "data:image/png;base64," + base64.b64encode(show(p)).decode()
css = show("dist/demeisen.css").decode().replace('url("assets/logo-mark.png")', f'url("{uri("dist/assets/logo-mark.png")}")')
rev = subprocess.check_output(["git", "-C", here, "rev-parse", "--short", ref], text=True).strip()
block = (f'<!-- demeisen-ui:begin -->\n<!-- Demeisen UI @ {rev}: do not edit here; run demeisen-ui/inline.py -->\n'
         f'<link rel="icon" href="{uri("dist/assets/favicon.png")}">\n<style>\n{css.strip()}\n</style>\n<!-- demeisen-ui:end -->')
html = open(page, encoding="utf-8").read()
new, n = re.subn(r"<!-- demeisen-ui:begin -->[\s\S]*?<!-- demeisen-ui:end -->", lambda m: block, html)
if n != 1: sys.exit("markers not found (add <!-- demeisen-ui:begin --> and <!-- demeisen-ui:end --> to the page)")
open(page, "w", encoding="utf-8").write(new); print(f"Demeisen UI {rev} inlined into {page}")
