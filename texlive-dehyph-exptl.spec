%global tl_name dehyph-exptl
%global tl_revision 79618
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides experimental hyphenation patterns for the German
language, covering both traditional and reformed orthography. The
patterns can be used with packages Babel and hyphsubst from the Oberdiek
bundle. Dieses Paket enthalt experimentelle Trennmuster fur die deutsche
Sprache. Die Trennmuster decken das in Deutschland, Osterreich und der
Schweiz gebrauchliche Standarddeutsch in der traditionellen und
reformierten Rechtschreibung ab und konnen mit den Paketen Babel und
hyphsubst aus dem Oberdiek-Bundel verwendet werden.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from dehyph-exptl:
german-x-2024-02-28 dehypht-x-2024-02-28.tex
=german-x-latest
ngerman-x-2024-02-28 dehyphn-x-2024-02-28.tex
=ngerman-x-latest
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from dehyph-exptl:
\addlanguage{german-x-2024-02-28}{dehypht-x-2024-02-28.tex}{}{2}{2}
\addlanguage{german-x-latest}{dehypht-x-2024-02-28.tex}{}{2}{2}
\addlanguage{ngerman-x-2024-02-28}{dehyphn-x-2024-02-28.tex}{}{2}{2}
\addlanguage{ngerman-x-latest}{dehyphn-x-2024-02-28.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from dehyph-exptl:
['german-x-2024-02-28'] = {
	loader = 'dehypht-x-2024-02-28.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'german-x-latest' },
	patterns = 'hyph-de-1901.pat.txt',
},
['ngerman-x-2024-02-28'] = {
	loader = 'dehyphn-x-2024-02-28.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'ngerman-x-latest' },
	patterns = 'hyph-de-1996.pat.txt',
},
TL_HYPHEN_EOF
