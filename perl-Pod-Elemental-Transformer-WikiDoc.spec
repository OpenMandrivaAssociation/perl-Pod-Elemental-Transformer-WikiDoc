%define upstream_name    Pod-Elemental-Transformer-WikiDoc
%define upstream_version 0.093001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A transformer to replace "wikidoc" data regions with Pod5 elements
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Pod::Elemental)
BuildRequires: perl(Pod::WikiDoc)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


