%define		plugin lighttpd
Summary:	Plugin for Cacti - Lighttpd stats
Name:		cacti-plugin-%{plugin}
Version:	1.0
Release:	2
License:	GPL v2
Group:		Applications/WWW
# http://forums.cacti.net/download.php?id=8273
Source0:	lighttpd_stats_%{version}.tar.gz
# Source0-md5:	09aa6716901e08301517004de099d240
Patch0:		%{name}.patch
URL:		http://forums.cacti.net/about4028.html
Requires:	cacti >= 0.8.6j
Requires:	cacti-add_template
Requires:	php-common >= 4:5.1
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
cp -a *.xml $RPM_BUILD_ROOT%{resourcedir}
install *.php $RPM_BUILD_ROOT%{scriptsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/cacti-add_template %{resourcedir}/cacti_host_template_webserver_lighttpd.xml

%files
%defattr(644,root,root,755)
%doc README INSTALL CHANGELOG
%attr(755,root,root) %{scriptsdir}/ss_lighttpd_stats.php
%{resourcedir}/cacti_host_template_webserver_lighttpd.xml
