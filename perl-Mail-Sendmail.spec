%include	/usr/lib/rpm/macros.perl
Summary:	Mail-Sendmail perl module
Summary(pl):	Modu³ perla Mail-Sendmail
Name:		perl-Mail-Sendmail
Version:	0.77
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/Mail-Sendmail-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail-Sendmail is a simple platform independent mailer.

%description -l pl
Mail-Sendmail to prosty, niezale¿ny od platformy modu³ do wysy³ania
poczty.

%prep
%setup -q -n Mail-Sendmail-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README Todo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Mail/Sendmail.pm
%{_mandir}/man3/*
