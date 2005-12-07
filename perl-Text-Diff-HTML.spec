#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Diff-HTML
Summary:	XHTML format for Text::Diff::Unified
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	0.1
# note if it is "same as perl"
License:	Artistic and GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd8a50dd2f9d90be1f949906441035c1
URL:		http://search.cpan.org/~dwheeler/Text-Diff-HTML-0.04/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
XHTML format for Text::Diff::Unified.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/Text/Diff,%{_mandir}/man3}

install lib/Text/Diff/HTML.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Text/Diff
install blib/libdoc/Text::Diff::HTML.3pm $RPM_BUILD_ROOT%{_mandir}/man3 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Diff/HTML.pm
%{_mandir}/man3/*
