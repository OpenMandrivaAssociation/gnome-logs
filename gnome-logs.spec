%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		gnome-logs
Version:	3.30.0
Release:	1
Summary:	GNOME Log Viewer
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.9.6
BuildRequires:	pkgconfig(systemd)
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

%find_lang %{name}  --with-gnome

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/%{name}
#%{_libdir}/%{name}
#{py3_puresitedir}/gnomemusic
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/glib-2.0/schemas/*.xml
#{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
#{_datadir}/appdata/org.gnome.Logs.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Logs.service
