Name:		texlive-kotex-oblivoir
Version:	2.1.8
Release:	1
Summary:	A LaTeX document class for typesetting Korean documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/kotex-oblivoir
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-oblivoir.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-oblivoir.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-memoir
Requires:	texlive-kotex-utf

%description
The class is based on memoir, and is adapted to typesetting
Korean documents. The bundle (of class and associated packages)
belongs to the ko.TeX bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kotex-oblivoir
%doc %{_texmfdistdir}/doc/latex/kotex-oblivoir

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
