Summary:	A PostgreSQL SQL syntax beautifier
Name:		pgFormatter
Version:	2.0
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/darold/%{name}/archive/v%{version}.tar.gz
URL:		https://github.com/darold/%{name}/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
A PostgreSQL SQL syntax beautifier that can work as a console program
or as a CGI. Download from https://sourceforge.net/p/pgformatter/ and
demo site at http://sqlformat.darold.net/

%prep
%setup -q
%{__perl} Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/pg_format
%{_mandir}/man1/pg_format.1.gz
%{_mandir}/man3/pgFormatter*.gz
%{perl_vendorlib}/%{name}/*.pm
%{perl_vendorlib}/regress_test.pl

%changelog
* Mon Jun 5 2017 - Devrim Gündüz <devrim@gunduz.org> 2.0-1
- Update to 2.0

* Mon Jan 23 2017 - Devrim Gündüz <devrim@gunduz.org> 1.6-1
- Update to 1.6

* Sun Oct 18 2015 - Devrim Gündüz <devrim@gunduz.org> 1.5-1
- Update to 1.5

* Sun Apr 19 2015 - Devrim Gündüz <devrim@gunduz.org> 1.4-1
- Update to 1.4

* Sun Mar 29 2015 - Devrim Gündüz <devrim@gunduz.org> 1.3-1
- Initial RPM packaging for PostgreSQL RPM Repository