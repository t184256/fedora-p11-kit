Name:           p11-kit
Version:        0.14
Release:        1%{?dist}
Summary:        Library for loading and sharing PKCS#11 modules

License:        BSD
URL:            http://p11-glue.freedesktop.org/p11-kit.html
Source0:        http://p11-glue.freedesktop.org/releases/p11-kit-%{version}.tar.gz

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/modules

rm $RPM_BUILD_ROOT%{_libdir}/*.la
# Install the example conf with %%doc instead
rm $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/pkcs11.conf.example


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING NEWS README
%doc p11-kit/pkcs11.conf.example
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules
%{_bindir}/p11-kit
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %{_datadir}/gtk-doc/


%changelog
* Mon Sep 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.14-1
- Update to 0.14

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Kalev Lember <kalevlember@gmail.com> - 0.13-1
- Update to 0.13

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 0.12-1
- Update to 0.12
- Run self tests in %%check

* Sat Feb 11 2012 Kalev Lember <kalevlember@gmail.com> - 0.11-1
- Update to 0.11

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.9-1
- Update to 0.9

* Wed Oct 26 2011 Kalev Lember <kalevlember@gmail.com> - 0.8-1
- Update to 0.8

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> - 0.6-1
- Update to 0.6

* Sun Sep 04 2011 Kalev Lember <kalevlember@gmail.com> - 0.5-1
- Update to 0.5

* Sun Aug 21 2011 Kalev Lember <kalevlember@gmail.com> - 0.4-1
- Update to 0.4
- Install the example config file to documentation directory

* Wed Aug 17 2011 Kalev Lember <kalevlember@gmail.com> - 0.3-2
- Tighten -devel subpackage deps (#725905)

* Fri Jul 29 2011 Kalev Lember <kalevlember@gmail.com> - 0.3-1
- Update to 0.3
- Upstream rewrote the ASL 2.0 bits, which makes the whole package
  BSD-licensed

* Tue Jul 12 2011 Kalev Lember <kalevlember@gmail.com> - 0.2-1
- Initial RPM release
