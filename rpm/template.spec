Name:           ros-indigo-pointcloud-to-laserscan
Version:        1.2.8
Release:        0%{?dist}
Summary:        ROS pointcloud_to_laserscan package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-tf2-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-tf2-sensor-msgs

%description
Converts a 3D Point Cloud into a 2D laser scan. This is useful for making
devices like the Kinect appear like a laser scanner for 2D-based algorithms
(e.g. laser-based SLAM).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 03 2018 Paul Bovbel <paul@bovbel.com> - 1.2.8-0
- Autogenerated by Bloom

* Mon Jun 08 2015 Paul Bovbel <paul@bovbel.com> - 1.2.7-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Paul Bovbel <paul@bovbel.com> - 1.2.6-0
- Autogenerated by Bloom

* Tue Jan 20 2015 Paul Bovbel <paul@bovbel.com> - 1.2.5-0
- Autogenerated by Bloom

* Thu Jan 15 2015 Paul Bovbel <paul@bovbel.com> - 1.2.4-0
- Autogenerated by Bloom

* Sat Jan 10 2015 Paul Bovbel <paul@bovbel.com> - 1.2.3-0
- Autogenerated by Bloom

* Sat Oct 25 2014 Paul Bovbel <paul@bovbel.com> - 1.2.2-0
- Autogenerated by Bloom

