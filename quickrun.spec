Summary:	Quickrun - a very simple command launcher
Summary(pl.UTF-8):	Quickrun - bardzo prosty wykonawca poleceń
Name:		quickrun
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://mbox2mysql.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	57edc8c82e84bdabdd02527fd1238d47
URL:		http://mbox2mysql.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quickrun is a very simple command launcher aimed for use with window
managers like Fluxbox and Blackbox, though it also works perfectly
well with Enlightenment, KDE, and others. Its features include a
history list and filename/command completion. It is not a dockable
applet, but instead requires a keybinding (shortcut) to be set in
order to use it.

%description -l pl.UTF-8
Quickrun jest bardzo prostym wykonawcą poleceń przeznaczonym do
współpracy z takimi zarządcami okien, jak Fluxbox i Blackbox. Jednakże
współpracuje on również świetnie z Enlightenmentem, KDE i innymi.
Obsługuje on historię poleceń oraz dopełnianie nazw plików i poleceń.
Nie jest to dokowalny aplet, ale wymaga do używania przypisania mu
określonej kombinacji klawiszy (skrótu).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install quickrun $RPM_BUILD_ROOT%{_bindir}
install doc/quickrun.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/quickrun*
