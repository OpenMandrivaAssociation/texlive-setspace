# revision 24881
# category Package
# catalog-ctan /macros/latex/contrib/setspace
# catalog-date 2011-12-19 12:40:22 +0100
# catalog-license lppl1.3
# catalog-version 6.7a
Name:		texlive-setspace
Version:	6.7a
Release:	1
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/setspace/setspace.sty
%doc %{_texmfdistdir}/doc/latex/setspace/README
%doc %{_texmfdistdir}/doc/latex/setspace/setspace-test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
