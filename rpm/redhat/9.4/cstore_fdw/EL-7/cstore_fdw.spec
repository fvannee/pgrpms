%global pgmajorversion 94
%global pginstdir /usr/pgsql-9.4
%global sname cstore_fdw

Summary:	Columnar store extension for PostgreSQL
Name:		%{sname}_%{pgmajorversion}
Version:	1.1
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/citusdata/%{sname}/archive/v%{version}.tar.gz
Patch0:		%{sname}-makefile.patch
URL:		http://citusdata.github.io/cstore_fdw/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	protobuf-c-devel

%description
cstore_fdw is column-oriented store available for PostgreSQL. Using it will 
let you:
    Leverage typical analytics benefits of columnar stores
    Deploy on stock PostgreSQL or scale-out PostgreSQL (CitusDB)

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} install DESTDIR=%{buildroot}
# Let's also install documentation:
%{__mkdir} -p %{buildroot}%{pginstdir}/share/extension
%{__cp} README.md %{buildroot}%{pginstdir}/share/extension/README-cstore_fdw.md

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{pginstdir}/share/extension/README-%{sname}.md
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}-*.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Fri Aug 29 2014 - Devrim GUNDUZ <devrim@gunduz.org> 1.1-1
- Initial RPM packaging for PostgreSQL RPM Repository
