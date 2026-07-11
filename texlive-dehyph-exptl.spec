%global tl_name dehyph-exptl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Experimental hyphenation patterns for the German language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/dehyph-exptl
License:	mit lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides experimental hyphenation patterns for the German
language, covering both traditional and reformed orthography. The
patterns can be used with packages Babel and hyphsubst from the Oberdiek
bundle. Dieses Paket enthalt experimentelle Trennmuster fur die deutsche
Sprache. Die Trennmuster decken das in Deutschland, Osterreich und der
Schweiz gebrauchliche Standarddeutsch in der traditionellen und
reformierten Rechtschreibung ab und konnen mit den Paketen Babel und
hyphsubst aus dem Oberdiek-Bundel verwendet werden.

