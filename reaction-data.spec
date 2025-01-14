%define		oname	Reaction
%define		gname	reaction

Name:		%{gname}-data
Version:	1.0
Release:	2
Summary:	Data files used to play first-person shooter Reaction
Group:		Games/Arcade
License:	CC-BY-SA 3.0
URL:		https://rq3.com/
Source0:	http://download.rq3.com/%{oname}-%{version}-Linux-i386.tar.gz
Requires:	%{gname}
BuildArch:	noarch

%description
Data files used to play first-person shooter Reaction.

%prep
%setup -q -n %{oname}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_gamesdatadir}/%{gname}/%{gname}
%__cp Boomstick/* %{buildroot}%{_gamesdatadir}/%{gname}/%{gname}/

%clean
%__rm -rf %{buildroot}

%files
%doc %{oname}-license.txt
%{_gamesdatadir}/%{gname}/%{gname}


%changelog
* Mon Apr 02 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0-1
+ Revision: 788818
- imported package reaction-data

