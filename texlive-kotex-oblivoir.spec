# revision 32105
# category Package
# catalog-ctan /language/korean/kotex-oblivoir
# catalog-date 2013-11-03 10:05:42 +0100
# catalog-license lppl
# catalog-version 2.0.0
Name:		texlive-kotex-oblivoir
Version:	2.0.0
Release:	3
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
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/10_5.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/fapapersize.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/hfontsel.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/hfontspec.nanum
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memhangul-common.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memhangul-patch.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memhangul-ucs.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memucs-enumerate.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memucs-gremph.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memucs-interword.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/memucs-setspace.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/nanumfontsel.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/ob-koreanappendix.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/ob-nokoreanappendix.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-ucs/ob-toclof.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/luatexko-xobfont.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/memhangul-x.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/memucs-interword-x.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xetexko-var.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xetexko-xobfont.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xob-amssymb.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xob-dotemph.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xob-hyper.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/memhangul-x/xob-paralist.sty
%{_texmfdistdir}/tex/latex/kotex-oblivoir/oblivoir-base.cls
%{_texmfdistdir}/tex/latex/kotex-oblivoir/oblivoir-xlua.cls
%{_texmfdistdir}/tex/latex/kotex-oblivoir/oblivoir.cls
%{_texmfdistdir}/tex/latex/kotex-oblivoir/xoblivoir.cls
%doc %{_texmfdistdir}/doc/latex/kotex-oblivoir/README
%doc %{_texmfdistdir}/doc/latex/kotex-oblivoir/oblivoir-simpledoc.pdf
%doc %{_texmfdistdir}/doc/latex/kotex-oblivoir/oblivoir-simpledoc.tex
%doc %{_texmfdistdir}/doc/latex/kotex-oblivoir/oblivoir-test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
