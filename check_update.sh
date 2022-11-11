#!/bin/sh
curl -L http://mirrors.ctan.org/systems/texlive/tlnet/archive/ 2>/dev/null |grep -E dehyph-exptl.r[0-9]*\.tar |sed -e 's,.*dehyph-exptl\.r,,;s,\.tar.*,,' |sort -V |tail -n1
