%define	major	0
%define libname	%mklibname mimic %{major}
%define devname	%mklibname -d mimic

Summary:	Audio/Video Conference software for Instant Messengers
Name:		libmimic
Version:	1.0.4
Release:	19
License:	LGPLv2+
Url:		http://sourceforge.net/projects/farsight/
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/farsight/%{name}-%{version}.tar.gz 
Patch0:		%{name}-1.0.4-fix-underlinking.patch
BuildRequires:	pkgconfig(glib-2.0)

%description
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Audio/Video Conference software for Instant Messengers

%description -n %{libname}
Audio/Video Conference software for Instant Messengers.
It aims to provide Audio/Video conferencing for as many 
Instant Messengers as possible through a modular design.

%package -n	%{devname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmimic.so.%{major}*

%files -n %{devname}
%{_includedir}/mimic.h
%{_libdir}/libmimic.so
%{_libdir}/pkgconfig/libmimic.pc

