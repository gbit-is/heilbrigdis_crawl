# wait, what ?

.... okay, þetta er ljótt mess
en þetta er gert með að:

1) keyra saekja_starfsleyfi.py, sem að sækjir lista af öllum starfsleyfum hjá heilbrigðiseftirlitinu
2) keyra grep_kt.sh, sem að greppar út allar kennitölur úr síðunum sóttum úr skrefi 1 og setur í skjal
3) keyra dl_all.py, sem að framkvæmir leit per kennitölu, og dumpar út html-inu af hverri síðu
4) keyra parser.py, sem að keyrir á móti öllum sóttu skýrslunum, finnur þau gögn sem er áhugavert að safna og býr til json með þeim
