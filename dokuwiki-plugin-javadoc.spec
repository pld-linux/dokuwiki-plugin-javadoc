%define		plugin		javadoc
Summary:	Add Javadoc link capability to dokuwiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20070919
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.doolin-guif.net/wiki/lib/exe/fetch.php?media=plugin:plugin-%{plugin}-1.0.0.zip#/%{plugin}.zip
# Source0-md5:	a6629e93b430f1a38ab4d2623f94f2ca
URL:		http://www.dokuwiki.org/plugin:javadoc
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin allows the editor to create links to a Javadoc page using
the full same of a class or a method, and referring the Javadoc base
URL using an identifier. This allows to easily refer to one or several
Javadoc sites without hard-coding the base URL at each time.

%prep
%setup -qc
mv %{plugin}/* .

version=$(awk -F"'" '/date/&&/=>/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force js/css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
%{plugindir}/images
