%define	name    libmimic
%define	version 1.0.4
%define	release %mkrel 3
%define major 0
%define libname %mklibname mimic %major
%define develname %mklibname -d mimic

Summary:	Audio/Video Conference software for Instant Messengers
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Url:		http://sourceforge.net/projects/farsight/
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/farsight/%{name}-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel

%description
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n %libname
Group: System/Libraries
Summary:Audio/Video Conference software for Instant Messengers
Obsoletes: libmimic

%description -n %libname
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n %develname
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libmimic.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/mimic.h
%{_libdir}/libmimic.a
%{_libdir}/libmimic.la
%{_libdir}/libmimic.so
%{_libdir}/pkgconfig/libmimic.pc

