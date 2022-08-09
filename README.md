# scoords

The ``scoords`` library defines an ``astropy`` custom coordinate frame. This allows to specify coordinates relative to the local spacecraft coordinates and transform them to any other system using ``astropy``'s machinery.

``SkyCoord`` objects are instantiated by passing a location with specified units and a coordinate frame. Use ``SpacecraftFrame`` to specify a coordinate in the reference system attached to the spacecraft:


```python
import astropy.units as u
from astropy.coordinates import SkyCoord
from scoords import SpacecraftFrame

c = SkyCoord(lon = 45*u.deg, lat = 10*u.deg, frame = SpacecraftFrame())
```

This allows you to know the reference frame of the coordinate, e.g.


```python
c.frame
```




    <SpacecraftFrame Coordinate (attitude=None, obstime=None, location=None): (lon, lat) in deg
        (45., 10.)>



However, in order to transform it into other coordinate system you need to specify the orientation of the spacecraft with respect to an inertial reference frame --i.e. the attitude


```python
from scoords import Attitude

attitude = Attitude.from_rotvec(45*u.deg*[0,0,1], frame = 'icrs')

c = SkyCoord(lon = 0*u.deg, lat = 0*u.deg, frame = SpacecraftFrame(attitude = attitude))
```

There are class methods to specify the orientation in any of the following formats:
- A rotation matrx
- A vector co-directional to the axis of rotation
- A quaternion
- A `scipy`'s `Rotation` object
- The direction the spacecraft coordinates axes point to

Once the attitude is specified, we can transform from/to any other frame supported by astropy


```python
c.transform_to('icrs')
```




    <SkyCoord (ICRS): (ra, dec) in deg
        (45., 0.)>




```python
c.transform_to('galactic')
```




    <SkyCoord (Galactic): (l, b) in deg
        (176.96129126, -48.90264434)>



Although it does not play a role in this particular coordinates transformation, the observation time and location can also be specified in case it is needed by any other algorithm:


```python
from astropy.time import Time
from astropy.coordinates import EarthLocation

frame = SpacecraftFrame(attitude = attitude,
                        obstime = Time('2026-01-01T00:00:00'),
                        location = EarthLocation(lon = 10*u.deg, lat = 46*u.deg, height = 400*u.km))

c = SkyCoord(lon = 45*u.deg, lat = 10*u.deg, frame = frame)
```


```python
c.frame.obstime
```




    <Time object: scale='utc' format='isot' value=2026-01-01T00:00:00.000>




```python
c.frame.location.geodetic
```




    GeodeticLocation(lon=<Longitude 10. deg>, lat=<Latitude 46. deg>, height=<Quantity 400. km>)


