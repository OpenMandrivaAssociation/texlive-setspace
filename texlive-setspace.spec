%global tl_name setspace
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.7b
Release:	%{tl_revision}.1
Summary:	Set space between lines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/setspace
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/setspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/setspace.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides support for setting the spacing between lines in a document.
Package options include singlespacing, onehalfspacing, and
doublespacing. Alternatively the spacing can be changed as required with
the \singlespacing, \onehalfspacing, and \doublespacing commands. Other
size spacings also available.

