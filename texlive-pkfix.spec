# revision 26032
# category Package
# catalog-ctan /support/pkfix/pkfix.pl
# catalog-date 2012-04-18 16:26:37 +0200
# catalog-license lppl1.3
# catalog-version 1.7
Name:		texlive-pkfix
Version:	1.7
Release:	6
Summary:	Replace pk fonts in PostScript with Type 1 fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pkfix/pkfix.pl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkfix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pkfix.bin = %{EVRD}

%description
The perl script pkfix looks for DVIPSBitmapFont comments in
PostScript files, generated by 'not too old' dvips, and
replaces them by type 1 versions of the fonts, if possible.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-1
+ Revision: 812778
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 754912
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719265
- texlive-pkfix
- texlive-pkfix
- texlive-pkfix
- texlive-pkfix

