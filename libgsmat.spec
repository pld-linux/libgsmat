Summary:	An implementation of GSM 07.07
Summary(pl.UTF-8):	Implementacja standardu GSM 07.07
Name:		libgsmat
Version:	0.0.2
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5d2458d8521e6b2e664ea7570964cf5c
Patch0:		%{name}-install.patch
# from bristuff-*.tar.gz 
URL:		http://212.91.251.199/~junghanns.net/downloads/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgsmat provides an implementation of GSM 07.07.

%description -l pl.UTF-8
libgsmat udostępnia implementację GSM 07.07

%package devel
Summary:	Header files for libgsmat library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgsmat
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgsmat library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgsmat.

%package static
Summary:	Static libgsmat library
Summary(pl.UTF-8):	Statyczna biblioteka libgsmat
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgsmat library.

%description static -l pl.UTF-8
Statyczna biblioteka libgsmat.

%prep
%setup -q
%patch0 -p1
chmod u+x mkdep

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

install %{name}.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
