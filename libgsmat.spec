Summary:	An implementation of GSM 07.07
Summary(pl.UTF-8):	Implementacja standardu GSM 07.07
Name:		libgsmat
Version:	0.0.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://212.91.251.199/~junghanns.net/downloads/bristuff-0.4.0-RC3b.tar.gz
# Source0-md5:	ac9b76a09b4ea1a70f243c31d817a393
Patch0:		%{name}-install.patch
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
%setup -q -n bristuff-0.4.0-RC3b
cd %{name}-%{version}
%patch -P0 -p1

chmod u+x mkdep

%build
cd %{name}-%{version}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd %{name}-%{version}
cp -a libgsmat.so* $RPM_BUILD_ROOT%{_libdir}
install libgsmat.a $RPM_BUILD_ROOT%{_libdir}
install libgsmat.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{README,TODO}
%attr(755,root,root) %{_libdir}/libgsmat.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsmat.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsmat.so
%{_includedir}/%{name}.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgsmat.a
