#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Typerep - library for runtime types
Summary(pl.UTF-8):	Typerep - biblioteka do typów uruchomieniowych
Name:		ocaml-typerep
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/typerep/tags
Source0:	https://github.com/janestreet/typerep/archive/v%{version}/typerep-%{version}.tar.gz
# Source0-md5:	d95f944090434bc998f4209c8725e5ba
URL:		https://github.com/janestreet/typerep
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Typerep is a library for runtime types.

This package contains files needed to run bytecode executables using
typerep library.

%description -l pl.UTF-8
Typerep to biblioteka do typów uruchomieniowych.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki typerep.

%package devel
Summary:	Typerep - library for runtime types - development part
Summary(pl.UTF-8):	Typerep - biblioteka do typów uruchomieniowych - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
typerep library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki typerep.

%prep
%setup -q -n typerep-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/typerep/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/typerep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml/typerep
%{_libdir}/ocaml/typerep/META
%{_libdir}/ocaml/typerep/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/typerep/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/typerep/*.cmi
%{_libdir}/ocaml/typerep/*.cmt
%{_libdir}/ocaml/typerep/*.cmti
%{_libdir}/ocaml/typerep/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/typerep/typerep_lib.a
%{_libdir}/ocaml/typerep/*.cmx
%{_libdir}/ocaml/typerep/*.cmxa
%endif
%{_libdir}/ocaml/typerep/dune-package
%{_libdir}/ocaml/typerep/opam
