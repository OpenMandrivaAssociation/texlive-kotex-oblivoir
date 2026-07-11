%global tl_name kotex-oblivoir
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5
Release:	%{tl_revision}.1
Summary:	A LaTeX document class for typesetting Korean documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/kotex-oblivoir
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-oblivoir.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-oblivoir.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kotex-utf)
Requires:	texlive(memoir)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is based on memoir, and is adapted to typesetting Korean
documents. The bundle (of class and associated packages) belongs to the
ko.TeX bundle. It depends on memoir and kotex-utf to function.

