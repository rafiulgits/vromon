var head = document.getElementsByTagName('head')[0];

var insertBefore = head.insertBefore;

head.insertBefore = function (newElement, referenceElement) {

    if (newElement.href && newElement.href.indexOf('//fonts.googleapis.com/css?family=Roboto') > -1) {

        console.info('Prevented Roboto from loading!');
        return;
    }

    insertBefore.call(head, newElement, referenceElement);
};

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 40,
            lng: 50
        },
        zoom: 4,
        mapTypeId: 'roadmap'
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var currentPosition = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            map.setCenter(currentPosition);
            map.setZoom(15);
            var marker = new google.maps.Marker({
                position: currentPosition,
                map: map,
                title: 'Here you are!'
            });
            var marker2 = new google.maps.Marker({
                position: {lat: 23.8365038, lng: 90.3766814},
                map: map,
                title: 'Chillox!'
            });
        });
    } else {
        console.log("Your browser is backdated!");
    }
}
