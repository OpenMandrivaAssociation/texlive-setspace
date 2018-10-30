# revision 24881
# category Package
# catalog-ctan /macros/latex/contrib/setspace
# catalog-date 2011-12-19 12:40:22 +0100
# catalog-license lppl1.3
# catalog-version 6.7a
Name:		texlive-setspace
Version:	6.7a
Release:	11
Summary:	Set space between lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/setspace
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setspace.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setspace.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides support for setting the spacing between lines in a
document. Package options include singlespacing,
onehalfspacing, and doublespacing. Alternatively the spacing
can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size
spacings also available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/setspace/setspace.sty
%doc %{_texmfdistdir}/doc/latex/setspace/README
%doc %{_texmfdistdir}/doc/latex/setspace/setspace-test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 6.7a-2
+ Revision: 755915
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 6.7a-1
+ Revision: 745307
- texlive-setspace

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 6.7-1
+ Revision: 719513
- texlive-setspace
- texlive-setspace
- texlive-setspace
- texlive-setspace

