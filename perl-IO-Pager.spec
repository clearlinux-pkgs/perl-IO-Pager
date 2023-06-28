#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-IO-Pager
Version  : 2.10
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/IO-Pager-2.10.tgz
Source0  : https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/IO-Pager-2.10.tgz
Summary  : 'Select a pager (possibly perl-based) & pipe it text if a TTY'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-IO-Pager-bin = %{version}-%{release}
Requires: perl-IO-Pager-man = %{version}-%{release}
Requires: perl-IO-Pager-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)
BuildRequires : perl(Term::ReadKey)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IO::Pager & IO::Pager::Perl
=====================
IO::Pager - Select a pager and pipe text to it if destination is a TTY
IO::Pager::Perl - A pure perl pager engine

%package bin
Summary: bin components for the perl-IO-Pager package.
Group: Binaries

%description bin
bin components for the perl-IO-Pager package.


%package dev
Summary: dev components for the perl-IO-Pager package.
Group: Development
Requires: perl-IO-Pager-bin = %{version}-%{release}
Provides: perl-IO-Pager-devel = %{version}-%{release}
Requires: perl-IO-Pager = %{version}-%{release}

%description dev
dev components for the perl-IO-Pager package.


%package man
Summary: man components for the perl-IO-Pager package.
Group: Default

%description man
man components for the perl-IO-Pager package.


%package perl
Summary: perl components for the perl-IO-Pager package.
Group: Default
Requires: perl-IO-Pager = %{version}-%{release}

%description perl
perl components for the perl-IO-Pager package.


%prep
%setup -q -n IO-Pager-2.10
cd %{_builddir}/IO-Pager-2.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tp

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Pager.3
/usr/share/man/man3/IO::Pager::Buffered.3
/usr/share/man/man3/IO::Pager::Page.3
/usr/share/man/man3/IO::Pager::Perl.3
/usr/share/man/man3/IO::Pager::Unbuffered.3
/usr/share/man/man3/IO::Pager::less.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tp.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
