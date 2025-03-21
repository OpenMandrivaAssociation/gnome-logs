%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		gnome-logs
Version:	45.0
Release:	3
Summary:	GNOME Log Viewer
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Logs
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(systemd)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libadwaita-1)
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
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

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
%{_datadir}/metainfo/org.gnome.Logs.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Logs.service
#{_datadir}/gnome-logs/gl-style.css
