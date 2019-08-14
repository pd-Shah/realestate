    function openNav() {
      document.getElementById("mySidepanel").style.width = "250px";
    }

  function closeNav() {
      document.getElementById("mySidepanel").style.width = "0";
    }

// map
function openNav() {
  document.getElementById("mySidepanel").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}

// CEDARMAPS_ACCESS_TOKEN change it with your own token

function contactMap() {
  // Map options
  var cm_options = {
    "center": {
      "lat": 35.726854,
      "lng": 51.525357
    },
    "maptype": "light",
    "scrollWheelZoom": false,
    "zoomControl": true,
    "zoom": 17,
    "minZoom": 6,
    "maxZoom": 17,
    "legendControl": false,
    "attributionControl": false
  }
  // Initialized CedarMap
  var map = window.L.cedarmaps.map('map_f0zsce',
    'https://api.cedarmaps.com/v1/tiles/cedarmaps.streets.json?access_token=ae7d1b021ae8f6785260040172ce86005372ed2d', cm_options);
  // Markers options
  var markers = [{
    "popupContent": "تهران",
    "center": {
      "lat": 35.726854,
      "lng": 51.525357
    },
    "iconOpts": {
      "iconUrl": "https://api.cedarmaps.com/v1/markers/marker-default.png",
      "iconRetinaUrl": "https://api.cedarmaps.com/v1/markers/marker-default@2x.png",
      "iconSize": [82, 98]
    }
  }];
  var markersLeaflet = [];
  var _marker = null;

  map.setView(cm_options.center, cm_options.zoom);
  // Add Markers on Map
  if (markers.length === 0) return;
  markers.map(function (marker) {
    var iconOpts = {
      iconUrl: marker.iconOpts.iconUrl,
      iconRetinaUrl: marker.iconOpts.iconRetinaUrl,
      iconSize: marker.iconOpts.iconSize,
      popupAnchor: [0, -49]
    };

    const markerIcon = {
      icon: window.L.icon(iconOpts)
    };

    _marker = new window.L.marker(marker.center, markerIcon);
    markersLeaflet.push(_marker);
    if (marker.popupContent) {
      _marker.bindPopup(marker.popupContent);
    }
    _marker.addTo(map);
  });
  // Bounding Map to Markers
  if (markers.length > 1) {
    var group = new window.L.featureGroup(markersLeaflet);
    map.fitBounds(group.getBounds(), {
      padding: [30, 30]
    });
  }
};

(function (c, e, d, a) {
  var p = c.createElement(e);
  p.async = 1;
  p.src = d;
  p.onload = a;
  c.body.appendChild(p);
})(document, 'script', 'https://api.cedarmaps.com/cedarmaps.js/v1.8.0/cedarmaps.js', contactMap);

function getclick()
{
    this.style.background-color: #EFF2F7;
}
