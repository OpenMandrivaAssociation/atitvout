Summary:	Config tool for ATI Rage Mobility TV-OUT
Name: 		atitvout
Version: 	0.4
Release:	 %mkrel 3
Group: 		System/Configuration/Hardware
License: 	GPL
Source: 	%name-%version.tar.bz2
Patch:		atitvout-0.4-cflags.patch.bz2
URL: 		http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/
ExclusiveArch: %ix86
BuildRoot: 	%_tmppath/%name-buildroot

%description
TV-OUT support tool for ATI Rage Mobility graphic cards.
Install it ONLY if you have an ATI Rage Mobility graphic card

%prep
%setup -q -n atitvout
%patch0 -p0

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT%_sbindir
install atitvout $RPM_BUILD_ROOT%_sbindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%_sbindir/atitvout
%defattr(644,root,root,755)
%doc COPYING README HARDWARE

