var Main = require('./main.vue');
var lib = require('../lib.js');
var Axios = require('axios');

function processInstagram(data) {
    var lastYear = null;
    var lastMonth = null;
    var images = [];
    var menuItems = [];
    var monthIds = [];
    var menuIndex = 0;
    var monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];
    var previousUrl = null;
    data.forEach(function iterateArray(item) {
        var itemDate = new Date(item.date);
        var year = itemDate.getFullYear();
        if (year !== lastYear) {
            menuItems.push({year: year, items: []});
            menuIndex = menuItems.length - 1;
            lastMonth = null;
            lastYear = year;
        }
        var month = itemDate.getMonth();
        var monthId = year + '-' + (month + 1 > 9 ? month + 1 : '0' + (month + 1));
        if (month !== lastMonth) {
            menuItems[menuIndex].items.push({
                name: monthNames[month],
                id: monthId,
                url: lib.makeUrl(monthId)
            });
            monthIds.push(monthId);
            lastMonth = month;
        }
        item.displayDate = itemDate.toLocaleString('uk-UA');
        item.monthId = monthId;
        item.id = item.url.split('/')[4];
        item.currentUrl = lib.makeUrl(item.monthId, item.id);
        // set previousID of current element and nextID of previous element
        item.nextUrl = null;
        if (previousUrl !== null) {
            // this is not the first image
            images[images.length - 1].nextUrl = item.currentUrl;
        }
        item.previousUrl = previousUrl;
        previousUrl = item.currentUrl;
        // format hashtags
        item.text = item.text.replace(
            /(#[^\s]+)/g,
            '<span class="hashtag">$1</span> '
        );
        images.push(item);
    });
    return {
        menuItems: menuItems,
        images: images,
        defaultMonth: monthIds[0]
    };
}

module.exports = {
    name: 'app',
    data: function controller() {
        return {
            instagram: {}
        };
    },
    components: {
        'main-component': Main
    },
    beforeMount: function beforeMount() {
        var self = this;
        Axios.get('data.json').then(
            function success(response) {
                self.instagram = processInstagram(response.data);
            }
        );
    }
};
