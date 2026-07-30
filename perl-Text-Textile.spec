%define upstream_name    Text-Textile
%define upstream_version 2.13

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


