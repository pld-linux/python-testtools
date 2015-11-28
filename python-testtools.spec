#
# Conditional build:
%bcond_without	doc	# HTML (sphinx-based) documentation
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform tests

Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Name:		python-testtools
Version:	0.9.34
Release:	3
License:	MIT
Group:		Development/Tools
Source0:	https://pypi.python.org/packages/source/t/testtools/testtools-%{version}.tar.gz
# Source0-md5:	51d37e7376a70cee40cf17b44889fc88
URL:		https://launchpad.net/testtools
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%if %{with tests}
BuildRequires:	python-devel-tools
BuildRequires:	python-extras
BuildRequires:	python-mimeparse
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel
%if %{with tests}
BuildRequires:	python3-devel-tools
BuildRequires:	python3-extras
BuildRequires:	python3-mimeparse
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -l pl.UTF-8
testtools to zestaw rozszerzeń szkieletu testów jednostkowych z
biblioteki standardowej Pythona.

%package -n python3-testtools
Summary:	Extensions to the Python unit testing framework
Summary(pl.UTF-8):	Rozszerzenie szkieletu testów jednostkowych Pythona
Group:		Development/Tools
Requires:	python3-extras

%description -n python3-testtools
testtools is a set of extensions to the Python standard library's unit
testing framework.

%description -n python3-testtools -l pl.UTF-8
testtools to zestaw rozszerzeń szkieletu testów jednostkowych z
biblioteki standardowej Pythona.

%package doc
Summary:	Documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja do pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains HTML documentation for %{name}.

%description doc -l pl.UTF-8
Dokumentacja HTML do pakietu %{name}.

%prep
%setup -q -n testtools-%{version}

%build
%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	%{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	%{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testtools/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testtools/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py_sitescriptdir}/testtools
%{py_sitescriptdir}/testtools/*.py[co]
%dir %{py_sitescriptdir}/testtools/matchers
%{py_sitescriptdir}/testtools/matchers/*.py[co]
%dir %{py_sitescriptdir}/testtools/testresult
%{py_sitescriptdir}/testtools/testresult/*.py[co]
%{py_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-testtools
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%dir %{py3_sitescriptdir}/testtools
%{py3_sitescriptdir}/testtools/*.py
%{py3_sitescriptdir}/testtools/__pycache__
%dir %{py3_sitescriptdir}/testtools/matchers
%{py3_sitescriptdir}/testtools/matchers/*.py
%{py3_sitescriptdir}/testtools/matchers/__pycache__
%dir %{py3_sitescriptdir}/testtools/testresult
%{py3_sitescriptdir}/testtools/testresult/*.py
%{py3_sitescriptdir}/testtools/testresult/__pycache__
%{py3_sitescriptdir}/testtools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
