Name: hunspell-uk
Summary: Ukrainian hunspell dictionaries
Version: 1.6.5
Release: 5%{?dist}
Source: http://downloads.sourceforge.net/ispell-uk/spell-uk-%{version}.tgz
Group: Applications/Text
URL: http://sourceforge.net/projects/ispell-uk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Ukrainian hunspell dictionaries.

%prep
%setup -q -n spell-uk-%{version}

%build
make myspell

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ./dist/myspell-uk-%{version}/uk_UA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ./dist/myspell-uk-%{version}/uk_UA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ./src/myspell/README_uk_UA.txt README README.uk COPYING.GPL COPYING.LGPL Copyright
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.6.5-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 22 2011 Caolán McNamara <caolanm@redhat.com> - 1.6.5-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 18 2009 Caolán McNamara <caolanm@redhat.com> - 1.6.0-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.7-1
- latest version

* Tue Sep 30 2008 Caolán McNamara <caolanm@redhat.com> - 1.5.5-1
- latest version

* Tue Sep 16 2008 Caolán McNamara <caolanm@redhat.com> - 1.5.0-2
- fixup extra Source lines

* Mon Sep 15 2008 Caolán McNamara <caolanm@redhat.com> - 1.5.0-1
- initial version
