%define upstream_name    Text-Textile
%define upstream_version 2.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Transforms text in Textile format to HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

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


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 2.120.0-2mdv2011.0
+ Revision: 654333
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.120.0-1mdv2011.0
+ Revision: 471081
- import perl-Text-Textile


* Sun Nov 29 2009 cpan2dist 2.12-1mdv
- initial mdv release, generated with cpan2dist
