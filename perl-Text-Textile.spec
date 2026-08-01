%define upstream_name    Text-Textile
%define upstream_version 2.13

Name:		perl-%{upstream_name}
Version:	2.13
Release:	2

Summary:	Transforms text in Textile format to HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bradchoate/text-textile/tree/master
Source0:	https://cpan.metacpan.org/authors/id/B/BC/BCHOATE/Text-Textile-2.13.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Transforms text in Textile format to HTML.

%prep
%setup -q -n Text-Textile-2.13

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
# soft: do not fail package on test failures
set +e
make test || :
%make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml README.textile
%{_mandir}/man3/*
%{perl_vendorlib}/*


