%include	/usr/lib/rpm/macros.perl
Summary:	Mail-Sendmail perl module
Summary(pl):	Modu³ perla Mail-Sendmail
Name:		perl-Mail-Sendmail
Version:	0.77
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/Mail-Sendmail-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail-Sendmail is a simple platform independent mailer.

%description -l pl
Mail-Sendmail to prosty, niezale¿ny od platformy modu³ do wysy³ania poczty.

%prep
%setup -q -n Mail-Sendmail-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Mail/Sendmail
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README Todo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,Todo}.gz

%{perl_sitelib}/Mail/Sendmail.pm
%{perl_sitearch}/auto/Mail/Sendmail

%{_mandir}/man3/*
