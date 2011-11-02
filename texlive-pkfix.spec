Name:		texlive-pkfix
Version:	1.6
Release:	1
Summary:	Replace pk fonts in PostScript with Type 1 fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pkfix/pkfix.pl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-pkfix.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

%description
The perl script pkfix looks for DVIPSBitmapFont comments in
PostScript files, generated by 'not too old' dvips, and
replaces them by type 1 versions of the fonts, if possible.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pkfix
%{_texmfdistdir}/scripts/pkfix/pkfix.pl
%doc %{_texmfdistdir}/doc/support/pkfix/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pkfix/pkfix.pl pkfix
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
