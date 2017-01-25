require('purecss/build/pure.css');
require('purecss/build/grids-responsive.css');

var Vue = require('vue');
var app = require('./components/app.vue');
var v = new Vue({
    el: '#app',
    data: {
        instagram: []
    },
    render: function render(handler) {
        return handler(app);
    }
});
