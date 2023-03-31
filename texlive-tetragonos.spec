Name:		texlive-tetragonos
Version:	49732
Release:	2
Summary:	Four-Corner codes of Chinese characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tetragonos
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetragonos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetragonos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a XeLaTeX package for mapping Chinese characters to
their codes in the Four-Corner Method.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/tetragonos
%doc %{_texmfdistdir}/doc/xelatex/tetragonos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
