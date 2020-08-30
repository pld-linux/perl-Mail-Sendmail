#
# Conditional build:
%bcond_with	tests	# unit tests (need network connection)

%define		pdir	Mail
%define		pnam	Sendmail
Summary:	Mail::Sendmail Perl module
Summary(pl.UTF-8):	Moduł Perla Mail::Sendmail
Name:		perl-Mail-Sendmail
Version:	0.80
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be1d23ebc2edc744ab2457f2086b4e2b
URL:		https://metacpan.org/release/Mail-Sendmail
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::Sendmail is a simple platform independent mailer.

%description -l pl.UTF-8
Mail::Sendmail to prosty, niezależny od platformy moduł do wysyłania
poczty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/Mail/Sendmail.pm
%{_mandir}/man3/Mail::Sendmail.3pm*
