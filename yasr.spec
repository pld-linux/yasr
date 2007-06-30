Summary:	Yet another screen reader
Summary(pl.UTF-8):	Jeszcze jeden screen reader
Name:		yasr
Version:	0.6.7
Release:	1	
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/yasr/%{name}-%{version}.tar.gz
# Source0-md5:	c7c6191f1d7413317924e580809817dc
Patch0:		%{name}-am.patch
Patch1:		%{name}-conf_settings.patch
Patch2:		%{name}-conf_path.patch
URL:		http://yasr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasr is a general-purpose console screen reader for GNU/Linux and
other Unix-like operating systems. The name "yasr" is an acronym that
can stand for either "Yet Another Screen Reader" or "Your All-purpose
Screen Reader" (take your pick; it doesn't really matter much). It
supports a number of synthesizers, although interfacing issues exist
with some of them at the moment. Currently, yasr attempts to support
the Speak-out, DEC-talk, BNS, Apollo, and DoubleTalk. It is also able
to communicate with Emacspeak servers and can thus be used with
synthesizers not directly supported, such as Festival Lite (via
eflite) or FreeTTS. It is small enough to fit on a root disk if
necessary (provided an Emacspeak server is not needed, of course). It
is written in C and works by opening a pseudo-terminal and running a
shell, intercepting all input and output. It looks at the escape
sequences being sent and maintains a virtual "window" containing what
it believes to be on the screen. It thus does not use any features
specific to Linux and can be ported to other Unix-like operating
systems without too much trouble.

#%%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS ChangeLog NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yasr.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
