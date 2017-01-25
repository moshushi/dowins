require('purecss/build/pure.css');
require('purecss/build/grids-responsive.css');

var Vue = require('vue');
var app = require('./components/app.vue');
var v = new Vue({
    el: '#app',
    data: {
        currentRoute: window.location.hash
    },
    render: function render(handler) {
        return handler(app);
    }
});

window.addEventListener('popstate', function popstate() {
    v.currentRoute = window.location.hash;
});
