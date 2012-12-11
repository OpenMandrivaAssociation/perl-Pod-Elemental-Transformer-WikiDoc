%define upstream_name    Pod-Elemental-Transformer-WikiDoc
%define upstream_version 0.093001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A transformer to replace "wikidoc" data regions with Pod5 elements
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(Pod::WikiDoc)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
A transformer to replace "wikidoc" data regions with Pod5 elements

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.93.1-2mdv2011.0
+ Revision: 655169
- rebuild for updated spec-helper

* Thu Nov 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.1-1mdv2011.0
+ Revision: 467465
- import perl-Pod-Elemental-Transformer-WikiDoc


* Thu Nov 19 2009 cpan2dist 0.093001-1mdv
- initial mdv release, generated with cpan2dist
