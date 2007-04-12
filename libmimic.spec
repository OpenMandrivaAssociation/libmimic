%define	name    libmimic
%define	version 1.0.4
%define	release %mkrel 3

Summary:	Audio/Video Conference software for Instant Messengers
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://sourceforge.net/projects/farsight/
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/farsight/%{name}-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n %{name}-devel
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{name}-devel
Headers of %{name} for development.


%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig


%files -n %{name}
%defattr(-,root,root)
%{_libdir}/libmimic.so.0
%{_libdir}/libmimic.so.0.0.1

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/mimic.h
%{_libdir}/libmimic.a
%{_libdir}/libmimic.la
%{_libdir}/libmimic.so
%{_libdir}/pkgconfig/libmimic.pc

