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

var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


(function($) {

  // Reverse
  // =============================================
  $.fn.reverse = [].reverse;

  // jQuery Extended Family Selectors
  // =============================================
  $.fn.cousins = function(filter) {
    return $(this).parent().siblings().children(filter);
  };

  $.fn.piblings = function(filter) {
    return $(this).parent().siblings(filter);
  };

  $.fn.niblings = function(filter) {
    return $(this).siblings().children(filter);
  };

  // Update
  // =============================================
  $.fn.update = function() {
    return $(this);
  };

  // Dropdown
  // =============================================
  $.fn.dropdown = function(options) {

    // Store object
    var $this = $(this);

    // Settings
    var settings = $.extend({
      className : 'toggled',
    }, options);

    // Simplify variable names
    var className = settings.className;

    // List selectors
    var $ul = $this.find('ul'),
        $li = $this.find('li'),
        $a  = $this.find('a');

    // Menu selectors
    var $drawers = $a.next($ul),      // All unordered lists after anchors are drawers
        $buttons = $drawers.prev($a), // All anchors previous to drawers are buttons
        $links   = $a.not($buttons);  // All anchors that are not buttons are links

    // Toggle menu on-click
    $buttons.on('click', function() {
      var $button = $(this),
          $drawer = $button.next($drawers),
          $piblingDrawers = $button.piblings($drawers);

      // Toggle button and drawer
      $button.toggleClass(className);
      $drawer.toggleClass(className).css('height', '');

      // Reset children
      $drawer.find($buttons).removeClass(className);
      $drawer.find($drawers).removeClass(className).css('height', '');

      // Reset cousins
      $piblingDrawers.find($buttons).removeClass(className);
      $piblingDrawers.find($drawers).removeClass(className).css('height', '');

      // Animate height auto
      $drawers.update().reverse().each(function() {
        var $drawer = $(this);
        if($drawer.hasClass(className)) {
          var $clone = $drawer.clone().css('display', 'none').appendTo($drawer.parent()),
              height = $clone.css('height', 'auto').height() + 'px';
          $clone.remove();
          $drawer.css('height', '').css('height', height);
        }
        else {
          $drawer.css('height', '');
        }
      });
    });

    // Close menu
    function closeMenu() {
      $buttons.removeClass(className);
      $drawers.removeClass(className).css('height', '');
    }

    // Close menu after link is clicked
    $links.click(function() {
      closeMenu();
    });

    // Close menu when off-click and focus-in
    $(document).on('click focusin', function(event) {
      if(!$(event.target).closest($buttons.parent()).length) {
        closeMenu();
      }
    });
  };
})(jQuery);

