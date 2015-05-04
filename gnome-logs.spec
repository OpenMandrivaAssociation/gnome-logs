%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		gnome-logs
Version:	3.16.1
Release:	1
Summary:	GNOME Log Viewer
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.9.6
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	appdata-tools
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
Requires:	gsettings-desktop-schemas

%description
Logs makes it easy to view and filter log messages and events. Filter
logs by category and importance to get the information you want. Use
the integrated search to get more relevant results.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%find_lang %{name} 

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/%{name}
#%{_libdir}/%{name}
#{py3_puresitedir}/gnomemusic
%{_datadir}/applications/org.gnome.Logs.desktop
#{_datadir}/glib-2.0/schemas/*.xml
#{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_datadir}/appdata/org.gnome.Logs.appdata.xml
%{_mandir}//man1/%{name}.1*
%{_datadir}/dbus-1/services/org.gnome.Logs.service


%changelog
* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796286
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 742430
- Second Mageia 5 Mass Rebuild

* Mon Oct 13 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738331
- new version 3.14.1

* Mon Sep 29 2014 wally <wally> 3.14.0-1.mga5
+ Revision: 731713
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679730
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676947
- new version 3.13.92

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670519
- new version 3.13.91

* Mon Aug 18 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665074
- new version 3.13.90

* Tue Jul 22 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655392
- new version 3.13.4

* Mon Jun 23 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639119
- new version 3.13.3

* Fri May 30 2014 ovitters <ovitters> 3.13.2-1.mga5
+ Revision: 627869
- new version 3.13.2

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622354
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614107
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608093
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604588
- new version 3.11.92

* Tue Mar 04 2014 fwang <fwang> 3.11.91-1.mga5
+ Revision: 599256
- update file list

  + ovitters <ovitters>
    - new version 3.11.91

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594169
- new version 3.11.90
- dropped merged patch 1

* Thu Feb 06 2014 ovitters <ovitters> 3.11.5-1.mga5
+ Revision: 583976
- add patch to fix desktop translation
- new version 3.11.5

* Wed Nov 20 2013 ovitters <ovitters> 3.11.2-1.mga4
+ Revision: 551969
- BR appdata-tools
- new version 3.11.2

* Wed Nov 06 2013 ovitters <ovitters> 3.11.1-1.mga4
+ Revision: 549832
- fix description
- imported package gnome-logs

