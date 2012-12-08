%define	name    libmimic
%define	version 1.0.4
%define	release %mkrel 7
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
Patch0:		%{name}-1.0.4-fix-underlinking.patch
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
%patch0 -p1 -b .undlink

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libmimic.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/mimic.h
%{_libdir}/libmimic.a
%{_libdir}/libmimic.so
%{_libdir}/pkgconfig/libmimic.pc



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-7mdv2011.0
+ Revision: 620153
- the mass rebuild of 2010.0 packages

* Wed Jun 10 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 1.0.4-6mdv2010.0
+ Revision: 384962
- fix underlinking

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.4-3mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + G√∂tz Waschk <waschk@mandriva.org>
    - fix license

* Thu Sep 06 2007 G√∂tz Waschk <waschk@mandriva.org> 1.0.4-3mdv2008.0
+ Revision: 80957
- fix buildrequires
- libify the package


* Thu Mar 23 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.4-3mdk
- Fix File section

* Thu Mar 23 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.4-2mdk
- Fix sub-packaging naming

* Thu Mar 23 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0.4-1mdk
- First Mandriva release

