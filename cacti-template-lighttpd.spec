%define		plugin lighttpd
%define		php_min_version 5.0.0
Summary:	Template for Cacti - Lighttpd stats
Name:		cacti-template-%{plugin}
Version:	1.0
Release:	9
License:	GPL v2
Group:		Applications/WWW
# http://forums.cacti.net/download.php?id=8273
Source0:	lighttpd_stats_%{version}.tar.gz
# Source0-md5:	09aa6716901e08301517004de099d240
Patch0:		fixes.patch
URL:		http://forums.cacti.net/viewtopic.php?t=19676
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti >= 0.8.7e-8
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Obsoletes:	cacti-plugin-lighttpd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
This package provides a script server script and cacti templates for
graphing statistics for a lighttpd webserver.

%prep
%setup -q -n lighttpd_stats_%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
cp -p *.xml $RPM_BUILD_ROOT%{resourcedir}
install -p *.php $RPM_BUILD_ROOT%{scriptsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%cacti_import_template %{resourcedir}/cacti_host_template_webserver_lighttpd.xml

%files
%defattr(644,root,root,755)
%doc README INSTALL CHANGELOG
%attr(755,root,root) %{scriptsdir}/ss_lighttpd_stats.php
%{resourcedir}/cacti_host_template_webserver_lighttpd.xml
