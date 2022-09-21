#!/bin/sh
POT_FILE=locale/tf2c-downloader.pot
xgettext --package-name=tf2c-downloader --keyword=_ --keyword=_N:1,2 -l python -o "$POT_FILE" *.py
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	msgmerge -U "$PO_FILE" "$POT_FILE"
done
