%define prj Horde_SessionObjects

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-sessionobjects
Version:       0.0.2
Release:       4
Summary:       Horde Session Storage API
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      php-pear
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Horde_SessionObjects:: class provides a way for storing data (usually,
but not necessarily, objects) in the current user's session.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{peardir}/Horde/SessionObjects.php



%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564099
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2010.1
+ Revision: 523008
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear

* Thu Feb 25 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 510889
- removed BuildRequires: horde-framework
- added BuildRequires: horde-framework

* Thu Feb 25 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 510867
- replaced PreRqu with Requires(pre)
- removed BuildRequires: horde-framework
- import horde-sessionobjects


