#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
			# need network connection
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Sendmail
Summary:	Mail::Sendmail perl module
Summary(pl):	Modu³ perla Mail::Sendmail
Name:		perl-Mail-Sendmail
Version:	0.79
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	038f261afd091d8fad347d6c66d2833d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::Sendmail is a simple platform independent mailer.

%description -l pl
Mail::Sendmail to prosty, niezale¿ny od platformy modu³ do wysy³ania
poczty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/Mail/Sendmail.pm
%{_mandir}/man3/*
