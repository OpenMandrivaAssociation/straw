%define	name	straw
%define version 0.27
%define release %mkrel 8
%define fname %name-%{version}
%define	Summary	RSS feed agregator for Gnome

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/News
URL:		http://www.gnome.org/projects/straw/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/straw/%{fname}.tar.bz2
Source1:	%name-icons.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel >= 2.3
BuildRequires:	pygtk2.0-libglade >= 2.6
BuildRequires:	pygtk2.0-devel >= 2.6
BuildRequires:	gnome-python-canvas
BuildRequires:	gnome-python-gtkhtml2
BuildRequires:	gnome-python-gnomevfs
BuildRequires:	gnome-python-gconf
BuildRequires:	adns-python 
BuildRequires:	intltool
BuildRequires:	dbus-python
BuildRequires:	desktop-file-utils
Requires:	pygtk2.0-libglade >= 2.6
Requires:	gnome-python-canvas
Requires:	gnome-python-gtkhtml2
Requires:	gnome-python-gnomevfs
Requires:	gnome-python-gconf
Requires:	dbus-python
Requires:	adns-python 
#gw we only need this for backward compatibility
Requires:	egenix-mx-base
BuildArch: noarch

%description
Straw is a desktop news aggregator for the GNOME environment. Its aim is to be
a faster, easier and more accessible way to read news and blogs than the 
traditional browser.

%prep
%setup -q -n %fname -a1

%build
python setup.py build

%install
rm -rf ${RPM_BUILD_ROOT}
python setup.py install --prefix=%_prefix --root=%buildroot --disable-modules-check
%find_lang %name
rm -rf %buildroot%_sysconfdir/gconf/gconf.xml.defaults

chmod 0644 NEWS LICENSE README TODO


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network;News" \
  --add-category="X-MandrivaLinux-Internet-News" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %{name}
%endif

%preun
%preun_uninstall_gconf_schemas %{name}


%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files -f straw.lang
%defattr(-,root,root)
%doc NEWS LICENSE README TODO

%{_bindir}/*
%_sysconfdir/gconf/schemas/%name.schemas
%{_datadir}/applications/%name.desktop
%{_datadir}/%name
%{py_puresitedir}/%name
%{py_puresitedir}/*.egg-info
%{_iconsdir}/*/%name.png
%{_iconsdir}/%name.png
%{_datadir}/pixmaps/%name.png


