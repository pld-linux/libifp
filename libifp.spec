Summary:	iRiver driver library
Summary(pl):	Biblioteka sterownika iRiver
Name:		libifp
Version:	1.0.0.1
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
# Source0-md5:	3b692cc224391b5714f5a8fbb8abf85b
URL:		http://ifp-driver.sourceforge.net/libifp/
BuildRequires:	libusb-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for IRiver's flash-based portable music players

%package devel
Summary:	The files needed for development of applications that use libifp
Group:		Development/Libraries
Requires:	%{name}-%{version}-%{release}

%description devel
Headers and libraries needed for development of applications that use
libifp

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/ifpline
%{_libdir}/libifp.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h
%{_mandir}/man3/*.3*
