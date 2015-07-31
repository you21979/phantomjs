%define name	phantomjs
%define version	2.0
%define release 0
%define prefix	/usr

%define mybuilddir %{_builddir}/%{name}-%{version}-root

Summary:	a headless WebKit with JavaScript API
Name:		%{name}
Version:	%{version}
License:	BSD
Release:	%{release}
Packager:	Matthew Barr <mbarr@snap-interactive.com>
Group:		Utilities/Misc
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%install
mkdir -p %{mybuilddir}%{prefix}/bin
mkdir -p %{mybuilddir}%{prefix}/share/%{name}/examples
cp bin/%{name} %{mybuilddir}%{prefix}/bin/%{name}
cp examples/* %{mybuilddir}%{prefix}/share/%{name}/examples/
cp CONTRIBUTING.md %{mybuilddir}%{prefix}/share/%{name}/
cp ChangeLog %{mybuilddir}%{prefix}/share/%{name}/
cp LICENSE.BSD %{mybuilddir}%{prefix}/share/%{name}/
cp README.md %{mybuilddir}%{prefix}/share/%{name}/

%files
%defattr(0444,root,root)
%attr(0555,root,root)%{prefix}/bin/%{name}
%{prefix}/share/%{name}/ChangeLog
%{prefix}/share/%{name}/CONTRIBUTING.md
%{prefix}/share/%{name}/examples/walk_through_frames.js
%{prefix}/share/%{name}/examples/direction.js
%{prefix}/share/%{name}/examples/simpleserver.js
%{prefix}/share/%{name}/examples/printenv.js
%{prefix}/share/%{name}/examples/sleepsort.js
%{prefix}/share/%{name}/examples/arguments.js
%{prefix}/share/%{name}/examples/serverkeepalive.js
%{prefix}/share/%{name}/examples/loadspeed.js
%{prefix}/share/%{name}/examples/waitfor.js
%{prefix}/share/%{name}/examples/run-jasmine.js
%{prefix}/share/%{name}/examples/netlog.js
%{prefix}/share/%{name}/examples/imagebin.js
%{prefix}/share/%{name}/examples/stdin-stdout-stderr.js
%{prefix}/share/%{name}/examples/child_process-examples.js
%{prefix}/share/%{name}/examples/follow.js
%{prefix}/share/%{name}/examples/echoToFile.js
%{prefix}/share/%{name}/examples/printheaderfooter.js
%{prefix}/share/%{name}/examples/features.js
%{prefix}/share/%{name}/examples/postserver.js
%{prefix}/share/%{name}/examples/detectsniff.js
%{prefix}/share/%{name}/examples/useragent.js
%{prefix}/share/%{name}/examples/seasonfood.js
%{prefix}/share/%{name}/examples/technews.js
%{prefix}/share/%{name}/examples/hello.js
%{prefix}/share/%{name}/examples/rasterize.js
%{prefix}/share/%{name}/examples/postjson.js
%{prefix}/share/%{name}/examples/run-jasmine2.js
%{prefix}/share/%{name}/examples/injectme.js
%{prefix}/share/%{name}/examples/weather.js
%{prefix}/share/%{name}/examples/phantomwebintro.js
%{prefix}/share/%{name}/examples/netsniff.js
%{prefix}/share/%{name}/examples/loadurlwithoutcss.js
%{prefix}/share/%{name}/examples/ipgeocode.js
%{prefix}/share/%{name}/examples/openurlwithproxy.js
%{prefix}/share/%{name}/examples/movies.js
%{prefix}/share/%{name}/examples/modernizr.js
%{prefix}/share/%{name}/examples/printmargins.js
%{prefix}/share/%{name}/examples/module.js
%{prefix}/share/%{name}/examples/server.js
%{prefix}/share/%{name}/examples/fibo.js
%{prefix}/share/%{name}/examples/post.js
%{prefix}/share/%{name}/examples/colorwheel.js
%{prefix}/share/%{name}/examples/page_events.js
%{prefix}/share/%{name}/examples/scandir.js
%{prefix}/share/%{name}/examples/universe.js
%{prefix}/share/%{name}/examples/render_multi_url.js
%{prefix}/share/%{name}/examples/version.js
%{prefix}/share/%{name}/examples/tweets.js
%{prefix}/share/%{name}/examples/countdown.js
%{prefix}/share/%{name}/examples/outputEncoding.js
%{prefix}/share/%{name}/examples/run-qunit.js
%{prefix}/share/%{name}/examples/pagecallback.js
%{prefix}/share/%{name}/examples/pizza.js
%{prefix}/share/%{name}/examples/unrandomize.js
%{prefix}/share/%{name}/LICENSE.BSD
%{prefix}/share/%{name}/README.md

%changelog
* Fri Apr 18 2014 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Tue Apr 30 2013 Eric Heydenberk <heydenberk@gmail.com>
- add missing filenames for examples to files section

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
