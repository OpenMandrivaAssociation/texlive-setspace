# revision 21104
# category Package
# catalog-ctan /macros/latex/contrib/setspace/setspace.sty
# catalog-date 2011-01-17 14:36:46 +0100
# catalog-license other-free
# catalog-version 6.7
Name:		texlive-setspace
Version:	6.7
Release:	1
Summary:	Set space between lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/setspace/setspace.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/setspace.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Provides support for setting the spacing between lines in a
document. Package options include singlespacing,
onehalfspacing, and doublespacing. Alternatively the spacing
can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size
spacings also available.

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
%{_texmfdistdir}/tex/latex/setspace/setspace.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
