var Main = require('./main.vue');
var Axios = require('axios');

function processInstagram(data) {
    var lastYear = null;
    var lastMonth = null;
    var images = [];
    var menuItems = [];
    var menuIndex = 0;
    var monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];
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
        if (month !== lastMonth) {
            menuItems[menuIndex].items.push({
                name: monthNames[month],
                id: year + '-' + (month + 1)
            });
            lastMonth = month;
        }
        images.push(item);
    });
    return {
        menuItems: menuItems,
        images: images
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
