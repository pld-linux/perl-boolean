#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	boolean
Summary:	boolean - Boolean support for Perl
Name:		perl-boolean
Version:	0.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/boolean-%{version}.tar.gz
# Source0-md5:	2a0d94fd6f5e01bac6b48536d3cd7197
URL:		http://search.cpan.org/dist/boolean/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides basic Boolean support, by defining two special
objects: true and false.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
