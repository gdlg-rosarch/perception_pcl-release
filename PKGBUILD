# Script generated with Bloom
pkgdesc="ROS - PCL (Point Cloud Library) ROS interface stack. PCL-ROS is the preferred bridge for 3D applications involving n-D Point Clouds and 3D geometry processing in ROS."
url='http://ros.org/wiki/perception_pcl'

pkgname='ros-kinetic-pcl-ros'
pkgver='1.4.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'pcl'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-genmsg'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-nodelet-topic-tools'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-rosbag'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2-eigen'
)

depends=('eigen3'
'pcl'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-nodelet-topic-tools'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-rosbag'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2-eigen'
)

conflicts=()
replaces=()

_dir=pcl_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/pcl_ros $srcdir/pcl_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

