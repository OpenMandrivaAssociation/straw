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
Patch0:		straw-0.27-fix-build.patch
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
%patch0 -p0

%build
python setup.py build -v

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




%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.27-8mdv2011.0
+ Revision: 677872
- fix build
- rebuild to add gconftool as req

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.27-7mdv2011.0
+ Revision: 599669
- fix install

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.27-6mdv2010.0
+ Revision: 445264
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.27-5mdv2009.1
+ Revision: 326009
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.27-4mdv2009.0
+ Revision: 261207
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.27-3mdv2009.0
+ Revision: 253571
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.27-1mdv2008.1
+ Revision: 148381
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 20 2007 Pascal Terjan <pterjan@mandriva.org> 0.27-1mdv2008.0
+ Revision: 28775
- 0.27


* Mon Mar 19 2007 Pascal Terjan <pterjan@mandriva.org> 0.26-5mdv2007.1
+ Revision: 146813
- package the .egg-info
- rebuild for python 2.5

* Mon Oct 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.26-4mdv2007.1
+ Revision: 73684
- Import straw

* Mon Oct 30 2006 Götz Waschk <waschk@mandriva.org> 0.26-4mdv2007.1
- remove xvfb build dep
- fix buildrequires

* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.26-3mdv2007.0
- xdg menu
- gconf macros
- fix group
- fix Xvfb path

* Mon Mar 06 2006 Götz Waschk <waschk@mandriva.org> 0.26-2mdk
- oops noarch

* Mon Mar 06 2006 Götz Waschk <waschk@mandriva.org> 0.26-1mdk
- fix preun
- update deps
- new URL
- new version

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.25.1-2mdk
- Rebuild for new python

* Sat Jul 17 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.25.1-1mdk
- New release 0.25.1

* Fri Jul 16 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.25-1mdk
- New release 0.25

* Thu Jul 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.24-2mdk
- readd gconf dependancy
- fix buildrequires

* Thu Jul 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.24-1mdk
- drop gconf dep
- it's now architecture dependant for the notification area applet
- fix source URL
- New release 0.24

* Sun May 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.23-2mdk
- drop py_ver macro
- fix buildrequires

* Thu Apr 29 2004 Götz Waschk <waschk@linux-mandrake.com> 0.23-1mdk
- fix installation
- new version

