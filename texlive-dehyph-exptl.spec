Name:		texlive-dehyph-exptl
Version:	0.22
Release:	1
Summary:	Experimental hyphenation patterns for the German language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/dehyph-exptl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
The package provides experimental hyphenation patterns for the
German language, covering both traditional and reformed
orthography. The patterns can be used with packages Babel and
hyphsubst.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyph-exptl.tex
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphn-x-2011-07-01.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphn-x-2011-07-01.tex
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehypht-x-2011-07-01.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehypht-x-2011-07-01.tex
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphts-x-2011-07-01.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphts-x-2011-07-01.tex
%_texmf_language_dat_d/dehyph-exptl
%_texmf_language_def_d/dehyph-exptl
%_texmf_language_lua_d/dehyph-exptl
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/CHANGES
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/INSTALL
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/LICENSE
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/README
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/dehyph-exptl.bib
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/dehyph-exptl.pdf
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/projektbeschreibung.bib
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/projektbeschreibung.pdf
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl/projektbeschreibung.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/dehyph-exptl <<EOF
%% from dehyph-exptl:
german-x-2011-07-01 dehypht-x-2011-07-01.tex
=german-x-latest
ngerman-x-2011-07-01 dehyphn-x-2011-07-01.tex
=ngerman-x-latest
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/dehyph-exptl <<EOF
%% from dehyph-exptl:
\addlanguage{german-x-2011-07-01}{dehypht-x-2011-07-01.tex}{}{2}{2}
\addlanguage{german-x-latest}{dehypht-x-2011-07-01.tex}{}{2}{2}
\addlanguage{ngerman-x-2011-07-01}{dehyphn-x-2011-07-01.tex}{}{2}{2}
\addlanguage{ngerman-x-latest}{dehyphn-x-2011-07-01.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/dehyph-exptl <<EOF
-- from dehyph-exptl:
	['german-x-2011-07-01'] = {
		loader = 'dehypht-x-2011-07-01.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'german-x-latest' },
		patterns = 'hyph-de-1901.pat.txt',
		hyphenation = 'hyph-de-1901.hyp.txt',
	},
	['ngerman-x-2011-07-01'] = {
		loader = 'dehyphn-x-2011-07-01.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'ngerman-x-latest' },
		patterns = 'hyph-de-1996.pat.txt',
		hyphenation = 'hyph-de-1996.hyp.txt',
	},
EOF