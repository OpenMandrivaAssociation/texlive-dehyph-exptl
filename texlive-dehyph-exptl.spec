Name:		texlive-dehyph-exptl
Version:	70233
Release:	1
Summary:	Experimental hyphenation patterns for the German language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/dehyph-exptl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dehyph-exptl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
The package provides experimental hyphenation patterns for the
German language, covering both traditional and reformed
orthography. The patterns can be used with packages Babel and
hyphsubst.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dehyph-exptl
%_texmf_language_dat_d/dehyph-exptl
%_texmf_language_def_d/dehyph-exptl
%_texmf_language_lua_d/dehyph-exptl
%doc %{_texmfdistdir}/doc/generic/dehyph-exptl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

cd tex/generic/dehyph-exptl
DEHYPHT="`ls dehypht-x-*.tex |head -n1`"
TVERSION="`echo $DEHYPHT |sed -e 's,^dehypht-x-,,;s,\.tex,,'`"
DEHYPHN="`ls dehyphn-x-*.tex |head -n1`"
NVERSION="`echo $DEHYPHN |sed -e 's,^dehyphn-x-,,;s,\.tex,,'`"
cd -
if ! echo $TVERSION |grep -qE '^[0-9][0-9][0-9][0-9]-[01][0-9]-[0-3][0-9]$'; then
	echo "Version detection failed, please fix the spec"
	exit 1
fi
if ! echo $NVERSION |grep -qE '^[0-9][0-9][0-9][0-9]-[01][0-9]-[0-3][0-9]$'; then
	echo "Version detection failed, please fix the spec"
	exit 1
fi

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/dehyph-exptl <<EOF
\%% from dehyph-exptl:
german-x-$TVERSION $DEHYPHT
=german-x-latest
ngerman-x-$NVERSION $DEHYPHN
=ngerman-x-latest
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/dehyph-exptl
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/dehyph-exptl <<EOF
\%% from dehyph-exptl:
\addlanguage{german-x-$TVERSION}{$DEHYPHT}{}{2}{2}
\addlanguage{german-x-latest}{$DEHYPHT}{}{2}{2}
\addlanguage{ngerman-x-$NVERSION}{$DEHYPHN}{}{2}{2}
\addlanguage{ngerman-x-latest}{$DEHYPHN}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/dehyph-exptl
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/dehyph-exptl <<EOF
-- from dehyph-exptl:
	['german-x-$TVERSION'] = {
		loader = '$DEHYPHT',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'german-x-latest' },
		patterns = 'hyph-de-1901.pat.txt',
		hyphenation = 'hyph-de-1901.hyp.txt',
	},
	['ngerman-x-$NVERSION'] = {
		loader = '$DEHYPHN',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'ngerman-x-latest' },
		patterns = 'hyph-de-1996.pat.txt',
		hyphenation = 'hyph-de-1996.hyp.txt',
	},
EOF
